# Dataset guide

[Course home](../README.md) · [Notebook index](NOTEBOOKS.md)

Each module documents its data under `datasets/README.md`. Committed inputs are resolved from the repository root by setup cells, so moving lessons into `code/` does not break their file references.

| Module | Data preparation |
| --- | --- |
| [Python](../modules/01-python/datasets/README.md) | File-handling examples write small text files locally |
| [NumPy](../modules/02-numpy/datasets/README.md) | Bundled CSV/array examples; generated grayscale image for indexing |
| [Pandas](../modules/03-pandas/datasets/README.md) | Bundled heart-disease data, shared diabetes CSV, and small synthetic file-loading examples |
| [Visualization](../modules/04-data-visualization/datasets/README.md) | Bundled diabetes CSV |
| [Statistics](../modules/05-statistics-and-probability/datasets/README.md) | Values defined in notebook cells |
| [Machine learning](../modules/06-machine-learning/datasets/README.md) | Bundled SVM data; instructor must supply two regression CSVs |
| [Deep learning](../modules/07-deep-learning/datasets/README.md) | Keras digit/fashion downloads; external Kaggle CNN images |
| [NLP](../modules/08-natural-language-processing/datasets/README.md) | Bundled mock reviews; optional Kaggle sentiment extension |

The new small CSV/JSON/image examples are explicitly described as generated teaching data. All previously committed dataset files are preserved. Their original upstream attribution is recorded only where it was supplied; this reorganization does not invent data provenance.

Do not commit large external datasets, model weights, credentials, or private student submissions. Use the dataset documentation to share download/setup instructions instead.
