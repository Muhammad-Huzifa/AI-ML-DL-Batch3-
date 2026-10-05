# AI, Machine Learning and Deep Learning — Batch 3

Classroom materials by **Muhammad Huzifa**: Python foundations, numerical computing, data analysis, machine learning, deep learning, and introductory NLP. Each module separates lesson notebooks, teaching slides, and datasets so students can find what they need before class.

**Start here:** [setup guide](docs/START_HERE.md) · [learning path](docs/COURSE_MAP.md) · [all notebooks](docs/NOTEBOOKS.md) · [all slides](docs/SLIDES.md)

## Learning path

| Order | Module | Notebooks, including exercises and preserved copies |
| --- | --- | --- |
| 01 | [Python foundations](modules/01-python/README.md) | 12 |
| 02 | [NumPy](modules/02-numpy/README.md) | 6 |
| 03 | [Pandas](modules/03-pandas/README.md) | 4 |
| 04 | [Data visualization](modules/04-data-visualization/README.md) | 5 |
| 05 | [Statistics and probability](modules/05-statistics-and-probability/README.md) | 2 |
| 06 | [Machine learning](modules/06-machine-learning/README.md) | 5 |
| 07 | [Deep learning](modules/07-deep-learning/README.md) | 17 |
| 08 | [Natural language processing](modules/08-natural-language-processing/README.md) | 1 |

## Quick start

Use **Python 3.11**. Run these commands from a terminal:

```bash
git clone https://github.com/Muhammad-Huzifa/ai-ml-dl-course-batch-3.git
cd ai-ml-dl-course-batch-3
python -m venv .venv
```

Activate the environment:

| Terminal | Command |
| --- | --- |
| Windows PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |
| Linux/macOS | `source .venv/bin/activate` |

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

Open a notebook through Jupyter's file browser. Before the ANN, CNN, or RNN lessons, follow the [TensorFlow setup](docs/START_HERE.md#tensorflow-lessons). The image section of NumPy has a separate optional extra.

## Repository layout

| Folder | Contents |
| --- | --- |
| `modules/` | Eight numbered modules; each has `code/`, `slides/`, and `datasets/` |
| `assignments/` | Python, machine learning, and deep learning assignments in teaching order |
| `projects/atm/` | Console ATM teaching project, sample data, and project brief |
| `docs/` | Setup, course map, notebook/slide indexes, dataset notes, and original outline |
| `assets/references/` | Attributed supplementary reference image and its license |
| `requirements/` | Base, image, TensorFlow, and validation dependencies |
| `scripts/` | Course structure checks and selected CPU example execution |

Within a module, `slides/pdf/` contains the available reading copies and `slides/source/` contains all editable original decks. `code/exercises/` contains practice work; `code/archive/` holds clearly labeled alternate copies. Deep learning further groups notebooks into `ann/` and `cnn/`.

## Study and practice

1. Read the module README and its PDF slides.
2. Open the lesson in a fresh kernel and run its setup cell first.
3. Work through the examples, then complete the exercises and [assignments](assignments/README.md).
4. Use [dataset notes](docs/DATASETS.md) before running lessons that need external CSVs or image collections.

The Day 1/Day 2 Python worksheets intentionally contain unanswered cells. External CNN datasets and two instructor-provided regression CSVs are listed explicitly; they are not downloaded automatically. [Notebook guidance](docs/NOTEBOOKS.md) distinguishes runnable samples, guided lessons, worksheets, and alternate copies.

Try the [ATM project](projects/atm/README.md) after functions and OOP. For supplementary study, use the [official resource list](docs/RESOURCES.md).

## Maintenance

```bash
python -m pip install -r requirements/validation.txt
python scripts/check_course.py
python scripts/run_cpu_examples.py
```

See [validation scope](docs/VALIDATION.md) and [contributing](CONTRIBUTING.md). The [migration map](docs/migration-map.json) records every original file's new location; all 60 original notebooks and all existing teaching assets are retained.
