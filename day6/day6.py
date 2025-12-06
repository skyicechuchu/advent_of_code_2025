import numpy as np


def parse_worksheet(text):
    """
    Parse the worksheet into individual problems using numpy.
    Problems are arranged vertically and separated by columns of spaces.
    """
    lines = text.strip('\n').split('\n')
    
    if not lines:
        return []
    
    # Pad all lines to the same length
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]
    
    # Convert to numpy array of characters
    grid = np.array([list(line) for line in lines])
    
    # Transpose to work with columns (each column is a vertical slice)
    grid_T = grid.T
    
    # Split by empty columns (all spaces)
    problems = []
    current_problem = []
    
    for col in grid_T:
        col_str = ''.join(col)
        if col_str.strip() == '':  # Empty column - separator
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col_str)
    
    # Don't forget the last problem
    if current_problem:
        problems.append(current_problem)
    
    return problems


def solve_problem(problem_columns):
    """
    Part 1: Solve a single problem given its columns.
    Each column contains numbers stacked vertically with an operator at the bottom.
    Numbers are in rows, read left-to-right.
    """
    if not problem_columns:
        return 0
    
    # Extract numbers and operator from the problem columns
    numbers = []
    operator = None
    
    # Join columns back into rows for this problem
    num_rows = len(problem_columns[0])
    rows = []
    for row_idx in range(num_rows):
        row = ''.join(col[row_idx] for col in problem_columns)
        rows.append(row.strip())
    
    # Last row is the operator, previous rows are numbers
    for row in rows[:-1]:
        if row:  # Skip empty rows
            numbers.append(int(row))
    
    operator = rows[-1].strip()
    
    # Calculate result
    if not numbers:
        return 0
    
    result = numbers[0]
    for num in numbers[1:]:
        if operator == '*':
            result *= num
        elif operator == '+':
            result += num
    
    return result


def solve_problem_part2(problem_columns):
    """
    Part 2: Solve reading right-to-left in columns (Cephalopod math).
    Each COLUMN represents one number (digits top-to-bottom).
    Process columns right-to-left.
    Operators include *, +, and % (modulo).
    """
    if not problem_columns:
        return 0
    
    numbers = []
    operator = None
    
    # The operator is in the last row (same across all columns)
    # Get it from any column that has it
    for col in problem_columns:
        op_char = col[-1].strip()
        if op_char and op_char in ['*', '+', '%']:
            operator = op_char
            break
    
    # Read columns RIGHT-TO-LEFT to get numbers
    for col_idx in range(len(problem_columns) - 1, -1, -1):
        col = problem_columns[col_idx]
        
        # Extract digits (all rows except last which is operator row)
        digits = []
        for row_idx in range(len(col) - 1):
            char = col[row_idx]
            if char.strip():  # Not a space
                digits.append(char)
        
        if digits:
            # Form number from digits (top to bottom = most to least significant)
            number = int(''.join(digits))
            numbers.append(number)
    
    # Calculate result
    if not numbers:
        return 0
    
    result = numbers[0]
    for num in numbers[1:]:
        if operator == '*':
            result *= num
        elif operator == '+':
            result += num
        elif operator == '%':
            result %= num
    
    return result


def solve_worksheet(text):
    """
    Part 1: Solve all problems on the worksheet and return the grand total.
    """
    problems = parse_worksheet(text)
    total = 0
    
    for problem in problems:
        answer = solve_problem(problem)
        total += answer
    
    return total


def solve_worksheet_part2(text):
    """
    Part 2: Solve all problems reading right-to-left (Cephalopod math).
    """
    problems = parse_worksheet(text)
    total = 0
    
    for problem in problems:
        answer = solve_problem_part2(problem)
        total += answer
    
    return total


if __name__ == "__main__":
    # Test with example
    example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    
    print("Testing example:")
    print(f"Part 1: {solve_worksheet(example)} (expected 4277556)")
    print(f"Part 2: {solve_worksheet_part2(example)} (expected 3263827)")
    print()
    
    # Run on actual input
    with open('day6_input.txt', 'r') as f:
        input_text = f.read()
    
    print(f"Part 1: {solve_worksheet(input_text)}")
    print(f"Part 2: {solve_worksheet_part2(input_text)}")


