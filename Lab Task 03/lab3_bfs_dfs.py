
from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["G"], "F": [], "G": []}


def bfs(start, goal, g=graph):
    q = deque([(start, [start])]); seen = {start}
    while q:
        node, path = q.popleft()
        if node != goal:
            for n in g[node]:
                if n not in seen:
                    seen.add(n); q.append((n, path + [n]))
        print("BFS", node, path, "queue:", [n for n, _ in q])
        if node == goal: return path


def dfs(start, goal, g=graph):
    stack = [(start, [start])]; seen = set()
    while stack:
        node, path = stack.pop()
        if node in seen: continue          
        seen.add(node)
        if node != goal:
            for n in reversed(g[node]): stack.append((n, path + [n]))   
        print("DFS", node, path, "stack:", [n for n, _ in stack])
        if node == goal: return path


if __name__ == "__main__":
    print("Final path:", bfs("A", "G"))
    print("Final path:", dfs("A", "G"))
    print("Start = goal:", bfs("A", "A"), dfs("A", "A"))
    print("Unreachable (C to G):", bfs("C", "G"), dfs("C", "G"))
    cyc = {"A": ["B"], "B": ["A", "C"], "C": [], "Z": []}      
    print("Cycle graph (A to Z):", bfs("A", "Z", cyc), dfs("A", "Z", cyc))