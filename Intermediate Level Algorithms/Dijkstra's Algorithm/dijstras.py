import heapq


def dijkstra(graph, start):
    # Initialize distances: start node=0, others=infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue: (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we've already found a better path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update if we found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Test
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'D': 3},
    'D': {}
}
print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 2, 'C': 3, 'D': 6}