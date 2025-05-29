DFS and BFS: Comprehensive Guide to Graph Traversals
1. What Are DFS and BFS?

DFS (Depth-First Search) and BFS (Breadth-First Search) are fundamental graph traversal algorithms that explore nodes in different orders:
DFS (Depth-First Search)

    Approach: Explores as far as possible along each branch before backtracking ("go deep first")

    Data Structure: Uses a stack (implicit in recursion, or explicit)

    Best For:

        Finding all possible solutions (e.g., maze paths)

        Topological sorting

        Detecting cycles in graphs

BFS (Breadth-First Search)

    Approach: Explores all neighbors at the present depth before moving deeper ("level by level")

    Data Structure: Uses a queue

    Best For:

        Shortest path in unweighted graphs

        Web crawling

        Social network connections

2. Real-World Analogies
DFS Examples

    Maze Solving

        Like following one path in a maze until you hit a dead end, then backtracking

    File System Navigation

        Opening folders and subfolders recursively until you find a file

    Game Decision Trees

        Exploring all possible moves in chess before choosing the best one

BFS Examples

    Social Networks

        Finding the shortest connection path between you and another person (1st-degree → 2nd-degree → etc.)

    Emergency Broadcasts

        Alerting all immediate neighbors first, then their neighbors

    GPS Navigation

        Finding the route with fewest turns between two points

3. Problem Statement

Given an undirected graph representing social connections:
python

graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Charlie': ['Alice', 'Frank'],
    'David': ['Bob'],
    'Eve': ['Bob', 'Frank'],
    'Frank': ['Charlie', 'Eve']
}

Tasks:

    DFS: Find all people reachable from 'Alice' (depth-first order)

    BFS: Find the shortest connection path from 'Alice' to 'Frank'