# Validation scope

[Course home](../README.md) · [Notebook index](NOTEBOOKS.md)

## Course check

`python scripts/check_course.py` verifies notebook JSON/schema, Python cell syntax after Jupyter magic transformation, local Markdown links, notebook catalog coverage, portable bundled dataset paths, module folders, migration destinations, and PDF readability. For each exported slide deck it compares the PDF page count with the original PowerPoint slide count.

The two initial Python worksheets contain 19 original answer placeholders. Only those specific cells, matched by source fingerprint, are accepted as intentionally incomplete. Other syntax errors fail the check.

## CPU examples

`python scripts/run_cpu_examples.py` executes the catalog's nine **CPU sample** notebooks in separate Python processes with IPython cell handling and an inline Matplotlib backend. Temporary working folders hold generated practice files. A package-install cell is skipped because dependencies are installed before validation.

The samples cover dictionaries, sets, nested loops, NumPy saving/loading exercises, Pandas CSV/JSON examples, Matplotlib, descriptive statistics, probability, and the first linear regression example. This is an unattended example check, not execution of every classroom notebook through a full Jupyter server.

## Teaching and training limits

Interactive Python lessons, student worksheets, guided debugging tasks, notebooks needing instructor-supplied CSVs, TensorFlow training, framework dataset downloads, and external image-classification datasets are outside the automated CPU execution check. Their preparation is documented in the module READMEs and dataset guides.

The organization preserves all 60 original notebooks, the original PowerPoint/DOCX/PDF assets, bundled dataset files, and ATM application source. Seventeen notebooks received portable path setup and cleared stale outputs; the optional NLP extension now reads KaggleHub's returned folder directly. Alternate copies remain labeled in the indexes, and the migration map records the previous paths.

The six retained PDF exports are reading copies of the original decks. Reading margins are adjusted where needed; decks with unresolved source layout issues remain available in their original PowerPoint format. All 14 original PowerPoint files remain unchanged. Page counts and rendered pages are checked during the reorganization; changes to deck content should regenerate and visually review the corresponding PDF.

## CI

The **Course checks** GitHub Actions workflow installs the classroom and validation dependencies on Python 3.11, runs the course check, then executes the selected CPU samples. It does not train neural networks or download external datasets.
