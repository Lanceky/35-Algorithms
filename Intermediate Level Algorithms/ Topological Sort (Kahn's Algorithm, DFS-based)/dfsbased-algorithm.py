def topological_sort_dfs(graph):
    visited = set()
    temp_mark = set()  # For cycle detection
    topo_order = []

    def dfs(node):
        if node in temp_mark:
            return False  # Cycle detected
        if node in visited:
            return True

        temp_mark.add(node)
        for neighbor in graph.get(node, []):
            if not dfs(neighbor):
                return False

        temp_mark.remove(node)
        visited.add(node)
        topo_order.append(node)
        return True

    for node in graph:
        if node not in visited:
            if not dfs(node):
                return None  # Cycle detected

    return topo_order[::-1]  # Reverse to get topological order