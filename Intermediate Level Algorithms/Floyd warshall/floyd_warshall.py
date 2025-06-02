def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]  # Copy input graph

    for k in range(n):  # Intermediate node
        for i in range(n):  # Source node
            for j in range(n):  # Destination node
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Optional: Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            print("Warning: Negative cycle detected")

    return dist


# Test
INF = float('inf')
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
print("Shortest distances:")
for row in floyd_warshall(graph):
    print(row)