def ao_star(n, g, h, sol):
    if n not in g or not g[n]: return h[n]
    costs = [(sum(h[c] + 1 for c in b), b) for b in g[n]]
    h[n], sol[n] = min(costs, key=lambda x: x[0])
    [ao_star(c, g, h, sol) for c in sol[n]]
    return h[n]

graph = {'A': [['B'], ['C', 'D']], 'B': [['E']], 'C': [['G']], 'D': []}
heuristic = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 0, 'G': 0}
solution = {}

print("Min Cost:", ao_star('A', graph, heuristic, solution))
print("Solution Tree:", {k: v for k, v in solution.items() if v})









def a_star(start, target, graph, h):
    open_set = {start}
    g = {start: 0}
    f = {start: h[start]}
    parent = {}

    while open_set:
        curr = min(open_set, key=lambda x: f[x])
        if curr == target:
            path = []
            while curr in parent:
                path.append(curr)
                curr = parent[curr]
            return [start] + path[::-1], g[target]

        open_set.remove(curr)
        for neighbor, cost in graph.get(curr, {}).items():
            temp_g = g[curr] + cost
            if temp_g < g.get(neighbor, float('inf')):
                parent[neighbor] = curr
                g[neighbor] = temp_g
                f[neighbor] = temp_g + h.get(neighbor, 0)
                open_set.add(neighbor)
    return None, float('inf')

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
heuristic = {'A': 3, 'B': 6, 'C': 1, 'D': 0}

path, cost = a_star('A', 'D', graph, heuristic)
print("Path:", path)
print("Cost:", cost)
