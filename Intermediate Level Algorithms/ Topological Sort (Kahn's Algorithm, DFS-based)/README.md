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

Solution 2: DFS-Based Algorithm


    Uses post-order traversal (nodes are added after their dependencies).

    Detects cycles using temporary marks.