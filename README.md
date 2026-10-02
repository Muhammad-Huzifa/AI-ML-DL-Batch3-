# AI, Machine Learning and Deep Learning — Batch 3

Classroom notebooks, practice exercises, assignments, and slides taught by Muhammad Huzifa. Follow the numbered modules from Python foundations through numerical computing, data analysis, machine learning, deep learning, and introductory NLP.

## Module index

| Order | Module |
| --- | --- |
| 1 | [01-Python](01-Python/README.md) |
| 2 | [02-NumPy](02-NumPy/README.md) |
| 3 | [03-Pandas](03-Pandas/README.md) |
| 4 | [04-Matplotlib](04-Matplotlib/README.md) |
| 5 | [05-Statistics-Probability](05-Statistics-Probability/README.md) |
| 6 | [06-ML](06-ML/README.md) |
| 7 | [07-DL](07-DL/README.md) |
| 8 | [08-NLP](08-NLP/README.md) |

## Setup

Use Python 3.11 in a separate environment. Clone and open the project root:

```bash
git clone https://github.com/Muhammad-Huzifa/AI-ML-DL-Batch3-.git
cd AI-ML-DL-Batch3-
python -m venv .venv
```

| Terminal | Activation |
| --- | --- |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |
| Windows PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Windows Git Bash | `source .venv/Scripts/activate` |
| Linux/macOS | `source .venv/bin/activate` |

```bash
python -m pip install -r requirements.txt
jupyter lab
```

For TensorFlow ANN/CNN/RNN lessons, install `python -m pip install -r requirements-deep-learning.txt` in a separate environment. Larger image models may be better suited to Kaggle or Colab.

## Classroom workflow

Read the slides, follow the live notebook, and then complete the corresponding exercises. Material remains grouped by module; [assignments](Assignments/README.md) are indexed separately. Some worksheets are intentionally incomplete and require student solutions before they can run.

Read the [notebook execution guide](docs/NOTEBOOKS.md) for unfinished worksheets, CSV working directories, and external image datasets.

For the ATM example, open another terminal from the repository root:

```bash
cd "Assignments/Projects/ATM-Project"
python main.py
```

## Structure and status

Each numbered module contains its notebooks and teaching assets. Dataset files stay with their original lessons. PDF and PowerPoint files are preserved; this change adds navigation and setup instructions rather than replacing slides or lesson content.

Notebook inputs and external datasets depend on the lesson. These instructions and indexes have been checked against the actual file tree; every classroom exercise and deep-learning training run has not been executed during this pass.
