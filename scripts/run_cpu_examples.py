"""Execute selected noninteractive notebook cells without a network kernel."""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def worker(notebook_path):
    from IPython.core.interactiveshell import InteractiveShell
    from IPython.utils.capture import capture_output

    class HeadlessShell(InteractiveShell):
        def enable_gui(self, gui=None):
            if gui is not None:
                raise RuntimeError(f'An unattended CPU example requested a GUI: {gui}')

    shell = HeadlessShell.instance()
    shell.run_line_magic('matplotlib', 'inline')
    notebook = json.loads(Path(notebook_path).read_text(encoding='utf-8'))
    executed = 0
    skipped = 0
    for index, cell in enumerate(notebook['cells']):
        if cell['cell_type'] != 'code':
            continue
        source = ''.join(cell.get('source', []))
        if source.strip().startswith('%pip '):
            # Dependencies are installed before the check, never by the lesson.
            skipped += 1
            continue
        with capture_output() as captured:
            result = shell.run_cell(source, store_history=True)
        if not result.success:
            raise RuntimeError(f'{notebook_path}, cell {index}: {result.error_before_exec or result.error_in_exec}\n{captured.stdout[-2000:]}')
        executed += 1
    print(json.dumps({'executed_code_cells': executed, 'skipped_install_cells': skipped}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, help='Optional path for the JSON execution report')
    parser.add_argument('--worker', help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        worker(args.worker)
        return
    catalog = json.loads((ROOT / 'docs/course-catalog.json').read_text(encoding='utf-8'))
    examples = [item for item in catalog['notebooks'] if item['runtime'] == 'CPU sample']
    require = ROOT / 'artifacts' / 'course-check'
    require.mkdir(parents=True, exist_ok=True)
    report = []
    for item in examples:
        with tempfile.TemporaryDirectory(prefix='example-', dir=require) as directory:
            env = dict(os.environ, MPLBACKEND='Agg', MPLCONFIGDIR=str(Path(directory) / 'mpl-cache'))
            process = subprocess.run([sys.executable, str(Path(__file__).resolve()), '--worker', str(ROOT / item['path'])], cwd=directory, env=env, capture_output=True, text=True, timeout=90)
            if process.returncode:
                raise RuntimeError(f'{item["path"]}\n{process.stdout[-2500:]}\n{process.stderr[-2500:]}')
            result = json.loads(process.stdout.strip().splitlines()[-1])
            record = {'notebook': item['path'], 'result': 'passed', **result}
            report.append(record)
            print(json.dumps(record), flush=True)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'Passed {len(report)} CPU notebooks; {sum(i["executed_code_cells"] for i in report)} code cells executed.', flush=True)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'CPU example validation failed: {error}', file=sys.stderr)
        sys.exit(1)
