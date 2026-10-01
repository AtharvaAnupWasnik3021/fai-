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



def hill_climbing(curr, neighbors, cost):
    while True:
        # Single-line: find the neighbor with the absolute lowest cost
        best = min(neighbors(curr), key=cost, default=curr)
        
        # If no neighbor improves the cost, we have reached the peak (local optimum)
        if cost(best) >= cost(curr): return curr
        curr = best

# --- Test Setup ---
# A dummy function returning adjacent integers as neighbors
get_neighbors = lambda x: [x - 1, x + 1]

# A cost function mimicking a valley (global minimum is at x = 4)
cost_func = lambda x: (x - 4) ** 2 

# Run starting from initial state x = 10
result = hill_climbing(10, get_neighbors, cost_func)
print(f"Optimal State Found: {result} (Cost: {cost_func(result)})")
