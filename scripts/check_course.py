"""Validate navigation, catalog coverage, input paths, and teaching assets."""
from pathlib import Path
import ast
import hashlib
import json
import os
import re
import sys
import warnings
import zipfile
from urllib.parse import unquote, urlsplit

import nbformat
from IPython.core.inputtransformer2 import TransformerManager
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def markdown_links():
    checked = 0
    for document in sorted(ROOT.rglob('*.md')):
        if any(part in {'.git', 'artifacts', '.venv', '.venv-tf'} for part in document.parts):
            continue
        source = document.read_text(encoding='utf-8')
        source = re.sub(r'```.*?```', '', source, flags=re.S)
        for link in re.findall(r'!?\[[^\]\n]*\]\(([^)]+)\)', source):
            target = link.strip().split(' "', 1)[0].strip('<>')
            uri = urlsplit(target)
            if uri.scheme or uri.netloc:
                continue
            resolved = (document.parent / unquote(uri.path)).resolve() if uri.path else document
            require(resolved.is_relative_to(ROOT), f'Link leaves repository: {document}: {target}')
            require(resolved.exists(), f'Broken link: {document.relative_to(ROOT)}: {target}')
            if uri.fragment and resolved.suffix == '.md':
                headings = re.findall(r'^#{1,6}\s+(.+?)\s*#*$', resolved.read_text(encoding='utf-8'), re.M)
                anchors = {re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-') for heading in headings}
                require(unquote(uri.fragment) in anchors, f'Broken heading link: {target}')
            checked += 1
    return checked


def main():
    catalog = json.loads((ROOT / 'docs/course-catalog.json').read_text(encoding='utf-8'))
    entries = {item['path']: item for item in catalog['notebooks']}
    require(len(entries) == len(catalog['notebooks']), 'Duplicate notebook catalog entries')
    disk = {str(p.relative_to(ROOT)) for parent in ['modules', 'assignments'] for p in (ROOT / parent).rglob('*.ipynb')}
    require(set(entries) == disk, f'Notebook catalog mismatch: {set(entries) ^ disk}')
    transformer = TransformerManager()
    allowed = {(item['notebook'], item['cell_index']): item for item in catalog['allowed_incomplete_cells']}
    incomplete = 0
    code_cells = 0
    for path in entries:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', nbformat.warnings.MissingIDFieldWarning)
            notebook = nbformat.read(ROOT / path, as_version=4)
            nbformat.validate(notebook)
        for index, item in enumerate(notebook.cells):
            if item.cell_type != 'code':
                continue
            code_cells += 1
            try:
                ast.parse(transformer.transform_cell(item.source), filename=path)
            except SyntaxError as error:
                allowance = allowed.get((path, index))
                digest = hashlib.sha256(item.source.encode()).hexdigest()
                require(allowance and digest == allowance['source_sha256'], f'Unexpected syntax error: {path}, cell {index}: {error}')
                incomplete += 1

    references = catalog['dataset_references']
    for item in references:
        require(item['notebook'] in entries, f'Unknown notebook reference: {item}')
        nb = json.loads((ROOT / item['notebook']).read_text(encoding='utf-8'))
        sources = [''.join(c.get('source', [])) for c in nb['cells'] if c['cell_type'] == 'code']
        require(any(item['path'] in s for s in sources), f'Catalog input not referenced in notebook: {item}')
        setup = next((s for s in sources if 'COURSE_ROOT = next(' in s), None)
        require(setup, f'Missing repository setup cell: {item["notebook"]}')
        original_cwd = Path.cwd()
        try:
            os.chdir((ROOT / item['notebook']).parent)
            namespace = {}
            exec(compile(setup, item['notebook'], 'exec'), namespace)
            require(namespace['COURSE_ROOT'] == ROOT, f'Incorrect input root: {item["notebook"]}')
        finally:
            os.chdir(original_cwd)
        if item['availability'] == 'bundled':
            require((ROOT / item['path']).is_file(), f'Missing bundled input: {item}')
        else:
            require((ROOT / item['path']).parent.joinpath('README.md').exists(), f'Undocumented external input: {item}')

    exported_pages = 0
    for item in catalog['slide_exports']:
        with zipfile.ZipFile(ROOT / item['source']) as source:
            slides = sum(name.startswith('ppt/slides/slide') and name.endswith('.xml') and '/_rels/' not in name for name in source.namelist())
        pages = len(PdfReader(ROOT / item['pdf']).pages)
        require(pages == slides and pages > 0, f'Slide export page count differs: {item}')
        exported_pages += pages
    pdf_files = [p for directory in ['modules', 'projects', 'docs'] for p in (ROOT / directory).rglob('*.pdf')]
    for pdf in pdf_files:
        require(len(PdfReader(pdf).pages) > 0, f'Unreadable PDF: {pdf}')
    for item in catalog['modules']:
        module = ROOT / item['path']
        for part in ['README.md', 'code', 'slides/README.md', 'slides/pdf', 'slides/source', 'datasets/README.md']:
            require((module / part).exists(), f'Missing module component: {module / part}')
    migration = json.loads((ROOT / 'docs/migration-map.json').read_text(encoding='utf-8'))
    for item in migration['files']:
        require((ROOT / item['new_path']).exists(), f'Missing migrated file: {item}')
    links = markdown_links()
    result = {'notebooks': len(entries), 'code_cells_parsed': code_cells,
              'known_student_placeholders': incomplete, 'local_markdown_links': links,
              'dataset_references': len(references), 'pdfs': len(pdf_files),
              'slide_exports': len(catalog['slide_exports']), 'exported_pages': exported_pages,
              'original_files_mapped': len(migration['files'])}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'Course validation failed: {error}', file=sys.stderr)
        sys.exit(1)
