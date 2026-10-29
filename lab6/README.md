# Lab 6 — Code and Branch Coverage Analysis

## Objective
To measure and improve code coverage and branch coverage for the assigned Spam Scoring application using Python, `pytest`, and `coverage.py`.

## Application
The application scores messages based on spam-related words, uppercase words, link counts, and whether the sender is known. It classifies messages as `spam`, `suspicious`, or `clean`, and summarizes the inbox status.

## Files

| File | Description |
|---|---|
| `spam_scoring.py` | Spam scoring application under test |
| `CodeCoverageTest_Pes1ug24am272_application.py` | Test cases for code coverage |
| `BranchCoverageTest_Pes1ug24am272_application.py` | Test cases for branch coverage |
| `code_coverage_report.txt` | Code coverage report |
| `branch_coverage_report.txt` | Branch coverage report |
| `code_coverage_screenshot.svg` | Code coverage terminal evidence |
| `branch_coverage_screenshot.svg` | Branch coverage terminal evidence |
| `code_evidence.txt` | Code coverage command output |
| `branch_evidence.txt` | Branch coverage command output |

## Requirements

- Python 3.x
- pytest
- coverage

Install the dependencies:

```bash
python -m pip install pytest coverage
```

## 1. Code Coverage Analysis

Run the code coverage test suite:

```bash
coverage erase
coverage run -m pytest -q CodeCoverageTest_Pes1ug24am272_application.py
coverage report -m spam_scoring.py
```

Code coverage measures the proportion of executable statements exercised by the tests.

## 2. Branch Coverage Analysis

Run the branch coverage test suite:

```bash
coverage erase
coverage run --branch -m pytest -q BranchCoverageTest_Pes1ug24am272_application.py
coverage report -m spam_scoring.py
```

Branch coverage checks whether the alternative outcomes of decision statements have been exercised.

## Results

The prepared test suites target at least 90% code coverage and branch coverage. Refer to the accompanying coverage reports and terminal evidence for the recorded results.

## Conclusion

The lab demonstrates how systematic test cases can improve confidence in the spam-scoring application by exercising its statements, decision branches, boundary conditions, classification logic, and inbox-status calculations.
