from collections import deque


def bfs_shortest_path(graph, start, target):
    """BFS to find shortest path between two nodes"""
    queue = deque([(start, [start])])  # (node, path)
    visited = set(start)

    while queue:
        node, path = queue.popleft()
        if node == target:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []  # No path exists


# Test BFS
print("\nShortest path from Alice to Frank:")
print(bfs_shortest_path(graph, 'Alice', 'Frank'))
# Output: ['Alice', 'Charlie', 'Frank']