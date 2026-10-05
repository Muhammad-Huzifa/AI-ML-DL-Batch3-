# Start here

[Course home](../README.md) · [Learning path](COURSE_MAP.md) · [Notebook index](NOTEBOOKS.md)

## Base environment

Install Python 3.11 and Git, then use the clone and environment commands in the course README. Run all `pip` commands from the repository root with the environment activated. The base environment covers Python, NumPy, Pandas, visualization, statistics, and scikit-learn.

Start Jupyter with `jupyter lab`, then open a notebook from `modules/<module>/code/`. Select the kernel belonging to your environment. In VS Code, open the repository folder and select the same `.venv` interpreter for the notebook.

If your terminal uses `python3` instead of `python`, use it consistently when creating the environment. On Windows, `py -3.11 -m venv .venv` also selects Python 3.11 explicitly. If PowerShell activation is restricted, use Command Prompt with `.venv\Scripts\activate.bat`.

## Image-array lesson

The NumPy fancy-indexing notebook imports OpenCV for its image section:

```bash
python -m pip install -r requirements/image-processing.txt
```

A small generated grayscale array image is bundled with the lesson. Other NumPy examples use the base environment.

## TensorFlow lessons

Create a separate environment for ANN, CNN, and RNN notebooks:

```bash
python -m venv .venv-tf
```

Activate `.venv-tf` using the same terminal-specific pattern as `.venv`, then run:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-deep-learning.txt
python -m ipykernel install --user --name batch3-tf --display-name "Batch 3 - TensorFlow"
jupyter lab
```

Choose **Batch 3 - TensorFlow** in the notebook's kernel menu. Small dense-network examples can use a CPU; larger image models may take substantially longer. The original CNN notebooks with `/kaggle/input/` paths are prepared for Kaggle: attach the datasets named in the notebook before training. Colab users must clone the repository into their runtime before using the portable dataset setup cells.

## Running a lesson

Run each notebook separately and restart the kernel before switching lessons. Several classroom notebooks reuse variable names for unrelated examples. For notebooks with a **Course data paths** section, run its setup cell before loading data; it locates the repository from the current directory or its parents.

The Day 1/Day 2 practice notebooks have deliberately blank answers. Complete them before using **Run All**. Read the notebook's runtime label in the index; an exercise may be a debugging task or require student code, input prompts, downloads, or instructor-provided data.

## Generated files

File-handling and NumPy saving exercises create small files in their working directory. Pandas exercises export cleaned CSVs there too. These classroom outputs are ignored by Git; the committed files in module `datasets/` folders remain available as inputs and examples. Model weights, checkpoints, downloaded datasets, and student submissions are also ignored.

## Common fixes

| Symptom | Check |
| --- | --- |
| `ModuleNotFoundError` | Activate the correct environment, install its requirements, and select its Jupyter kernel |
| `FileNotFoundError` for a bundled CSV | Run the **Course data paths** setup cell inside the cloned repository |
| `FileNotFoundError` for `placement.csv` or the healthcare CSV | Follow the machine learning dataset README; these original inputs were not committed |
| Syntax error in Day 1/Day 2 practice | Fill in the student-answer placeholders |
| `/kaggle/input/` directory missing | Attach the required external image dataset in Kaggle or configure your own local folder |
| A cell asks for input | Run it interactively rather than through the automated CPU sample check |
