tree = [
    [[2, 3], [1, 7]],
    [[6, 5], [4, 9]]
]

def alpha_beta(node, alpha, beta, is_max):

    if isinstance(node, int):
        return node
    
    val = float('-inf') if is_max else float('inf')
    
    for child in node:
        res = alpha_beta(child, alpha, beta, not is_max)
        if is_max:
            val = max(val, res)
            alpha = max(alpha, val)
        else:
            val = min(val, res)
            beta = min(beta, val)
            
        if beta <= alpha:
            break  # Prune branch
            
    return val


optimal_value = alpha_beta(tree, float('-inf'), float('inf'), is_max=True)
print(f"Optimal Value: {optimal_value}")



def ao_star(n, g, h, sol):
    if n not in g or not g[n]: return h[n]
    

    costs = [(sum(h[c] + 1 for c in b), b) for b in g[n]]
    h[n], sol[n] = min(costs, key=lambda x: x[0])
    

    [ao_star(c, g, h, sol) for c in sol[n]]
    return h[n]

# --- Graph Setup & Test ---
# AND branches are grouped in sublists
graph = {'A': [['B'], ['C', 'D']], 'B': [['E']], 'C': [['G']], 'D': []}
heuristic = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 0, 'G': 0}
solution = {}

print("Min Cost:", ao_star('A', graph, heuristic, solution))
print("Solution Tree:", {k: v for k, v in solution.items() if v})
