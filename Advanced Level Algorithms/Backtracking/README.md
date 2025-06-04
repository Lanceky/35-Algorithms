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

           **Explanation of the backtracking template**
 def backtrack(candidate):

    This is a recursive function.

    candidate represents the current state or partial solution being built.

🔸 if is_complete(candidate):

    This checks if the current candidate is a complete solution.

    This could mean:

        A full permutation is built.

        All queens are placed (in N-Queens).

        A valid Sudoku board is filled.

🔸 output(candidate)

    If the solution is complete and valid, we record or print it.

    Often this is where we add the solution to a results list or count it.

🔸 for next_candidate in generate_candidates(candidate):

    We generate all possible next steps (choices/extensions) from the current state.

    For example:

        Add the next digit.

        Try placing a queen in the next row.

        Pick the next letter in a word puzzle.

🔸 if is_valid(next_candidate):

    We check if this partial solution still satisfies the problem’s constraints.

    This pruning step prevents wasted work on invalid branches.

    Examples:

        No duplicate numbers in row (Sudoku).

        No queens attacking each other (N-Queens).

🔸 make_move(next_candidate)

    This modifies the state by applying the current choice.

    Sometimes it modifies global state (like a board), other times it's just part of the recursion input.

🔸 backtrack(next_candidate)

    Recursive call to continue building from this new partial solution.

🔸 undo_move(next_candidate)

    This undoes the previous change (backtracks) so we can try a different path.

    Essential to avoid side effects between recursive calls.

📌 Why This Template Works

    It's systematic: explores all paths in a structured, recursive way.

    It's efficient: thanks to pruning (is_valid) and undoing steps (undo_move).

    It's reusable: this exact structure can solve a wide range of problems with different definitions for is_complete, generate_candidates, is_valid, etc.

✅ Summary

This backtracking template captures the essence of solving a problem by:

    Exploring all options, pruning bad ones early, and cleaning up after each decision.