Union-Find (Disjoint Set Union - DSU): The Complete Guide
1. What is Union-Find?

Union-Find is a data structure that tracks elements divided into disjoint (non-overlapping) sets. It supports two key operations:

    Find: Determine which set an element belongs to

    Union: Merge two sets together

Key Features

    Amortized near-constant time per operation (with optimizations)

    Essential for connectivity problems

    Memory efficient (typically O(n) space)

2. Core Operations
Find Operation
python

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # Path compression
        x = parent[x]
    return x

Purpose: Locates the root representative of an element's set.
Union Operation
python

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root: return  # Already connected
    
    if rank[x_root] < rank[y_root]:  # Union by rank
        parent[x_root] = y_root
    else:
        parent[y_root] = x_root
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1

Purpose: Merges two sets while maintaining balanced trees.
3. Real-World Analogies
Social Networks

    Find: "Are Alice and Bob in the same friend group?"

    Union: "Merge these two friend circles"

Circuit Design

    Find: "Are these two components electrically connected?"

    Union: "Connect these two circuit nodes"

4. Problem Statement: Friend Circles

Given an N×N adjacency matrix where:

    matrix[i][j] = 1 if person i and j are friends

    matrix[i][j] = 0 otherwise

Find: The number of distinct friend circles.

Example:
python

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]

Output: 2  # First two people are friends, third is alone