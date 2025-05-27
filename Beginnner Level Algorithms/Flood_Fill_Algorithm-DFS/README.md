Flood Fill Algorithm: A Deep Dive with DFS for Grid Problems
🌊 Introduction to Flood Fill

Flood Fill is a classic algorithm used to color connected regions in grids (2D matrices). It's fundamental in:

    Image editing tools (like Photoshop's "paint bucket")

    Game development (terrain generation, puzzle games)

    Computer vision (object detection)

🎯 Problem Statement

Given:

    A 2D grid (matrix) representing an image/map

    A starting pixel (row, col)

    A target color

    An original color

Goal: Fill all connected pixels of the original color with the target color.

Example:
python

Input:
[
 [1, 1, 1],
 [1, 1, 0],
 [1, 0, 1]
]
start = (1, 1), target = 2, original = 1

Output:
[
 [2, 2, 2],
 [2, 2, 0],
 [2, 0, 1]
]

🧠 How It Works: DFS Approach

Depth-First Search (DFS) is ideal for Flood Fill because it:

    Starts at the given cell

    Recursively visits all 4-directionally/8-directionally connected cells

    Changes their color if they match the original color

Key Steps:

    Base Cases:

        If out of bounds → return

        If cell color ≠ original color → return

        If cell already = target color → return (avoid cycles)

    Recursive Step:

        Change current cell to target color

        Call DFS on neighbors (up, down, left, right)

🔍 Interactive Example

Try this grid:
python

grid = [
    [1, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

    Start at (0, 0) with target = 2

    Watch how DFS fills connected 1s!

⚡ Optimizations & Variations

    BFS Approach:

        Uses a queue (better for large grids to avoid stack overflow)

    8-Directional Flood Fill:

        Include diagonals by adding 4 more directions

    Early Termination:

        Stop if target = original color

💡 Real-World Applications

    Image Editing:

        "Paint bucket" tool in Photoshop/GIMP

    Minesweeper:

        Reveal connected empty cells

    Terrain Generation:

        Identify contiguous landmasses in games

📚 Practice Problems

    LeetCode #733 - Flood Fill

    Number of Islands (DFS variant)

    Coloring a Border

Key Takeaways

✅ Use DFS/BFS to traverse connected cells
✅ Handle edge cases (out-of-bounds, same color)
✅ Optimize with BFS for large grids
✅ Applies to image processing, games, and more

How Path Connectivity Works in Flood Fill (DFS/BFS for Grids)

Flood Fill algorithms (using DFS or BFS) traverse a grid by moving between connected neighbors of the same original value. Whether cells connect depends on two key factors:
1. Connection Rules

A cell (row, col) is connected to its neighbor if:

    They share an edge (4-directional) or edge + corners (8-directional).

    Both have the same original value (e.g., 1 in your example).

    The neighbor is within grid bounds.

4-Directional vs. 8-Directional
Movement	Directions	When to Use
4-Way	Up, Down, Left, Right	Standard Flood Fill (e.g., paint bucket)
8-Way	Adds Diagonals (NW, NE, SW, SE)	Image processing (e.g., anti-aliasing)


Why the Example above Has an Unfilled 1
Given Grid:
python

[
 [1, 1, 1],  # Row 0
 [1, 1, 0],  # Row 1
 [1, 0, 1]   # Row 2
]
# Start at (1, 1), target = 2, original = 1

Step-by-Step Path Analysis (4-Way DFS)

    Start at (1, 1) (value = 1) → Changes to 2.

    Check 4 Neighbors:

        Up: (0, 1) → 1 → Connected! Fills to 2.

            Now process (0, 1)'s neighbors:

                (0, 0), (0, 2) → All 1s → Fill to 2.

        Down: (2, 1) → 0 → Blocked! (Not original 1).

        Left: (1, 0) → 1 → Connected! Fills to 2.

            Processes (1, 0)'s neighbors:

                (0, 0) already filled, (2, 0) → 1 → Fills to 2.

        Right: (1, 2) → 0 → Blocked!

    Result:

        The 1 at (2, 2) is isolated because:

            Path 1: (1,1) → (2,1)=0 → Blocked.

            Path 2: (1,1) → (1,2)=0 → Blocked.



Final Grid:
[
 [2, 2, 2],  # All connected 1s filled
 [2, 2, 0],  # (1,2)=0 (unchanged)
 [2, 0, 1]   # (2,2)=1 (no path to start)
]

3. When Does a Cell Not Connect?

A cell won’t connect if:

    Blocked by a different value:

        In your example, 0s block access to (2, 2).

    Out of grid bounds:

        Example: (-1, 1) or (3, 1) are invalid.

    Already filled with the target color:

        Prevents infinite loops (e.g., (1,1) changes to 2 and won’t be reprocessed).

4. Visualizing Connectivity
Connected Path (Green) vs. Blocked Path (Red)

Initial Grid:       Connected Path:       Blocked Paths:
[1, 1, 1]          [2, 2, 2]            [ ,  ,  ]
[1, 1, 0]    →     [2, 2, 0]            [ ,  , X]  # (1,2)=0 blocks right
[1, 0, 1]          [2, 0, 1]            [ , X,  ]  # (2,1)=0 blocks down

    ✅ Connected: All 1s linked to (1,1) via 1s.

    ❌ Blocked: (2,2) is separated by 0s.

5. Key Takeaways

    Flood Fill propagates through same-value neighbors (original color).

    Barriers (0s in your case) block connectivity.

    Indexing starts at 0, and movement follows grid edges (4-way) or edges+corners (8-way).

    To fill all 1s (even disconnected ones), you’d need to:

        Iterate the entire grid.

        Run Flood Fill on every unprocessed 1 (changes the problem definition).

