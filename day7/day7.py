"""
Day 7: Tachyon Manifold Beam Splitter

Part 1: Count beam splits in classical physics simulation
Part 2: Count quantum timelines (many-worlds interpretation)

Part 2 has TWO implementations:
1. count_quantum_timelines_dfs() - Top-down with @lru_cache memoization
2. count_quantum_timelines_dp() - Bottom-up dynamic programming

Both are O(rows × cols) time and space, produce identical results.
"""

def parse_input(text):
    """Parse the tachyon manifold grid."""
    return [list(line) for line in text.strip().split('\n')]


def find_start(grid):
    """Find the starting position marked with S."""
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'S':
                return (r, c)



def simulate_beams(grid):
    """
    Simulate tachyon beams through the manifold.
    Returns the total number of beam splits.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    start_pos = find_start(grid)

    
    # Track active beams: list of (row, col) positions
    # All beams move downward
    beams = [start_pos]
    split_count = 0
    
    # To avoid infinite loops, track processed beams at each position
    processed = set()
    
    while beams:
        new_beams = []
        
        for row, col in beams:
            # Skip if already processed
            if (row, col) in processed:
                continue
            processed.add((row, col))
            
            # Move beam downward
            next_row = row + 1
            
            # Check if beam exits the manifold
            if next_row >= rows:
                continue
            
            # Check what's at the next position
            next_cell = grid[next_row][col]
            
            if next_cell == '.':
                # Empty space, beam continues
                new_beams.append((next_row, col))
            elif next_cell == '^':
                # Splitter! Beam stops, create two new beams
                split_count += 1
                
                # New beam to the left
                if col - 1 >= 0:
                    new_beams.append((next_row, col - 1))
                
                # New beam to the right
                if col + 1 < cols:
                    new_beams.append((next_row, col + 1))
        
        beams = new_beams
    
    return split_count


def count_quantum_timelines_dfs(grid):
    """
    Part 2 (Approach 1): Count distinct timelines using memoized DFS.
    Top-down recursive approach with @lru_cache.
    """
    from functools import lru_cache
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    start_pos = find_start(grid)
    
    @lru_cache(maxsize=None)
    def dfs(r, c):
        """
        Return the number of timelines starting from position (r, c).
        The particle always moves downward.
        """
        # If we're on the last row, next move goes out of bounds
        if r == rows - 1:
            return 1
        
        below_r = r + 1
        below_c = c
        cell = grid[below_r][below_c]
        
        # Empty space or S: continue straight down
        if cell == '.' or cell == 'S':
            return dfs(below_r, below_c)
        
        # Splitter: particle takes both paths
        if cell == '^':
            total = 0
            
            # Left branch
            left_c = below_c - 1
            if left_c < 0:
                # Goes out of bounds → 1 timeline completes
                total += 1
            else:
                total += dfs(below_r, left_c)
            
            # Right branch
            right_c = below_c + 1
            if right_c >= cols:
                # Goes out of bounds → 1 timeline completes
                total += 1
            else:
                total += dfs(below_r, right_c)
            
            return total
        
        return 1
    
    return dfs(start_pos[0], start_pos[1])


def count_quantum_timelines_dp(grid):
    """
    Part 2 (Approach 2): Count distinct timelines using Dynamic Programming.
    Bottom-up iterative approach that processes row by row.
    
    ways[r][c] = number of quantum particles at position (r, c) after processing row r.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find starting position S
    start_pos = find_start(grid)
    sr, sc = start_pos
    
    # DP table: ways[r][c] = how many quantum particles are at (r, c)
    ways = [[0] * cols for _ in range(rows)]
    ways[sr][sc] = 1
    
    total_timelines = 0
    
    # Process row by row, from S downward
    for r in range(sr, rows):
        for c in range(cols):
            w = ways[r][c]
            if w == 0:
                continue
            
            # Particle at (r, c) tries to move down
            if r == rows - 1:
                # Next move would exit below the grid
                total_timelines += w
                continue
            
            nr = r + 1
            cell = grid[nr][c]
            
            if cell == '.' or cell == 'S':
                # Continue downward in same column
                ways[nr][c] += w
            elif cell == '^':
                # Splitter: branch to left and right
                # Left branch
                if c - 1 < 0:
                    # Goes out of manifold → completes timelines
                    total_timelines += w
                else:
                    ways[nr][c - 1] += w
                
                # Right branch
                if c + 1 >= cols:
                    total_timelines += w
                else:
                    ways[nr][c + 1] += w
    
    return total_timelines


def solve_part1(input_text):
    """Count total number of beam splits."""
    grid = parse_input(input_text)
    return simulate_beams(grid)


def solve_part2(input_text):
    """
    Count total number of quantum timelines.
    Uses DP approach (bottom-up). 
    Alternative: count_quantum_timelines_dfs (top-down with memoization).
    """
    grid = parse_input(input_text)
    return count_quantum_timelines_dp(grid)


if __name__ == "__main__":

    with open('day7_input.txt', 'r') as f:
        input_text = f.read()
    
    print(f"Part 1: {solve_part1(input_text)}")
    print(f"Part 2: {solve_part2(input_text)}")

