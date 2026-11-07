import heapq
 
graph = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)], "B": [("G", 5)], "C": [("G", 3)], "G": []}
h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}    
 
 
def astar(graph, h, start, goal, show=True):
    pq = [(h[start], 0, start, [start])]; best = {start: 0}; order = []; expanded = 0
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best[node]: continue                      
        order.append(node)
        if node == goal:                                 
            if show: print(f"  process {node}: g={g} h={h[node]} f={f} -> goal reached")
            return g, path, order, expanded
        expanded += 1                                    
        for nxt, w in graph.get(node, []):
            if g + w < best.get(nxt, float("inf")):
                best[nxt] = g + w
                heapq.heappush(pq, (g + w + h[nxt], g + w, nxt, path + [nxt]))
        if show:
            front = [(n, gg, h[n], ff) for ff, gg, n, _ in sorted(pq) if gg == best[n]]
            print(f"  process {node}: g={g} h={h[node]} f={f} | frontier (node,g,h,f): {front}")
    return None, None, order, expanded
 
 
def edge_sum(path):                                    
    return sum(dict(graph[a])[b] for a, b in zip(path, path[1:]))
 
 
def report(name, result):
    g, path, order, expanded = result
    print(f"{name}: path={path}, returned cost={g}, summed cost={edge_sum(path) if path else None}, "
          f"processed={order}, expanded={expanded}")
 
 
print("=== TASK 1: manual g/h/f check (supplied h) ===")
astar(graph, h, "S", "G")
 
print("\n=== HEURISTIC AUDIT ===")
zero = {n: 0 for n in graph}
true = {n: astar(graph, zero, n, "G", False)[0] for n in graph}     
for n in graph: print(f"  {n}: h={h[n]}, true remaining={true[n]}, admissible={h[n] <= true[n]}")
for u in graph:
    for v, w in graph[u]: print(f"  edge {u}->{v} (cost {w}): h({u}) <= {w} + h({v}) -> {h[u]} <= {w + h[v]}: {h[u] <= w + h[v]}")
 
print("\n=== TASK 2: A* vs UCS (h = 0), same graph, start S, goal G ===")
a = astar(graph, h, "S", "G", False); u = astar(graph, zero, "S", "G")
report("A*  ", a); report("UCS ", u)
print("\n=== TASK 3: overestimate, only h(C) changed ===")
h2 = dict(h); h2["C"] = 10
print(f"  h(C): {h['C']} -> {h2['C']}, true remaining cost of C = {true['C']}, admissible={h2['C'] <= true['C']}")
o = astar(graph, h2, "S", "G")
report("Original h  ", a); report("h(C)=10     ", o)
print(f"  Changed? path={a[1] != o[1]}, cost={a[0] != o[0]}, expansions={a[3] != o[3]}")
 
print("\n=== EDGE CASES ===")
print("  Start = goal (S to S):", astar(graph, h, "S", "S", False)[:2])
print("  Unreachable goal (G to S):", astar(graph, h, "G", "S", False)[:2])
 