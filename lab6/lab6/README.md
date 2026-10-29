# Lab 6 — Code and Branch Coverage

This folder contains the application from the assigned spam-scoring repository and two separate test suites, one for statement/code coverage and one for branch coverage.

## Install

```bash
python -m pip install pytest coverage
```

## Code coverage stage

```bash
coverage erase
coverage run -m pytest -q CodeCoverageTest_Pes1ug24am272_application.py
coverage report -m spam_scoring.py
```

Evidence: `code_evidence.txt`, `code_coverage_report.txt`, and `code_coverage_screenshot.png`.

## Branch coverage stage

```bash
coverage erase
coverage run --branch -m pytest -q BranchCoverageTest_Pes1ug24am272_application.py
coverage report -m spam_scoring.py
```

Evidence: `branch_evidence.txt`, `branch_coverage_report.txt`, and `branch_coverage_screenshot.png`.

## Results from the execution environment used to prepare these files

- Code coverage suite: 13 passed; 100% statement coverage (39/39 statements).
- Branch coverage suite: 20 passed; 100% total coverage, 26/26 branches covered, zero partial branches.

## Commit requirement

For the two-commit requirement, commit the code-coverage test and its evidence first. Then commit the branch-coverage test and its evidence separately. See the submission steps provided in chat.
