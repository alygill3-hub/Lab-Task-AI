# Lab 3: Uninformed Search (BFS, DFS, DLS, IDDFS, UCS)
Course: CAI601400 - Artificial Intelligence

## Requirements
- Python 3.8 or higher.
- No external libraries are used, only the Python standard library.
- All three `.py` files must stay together in one folder (`lab3/`) because they import from each other.

## How to Run
Open a terminal in the `lab3/` folder and run:

```
python lab3_bfs_dfs.py        # Task 1: BFS and DFS traces, verification and edge cases
python lab3_depth_search.py   # Task 2: DLS (limits 1-4), IDDFS (max depths 1-4) and edge cases
python lab3_ucs.py            # Task 3: weighted graph, UCS, BFS comparison and edge cases
```

The saved program outputs are in the `outputs/` folder.

## Project Files
| File | What it does |
|---|---|
| `lab3_bfs_dfs.py` | BFS and DFS from the lab manual (Section 3.2), extended to print the frontier at each step |
| `lab3_depth_search.py` | DLS returning FOUND, CUTOFF or FAILURE with a path-local cycle check, plus IDDFS |
| `lab3_ucs.py` | Weighted graph with the added C -> G corridor, UCS using `heapq`, and an independent cost check |
| `outputs/` | Saved output of each program |

## Assumptions
- The start node is A and the goal node is G. Neighbours are explored in the order they are listed in the graph.
- Depth is counted in edges, so A has depth 0. The goal node is counted as processed when it is removed from the frontier.
- Edge weights are non-negative sample travel-cost values. The C -> G corridor is added only for the weighted experiment and is not part of the original graph.

## References
- The BFS and DFS functions are taken from the Lab 3 manual (CAI601400 Artificial Intelligence Lab Manual, Section 3.2) and are cited as borrowed code.
