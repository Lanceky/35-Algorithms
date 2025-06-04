                         Backtracking Algorithms

Backtracking is a powerful algorithmic paradigm for solving constraint satisfaction problems by
incrementally building candidates and abandoning (backtracking) partial soluions that fail
constraints.

1. What is Backtracking?

Backtracking is a refined brute-force approach that:

    Systematically explores possible solutions

    Abandons partial candidates as soon as they violate constraints ("pruning")

    Recursively builds solutions one piece at a time

Key Property: It uses depth-first search (DFS) with state rollback.
2. When to Use Backtracking?

Ideal for problems where:

    You need all possible solutions (not just one)

    The solution can be built incrementally

    Decisions have constraints that can be checked early

Real-World Applications

    Puzzle Solving

        Sudoku, Crosswords, N-Queens

    Combinatorial Problems

        Permutations, Subsets, Combinations

    Scheduling & Resource Allocation

        Timetable generation with constraints

    Pathfinding & Maze Solving

        Finding all possible routes with obstacles

Analogy: Maze Exploration

Imagine navigating a maze:

    You try a path.

    If you hit a dead end, you backtrack to the last decision point.

    Try alternative paths until you find the exit (or all exits).