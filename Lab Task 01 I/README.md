# Lab 1: Introduction to AI and Paradigms

**Course:** CAI601400 - Artificial Intelligence
**Name:** (your name) | **ID:** (your ID)
**University / Program:** (your university and program)

## Overview
The case study for this lab is a scholarship screening prototype that flags incomplete applications. Two ways of deciding were compared: a transparent rule-based checker and a simple score/probability threshold. In this prototype "Review" only means that the application is sent to a human reviewer. It is not a scholarship decision.

The lab has three parts:
1. A sourced AI timeline with at least five milestones, including one AI winter and one modern compute/data milestone (in the report).
2. An extended rule-based checker with two extra named conditions, tested on four cases.
3. A short comparison explaining why passing a conversational test does not prove general intelligence (in the report).

## Requirements
- Python 3.8 or higher. No extra libraries are needed.
- The two scripts are independent, and each can be run on its own.

## Running the Code
Open a terminal in the project folder and run:

```
python lab1_compare.py
python lab1_rules.py
```

If `python` is not recognised, use `python3` or `py` instead.

To save the printed results into text files (stored in `outputs/`):

```
python lab1_compare.py > outputs/lab1_compare_output.txt
python lab1_rules.py > outputs/lab1_rules_output.txt
```

## Files
| File | Description |
|---|---|
| `lab1_compare.py` | Runs the rule-based checker and the probability threshold on four cases (complete_high, complete_low, incomplete_high, boundary) and prints where they disagree. |
| `lab1_rules.py` | Extended rule-based checker. It keeps `score >= 70` and document completeness, and adds two named conditions: `attendance_ok` and `no_disciplinary_record`. It runs four test cases and prints the input, expected result, actual result and reason for each. |
| `Lab1_Report.docx` | Full report: timeline, four rule tests, disagreement table, conversational-test comparison, limitations, reflection and references. |
| `outputs/` | Saved output of both scripts. |

## Testing
**`lab1_compare.py`:** I predicted the four rows before running the script. The manual expects:

| Case | Symbolic | Threshold | Disagreement |
|---|---|---|---|
| complete_high | Review | Review | False |
| complete_low | Hold | Review | True |
| incomplete_high | Hold | Review | True |
| boundary | Review | Review | False |

**`lab1_rules.py`:** The four cases are one full pass, one failure for each of the two new conditions, and one boundary case showing that a score of exactly 70 still passes. Together they cover every branch of the rule.

## Assumptions
- All thresholds (score 70, probability 0.70 and the limits of the two extra conditions) are made-up lab values, not real scholarship rules.
- The probability values are invented demonstration inputs. No model is trained, so nothing can be said about accuracy.
- There is no ground truth, so this compares behaviour and is not an accuracy experiment.
- No real student data is used.

## References
- The `rule_based` / `symbolic` and `probability_based` / `threshold` functions and the four-case list in `lab1_compare.py` come from the Lab 1 manual (Sections 1.4 and 1.5), CAI601400 Artificial Intelligence Lab Manual. `lab1_rules.py` was built on top of the manual's rule-based example.
- Sources for the timeline entries are listed in the references section of `Lab1_Report.docx`.
