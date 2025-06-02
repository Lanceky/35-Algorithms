Topological Sort Algorithms

Topological sort is an ordering of vertices in a directed acyclic graph (DAG) where for every directed edge (u, v), vertex u comes before v in the ordering. Here are two common implementations:
1. Kahn's Algorithm (BFS-based)
python

from collections import deque

def topological_sort_kahn(graph):
    # Calculate in-degree for each node
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Initialize queue with nodes having 0 in-degree
    queue = deque([node for node in graph if in_degree[node] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        # Reduce in-degree for neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycles
    if len(topo_order) != len(graph):
        return None  # Graph has at least one cycle
    
    return topo_order

2. DFS-based Algorithm
python

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
                return None  # Graph has at least one cycle
    
    return topo_order[::-1]  # Reverse to get topological order

Usage Example
python

# Example DAG
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

print("Kahn's algorithm result:", topological_sort_kahn(graph))
print("DFS-based algorithm result:", topological_sort_dfs(graph))

Key Differences

    Kahn's Algorithm:

        Uses BFS approach

        Starts with nodes having no incoming edges

        Explicitly calculates in-degrees

        Naturally detects cycles

    DFS-based Algorithm:

        Uses DFS approach

        Processes nodes until reaching "sink" nodes (no outgoing edges)

        Uses temporary marks for cycle detection

        Needs to reverse the result at the end

Both algorithms have O(V+E) time complexity for a graph with V vertices and E edges.
it's the explanation ( comprehensive explanation first what it is where and when it's used , how it's used examples of where they can be used in practical life) , real world analogies then the problem statement followed by it's solution in python
Comprehensive Guide to Topological Sort
1. What is Topological Sort?

Topological sort is an algorithm that orders the nodes of a Directed Acyclic Graph (DAG) in such a way that for every directed edge (u → v), node u appears before v in the ordering.

    Key Property: It only works on DAGs (no cycles allowed).

    Non-Uniqueness: A DAG can have multiple valid topological orderings.

2. Where and When is Topological Sort Used?

Topological sorting is used in problems where tasks have dependencies, meaning some tasks must be completed before others can begin.
Real-World Applications

    Task Scheduling

        Example: In a build system (like make), compiling files in the correct order where some files depend on others.

        Example: University course prerequisites (you must take Calculus before Machine Learning).

    Package Management

        Example: npm or pip installing dependencies in the correct order.

    Event Processing

        Example: In a workflow system, certain steps must happen before others.

    Data Processing Pipelines

        Example: ETL (Extract, Transform, Load) jobs where some transformations depend on others.

    Deadlock Detection

        If a topological sort is impossible, the graph has a cycle (cyclic dependencies).

Real-World Analogy: Getting Dressed

Imagine you need to put on clothes in a certain order:

    You must wear underwear before pants.

    You must wear a shirt before a jacket.

    You must wear socks before shoes.

A valid topological order could be:
[underwear, socks, pants, shoes, shirt, jacket]
(But other valid orders exist, like wearing the shirt before pants.)

If you try to wear shoes before socks, it violates dependencies → invalid order.
3. Problem Statement

Given a directed acyclic graph (DAG), return a topological ordering of its vertices. If the graph contains a cycle, return None (since topological sort is only possible for DAGs).
Input Representation

A graph is given as an adjacency list:
python

graph = {
    'A': ['B', 'C'],  # A must come before B and C
    'B': ['D'],        # B must come before D
    'C': ['D'],        # C must come before D
    'D': ['E'],        # D must come before E
    'E': []            # E has no dependencies
}

Expected Output

A valid topological order, such as:
['A', 'B', 'C', 'D', 'E']
or
['A', 'C', 'B', 'D', 'E']

If the graph has a cycle (e.g., A → B → C → A), return None.
4. Solutions in Python
Solution 1: Kahn's Algorithm (BFS-Based)

    Uses in-degree counting (number of incoming edges).

    Starts with nodes that have no dependencies (in-degree = 0).

    Removes dependencies as it processes nodes.