def flood_fill(grid, row, col, target, original=None):
    if original is None:
        original = grid[row][col]

    # Base cases
    if (row < 0 or row >= len(grid) or (col < 0 or col >= len(grid[0])):
        return
    if grid[row][col] != original or grid[row][col] == target:
        return

    # Fill the cell
    grid[row][col] = target

    # 4-directional DFS
    flood_fill(grid, row + 1, col, target, original)  # Down
    flood_fill(grid, row - 1, col, target, original)  # Up
    flood_fill(grid, row, col + 1, target, original)  # Right
    flood_fill(grid, row, col - 1, target, original)  # Left

    return grid