def dfs(graph, node, visited=None):
    """Depth-First Search (recursive implementation)"""
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')  # Process node (e.g., print)

    # Recur for all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


# Test DFS
print("DFS traversal from Alice:")
dfs(graph, 'Alice')
# Output: Alice Bob David Eve Frank Charlie