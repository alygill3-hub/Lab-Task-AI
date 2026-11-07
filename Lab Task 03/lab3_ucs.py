
import heapq
from lab3_bfs_dfs import bfs

wgraph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": [], "E": ["G"], "F": [], "G": []}
w = {("A", "B"): 1, ("A", "C"): 5, ("B", "D"): 4, ("B", "E"): 1, ("C", "F"): 3, ("C", "G"): 7, ("E", "G"): 1}
assert all(x >= 0 for x in w.values())     


def ucs(g, w, start, goal):
    pq = [(0, 0, start, [start])]; done = set(); count = 0     
    while pq:
        cost, _, node, path = heapq.heappop(pq)
        if node in done: continue
        done.add(node)
        if node != goal:
            for n in g[node]:
                if n not in done:
                    count += 1; heapq.heappush(pq, (cost + w[(node, n)], count, n, path + [n]))
        print("UCS", node, "cost", cost, path, "queue:", [(c, n) for c, _, n, _ in sorted(pq)])
        if node == goal: return path, cost
    return None, None


def cost_of(path):                         
    return sum(w[e] for e in zip(path, path[1:]))


if __name__ == "__main__":
    p, c = ucs(wgraph, w, "A", "G")
    print(f"UCS path {p}: hops={len(p) - 1}, UCS cost={c}, independent sum={cost_of(p)}")
    b = bfs("A", "G", wgraph)
    print(f"BFS path {b}: hops={len(b) - 1}, cost={cost_of(b)}")
    print("Start = goal :", ucs(wgraph, w, "A", "A"))
    print("Unreachable  :", ucs(wgraph, w, "F", "G"))
    cyc = {"A": ["B"], "B": ["A", "C"], "C": [], "Z": []}
    print("Cycle graph  :", ucs(cyc, {("A", "B"): 2, ("B", "A"): 2, ("B", "C"): 3}, "A", "Z"))