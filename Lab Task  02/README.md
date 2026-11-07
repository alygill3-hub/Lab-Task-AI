# Lab 2: Intelligent Agents and PEAS

**Course:** CAI601400 - Artificial Intelligence
**Name:** (your name) | **ID:** (your ID)
**University / Program:** (your university and program)

## Overview
This lab uses a smart classroom energy agent as the case study. The agent reads the room temperature and whether the room is occupied, and then chooses an operating mode so that energy is not wasted when nobody is inside.

The lab has three parts:
1. PEAS specifications for a delivery robot and an LLM-based student-support agent (in the report).
2. Classification of both environments as fully or partially observable and as deterministic or stochastic (in the report).
3. A stateful version of the classroom agent that remembers its last mode and does not send the same command again.

## Requirements
- Python 3.8 or higher. No extra libraries are needed.
- Keep all `.py` files in one folder, since `lab2_check.py` imports the agent from `lab2_model.py`.

## Running the Code
Open a terminal in the project folder and run:

```
python lab2_percepts.py
python lab2_model.py
python lab2_check.py
```

If `python` is not recognised, use `python3` or `py` instead.

To save the printed results into text files (stored in `outputs/`):

```
python lab2_percepts.py > outputs/lab2_percepts_output.txt
python lab2_check.py > outputs/lab2_check_output.txt
```

## Files
| File | Description |
|---|---|
| `lab2_percepts.py` | Reflex agent from the lab manual. It processes six percepts and prints the target mode for each. It has no memory, so a repeated hot reading gives COOL twice. |
| `lab2_model.py` | Stateful agent. It stores the last mode and returns the target mode together with a flag saying whether a command must be sent. A command is sent only when the mode changes. |
| `lab2_check.py` | Test runs for the stateful agent. Each step prints the previous mode, the percept, the target mode and the command / no command result. |
| `Lab2_Report.docx` | Full report: PEAS tables, environment classification, reflex vs stateful comparison, trace, limitations, reflection and references. |
| `outputs/` | Saved output of the scripts. |

## Test Cases
- **Repeated percept:** the second identical reading should not send a command.
- **Exact boundaries (20 and 26):** both give IDLE, because the code uses `<` and `>`.
- **Mode change:** for example IDLE to WARM sends a new command.
- **Empty and hot room:** the result is ECO, since an empty room has priority over temperature.
- **Noisy readings around 26 C:** shows that remembering the last mode does not give hysteresis.

For the reflex agent, the manual expects COOL, COOL, IDLE, IDLE, WARM, ECO. I predicted this sequence before running the code and then compared it with the real output.

## Assumptions
- Temperature is in degrees Celsius and occupancy is True or False.
- ECO, COOL, WARM and IDLE are simulated mode labels only. No hardware is controlled.
- The thresholds 20 and 26 are lab values, not official comfort standards.
- Remembering the last mode is not learning. It only prevents repeated commands.

## References
- The `ClassroomAgent` code and the percept list in `lab2_percepts.py` are taken from the Lab 2 manual (Sections 2.4 and 2.5), CAI601400 Artificial Intelligence Lab Manual. The stateful agent and the tests were built on top of it.
