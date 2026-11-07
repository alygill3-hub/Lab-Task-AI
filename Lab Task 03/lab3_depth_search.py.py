"""Lab 3 Task 2: DLS and IDDFS. Depth counts edges (A = depth 0). Cycle check is path-local."""
from lab3_bfs_dfs import graph


def dls(g, node, goal, limit, path, order):
    order.append(node)
    if node == goal: return "FOUND", path
    if limit == 0:                         # deeper unexplored continuation -> CUTOFF, else FAILURE
        return ("CUTOFF" if any(n not in path for n in g[node]) else "FAILURE"), None
    cutoff = False
    for n in g[node]:
        if n not in path:                  # path-local cycle check
            s, p = dls(g, n, goal, limit - 1, path + [n], order)
            if s == "FOUND": return s, p
            cutoff = cutoff or s == "CUTOFF"
    return ("CUTOFF" if cutoff else "FAILURE"), None


def iddfs(g, start, goal, max_depth):
    total = 0
    for limit in range(max_depth + 1):     # fresh DLS each time, no global visited set
        order = []
        s, p = dls(g, start, goal, limit, [start], order)
        total += len(order)
        if s != "CUTOFF": break
    return s, p, list(range(limit + 1)), total


if __name__ == "__main__":
    for limit in (1, 2, 3, 4):
        order = []
        s, p = dls(graph, "A", "G", limit, ["A"], order)
        print(f"DLS limit {limit}: {s}, path={p}, processed={order}")
    for m in (1, 2, 3, 4):
        s, p, tried, total = iddfs(graph, "A", "G", m)
        print(f"IDDFS max depth {m}: {s}, path={p}, limits attempted={tried}, node visits={total}")
    cyc = {"A": ["B"], "B": ["A", "C"], "C": [], "Z": []}      # A <-> B is a cycle, Z is unreachable
    print("Start = goal :", dls(graph, "A", "A", 0, ["A"], []))
    print("Unreachable  :", dls(graph, "C", "G", 3, ["C"], []))
    print("Cycle graph  :", dls(cyc, "A", "Z", 5, ["A"], []))