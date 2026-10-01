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



def hill_climbing(curr, neighbors_func, cost_func):
    while True:
        neighbors = neighbors_func(curr)
        if not neighbors: return curr
        best_neighbor = min(neighbors, key=cost_func)
        if cost_func(best_neighbor) >= cost_func(curr): return curr
        curr = best_neighbor
initial_state = (70, 20, 10)

def q3_neighbors(state):

    mapping = {
        (70, 20, 10): [(60, 30, 10), (80, 10, 10), (70, 10, 20)]
    }
    return mapping.get(state, [])

def q3_latency(state):
    scores = {
        (70, 20, 10): 85,
        (60, 30, 10): 62,
        (80, 10, 10): 98,
        (70, 10, 20): 55
    }
    return scores.get(state, float('inf'))

best_config = hill_climbing(initial_state, q3_neighbors, q3_latency)
print("\n--- Q3: Hill Climbing Result ---")
print(f"Optimal Configuration (S1%, S2%, S3%): {best_config}")
print(f"Lowest Achieved Latency: {q3_latency(best_config)} ms")
