# Dataset notes

[Module home](../README.md) · [Course dataset guide](../../../docs/DATASETS.md)

`breast_cancer.csv` is the original `06-ML/Dataset/data.csv`, renamed for clarity. The SVM lesson and assignment share this file. Two regression lessons need the original instructor-provided CSVs listed below; their upstream source was not recorded in the original repository.

## Bundled files

| File | Purpose |
| --- | --- |
| [breast_cancer.csv](breast_cancer.csv) | Original course file |

## Instructor-provided inputs

| Put the file here | Expected schema | Used by |
| --- | --- | --- |
| `external/placement.csv` | Numeric `cgpa` and `package` columns | Linear regression lecture and its alternate copy |
| `external/smart_healthcare_dataset1.csv` | Numeric predictors and target `health_risk_score` | Multiple linear regression |

Obtain these files from the instructor, then place them in the paths above. No substitute dataset is presented as the original. The external folder is ignored by Git; its committed README keeps the required location visible.

Run the notebook's **Course data paths** setup cell before reading bundled inputs. Files created by saving/export exercises use the notebook working directory. Existing dataset provenance is retained as found; no unrecorded source or license is assigned to original course data.
