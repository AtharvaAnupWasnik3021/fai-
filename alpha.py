tree = [
    [[2, 3], [1, 7]],
    [[6, 5], [4, 9]]
]

def alpha_beta(node, alpha, beta, is_max):
    # Base case: if we reach an integer leaf, return its value
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

# Start at root (Layer 0 = Max, Layer 1 = Min, Layer 2 = Max, Layer 3 = Leaves)
optimal_value = alpha_beta(tree, float('-inf'), float('inf'), is_max=True)
print(f"Optimal Value: {optimal_value}")
