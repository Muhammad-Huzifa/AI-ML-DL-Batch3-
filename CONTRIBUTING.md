# Contributing

Thank you for improving the Batch 3 course. Open an issue for a broken lesson path, unclear instruction, or proposed new topic. For a fix, create a branch or fork and submit a pull request describing the student-visible change.

## Adding material

- Put lesson notebooks in the appropriate module's `code/` folder and exercises in `code/exercises/`.
- Put reading PDFs in `slides/pdf/` and editable decks in `slides/source/`; update both after changing a deck.
- Put small permitted inputs in `datasets/` and document their source, license, schema, and preparation. Link large datasets instead of committing them.
- Update the module README, the central index, and `docs/course-catalog.json` when adding or moving a notebook.
- Keep student-answer TODOs in worksheets. Describe intentional incomplete cells in the catalog; do not suppress unrelated syntax errors.
- Clear stale notebook outputs after code/path changes and avoid committing credentials, personal student information, or trained model files.

## Checks

```bash
python -m pip install -r requirements.txt -r requirements/validation.txt
python scripts/check_course.py
python scripts/run_cpu_examples.py
```

The execution check covers the catalog's selected **CPU sample** notebooks. Explain any changes that require input prompts, TensorFlow downloads, or external training data in the pull request.
