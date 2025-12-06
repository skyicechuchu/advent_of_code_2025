def find_invalid_ids_part1(id):
    """
    Part 1: Check if ID has mirror property (first half equals second half).
    Returns True if invalid.
    """
    id_name = str(id)
    length = len(id_name)
    if length % 2 != 0:
        return False
    mid = length // 2 
    left = 0

    while left < mid and mid < length:
        if id_name[left] != id_name[mid]:
            return False
        left += 1
        mid += 1
    return True

def find_invalid_ids_part2(id):
    """
    Part 2: Check if ID is made of a repeating pattern (at least twice).
    Examples: 11 (1*2), 123123 (123*2), 12341234 (1234*2), 565656 (56*3)
    Returns True if invalid.
    """
    id_str = str(id)
    length = len(id_str)
    
    # Try all possible pattern lengths from 1 to length//2
    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0:
            # Check if the pattern repeats
            pattern = id_str[:pattern_length]
            repetitions = length // pattern_length
            if repetitions >= 2 and pattern * repetitions == id_str:
                return True
    
    return False

def parse_ranges(text):
    """
    Parse ranges from text like '11-22,95-115,998-1012'
    Returns a list of all numbers in the ranges.
    Format: always two numbers separated by one dash (e.g., '11-22')
    """
    all_numbers = []
    
    # Split by newlines and commas to handle multi-line input
    parts = text.replace('\n', ',').split(',')
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
        
        # Split on dash - always two numbers
        start, end = part.split('-')
        start = int(start)
        end = int(end)
        all_numbers.extend(range(start, end + 1))
    
    return all_numbers

def process_ids(ids):
    """
    Part 1: Process a list of IDs and sum invalid ones (mirror property).
    """
    result = 0
    
    for id_num in ids:
        if find_invalid_ids_part1(id_num):
            result += id_num
    
    return result

def process_ids_part2(ids):
    """
    Part 2: Process a list of IDs and sum invalid ones (repeating pattern).
    """
    result = 0
    
    for id_num in ids:
        if find_invalid_ids_part2(id_num):
            result += id_num
    
    return result

# Standard aliases for the runner
def solve_part1(input_text):
    all_ids = parse_ranges(input_text)
    return process_ids(all_ids)

def solve_part2(input_text):
    all_ids = parse_ranges(input_text)
    return process_ids_part2(all_ids)


if __name__ == "__main__":
    # Read input from file
    with open('day2_input.txt', 'r') as f:
        input_text = f.read()
    
    # Part 1
    result_part1 = solve_part1(input_text)
    print(f"Part 1: {result_part1}")
    
    # Part 2
    result_part2 = solve_part2(input_text)
    print(f"Part 2: {result_part2}")
