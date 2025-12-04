def count_accessible_rolls(grid):
    """
    Count rolls of paper (@) that have fewer than 4 adjacent rolls.
    Time: O(rows * cols), Space: O(1)
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # 8 directions: all adjacent positions
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        adjacent += 1
                
                if adjacent < 4:
                    count += 1
    
    return count


def find_accessible_positions(grid):
    """
    Find all positions with rolls that have fewer than 4 adjacent rolls.
    Returns list of (row, col) positions.
    """
    rows = len(grid)
    cols = len(grid[0])
    accessible = []
    
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        adjacent += 1
                
                if adjacent < 4:
                    accessible.append((r, c))
    
    return accessible


def remove_rolls_iteratively(grid):
    """
    Part 2: Keep removing accessible rolls until no more can be removed.
    Returns total number of rolls removed.
    """
    # Work with a copy so we don't modify original
    grid = [row[:] for row in grid]
    total_removed = 0
    
    while True:
        # Find all accessible rolls
        accessible = find_accessible_positions(grid)
        
        if not accessible:
            break
        
        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = '.'
        
        total_removed += len(accessible)
    
    return total_removed


def solve_part1(input_text):
    """Parse input and count accessible rolls."""
    lines = [list(line.strip()) for line in input_text.strip().split('\n') if line.strip()]
    return count_accessible_rolls(lines)


def solve_part2(input_text):
    """Parse input and count total removable rolls."""
    lines = [list(line.strip()) for line in input_text.strip().split('\n') if line.strip()]
    return remove_rolls_iteratively(lines)


if __name__ == "__main__":
    # Test with example
    example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    
    print("Testing example:")
    print(f"Part 1: {solve_part1(example)} (expected 13)")
    print(f"Part 2: {solve_part2(example)} (expected 43)")
    print()
    
    # Run on actual input
    with open('day4_input.txt', 'r') as f:
        input_text = f.read()
    
    print(f"Part 1: {solve_part1(input_text)}")
    print(f"Part 2: {solve_part2(input_text)}")

