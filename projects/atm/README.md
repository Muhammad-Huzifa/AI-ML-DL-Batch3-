# ATM console project

[Course home](../../README.md) · [Project brief](instructions/atm_project.pdf)

A classroom ATM simulation with account classes, login prompts, deposits/withdrawals, and JSON persistence. Read the original PDF brief, then inspect `account.py`, `atm.py`, and `main.py` in `code/`.

## Run

From the repository root:

```bash
cd projects/atm/code
python main.py
```

Run from `code/` because the original application opens `data.json` relative to the current working directory. It uses only Python's standard library.

## Sample accounts

| Card number | PIN | Original account label |
| --- | --- | --- |
| `2222` | `1234` | SavingsAccount |
| `1111` | `5555` | Current |

These values are the original demonstration data. The program changes balances in `code/data.json` while running; copy that file before experimenting if you want to restore the starting balances later. Keep the sample file for teaching and use separate local copies for student work.

The original account logic is retained as a teaching exercise. Follow the brief when extending validation, persistence, or account behavior.
