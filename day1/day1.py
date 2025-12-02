def solve_safe_dial_part1(rotations_text):
    """
    Solve the safe dial puzzle.
    
    Args:
        rotations_text: String containing rotation instructions, one per line
        
    Returns:
        Number of times the dial points at 0 after any rotation
    """
    lines = rotations_text.strip().split('\n')
    
    position = 50  
    result = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'R':
            # Rotate left (toward lower numbers)
            position = (position + distance) % 100
        else:  # direction == 'R'
            # Rotate right (toward higher numbers)
            position = (position - distance) % 100
        
        # Check if we landed on 0
        if position == 0:
            result += 1
    
    return result

def solve_safe_dial_part2(rotations_text):
    """
    Solve the safe dial puzzle. pass through 0
    
    Args:
        rotations_text: String containing rotation instructions, one per line
        
    Returns:
        Number of times the dial points at 0 after any rotation
    """
    lines = rotations_text.strip().split('\n')
    
    position = 50  
    result = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'R':
            # Rotate right (adding to position)
            new_position = (position + distance) % 100
            # Count how many times we pass through 0
            times_through_zero = (position + distance) // 100
            result += times_through_zero
            position = new_position
        
        elif direction == 'L':
            # Rotate left (subtracting from position)
            new_position = (position - distance) % 100
            # Count how many times we pass through 0
            if position == 0:
                # Special case: starting at 0, we move away and might come back
                times_through_zero = distance // 100
            elif distance >= position:
                # We reach 0 after 'position' steps, then every 100 steps after
                times_through_zero = 1 + (distance - position) // 100
            else:
                # We don't reach 0
                times_through_zero = 0
            result += times_through_zero
            position = new_position
    return result
        


if __name__ == "__main__":
    with open('day1_input.txt', 'r') as f:
        input_text = f.read()
    
    result = solve_safe_dial_part1(input_text)
    print(f"The dial points at 0 {result} times")

    result = solve_safe_dial_part2(input_text)
    print(f"The dial points at 0 {result} times")