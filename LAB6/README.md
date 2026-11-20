# Lab 6 — Phone Repair Quote

PES University · Software Engineering Lab · Code and Branch Coverage

**C NITISH** · **PES1UG25CS809** · [GitHub](https://github.com/nitish5052)

## About

A small Python module that quotes phone repairs by part, brand tier, warranty and express service, estimates turnaround time, and values phones offered for trade-in. The implementation comes from [the instructor’s Lab 6 starter](https://github.com/SETAPESU26/L6_L7_59_phone_repair_quote/tree/363593f10ca7f58571f7ada79754a1285919ea58/LAB6). Refer to the course handout for submission instructions.

## Setup and execution

Run from the repository root. These commands use Bash.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install pytest pytest-cov
python -m pytest test_phone_repair_quote.py -v
python -m pytest --cov=phone_repair_quote --cov-branch --cov-report=term-missing --cov-report=html:htmlcov -v
python -m coverage json -o /tmp/lab6-coverage.json
```

On Windows PowerShell, activate with `.\.venv\Scripts\Activate.ps1` and use `coverage.json` in place of `/tmp/lab6-coverage.json`. Open `htmlcov/index.html` to explore the generated coverage report. The coverage JSON gives the statement and branch percentages separately.

## Measured results

| Metric | Result |
|---|---:|
| pytest | 30 passed, 0 failed |
| Statement coverage | 40 of 40 (100%) |
| Branch coverage | 28 of 28 (100%) |
| Partial branches | 0 |

Statement coverage measures which executable lines ran. For example, an invalid part executes the quote validation's exception line. Branch coverage measures which possible destinations were reached from a decision. The invalid-part test takes the exception path, and a valid part takes the path to tier validation.

The 30 cases include both starter tests, all four repair parts, both brand tiers, warranty and express decisions, all stock and technician outcomes, invalid inputs, and the trade-in boundaries at 12/13, 24/25, and 48/49 months.

## Deliverables

| File | Description |
|---|---|
| `phone_repair_quote.py` | Module under test |
| `test_phone_repair_quote.py` | Starter tests and parameterized Lab 6 tests |
| `screenshots/pytest.png` | Successful verbose pytest run |
| `screenshots/branch-coverage.png` | Terminal statement and branch results |
| `screenshots/html-coverage.png` | Generated source coverage report |
| [PES1UG25CS809_C_NITISH_LAB6.pdf](PES1UG25CS809_C_NITISH_LAB6.pdf) | Test matrix, decision mapping, results and evidence |
| `.gitignore` | Python, pytest, virtual environment and generated coverage exclusions |
