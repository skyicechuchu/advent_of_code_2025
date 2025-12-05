def parse_input(text):
    """
    Parse input into ranges and ingredient IDs.
    Returns (ranges, ids) where ranges is list of (start, end) tuples.
    """
    # Split by double newline (blank line)
    sections = text.split('\n\n')
    
    if len(sections) < 2:
        raise ValueError("Input must have ranges, blank line, then IDs")
    
    # Parse ranges
    ranges = []
    for line in sections[0].strip().split('\n'):
        if line.strip() and '-' in line:
            start, end = map(int, line.strip().split('-'))
            ranges.append((start, end))
    
    # Parse available ingredient IDs
    ids = []
    for line in sections[1].strip().split('\n'):
        if line.strip():
            ids.append(int(line.strip()))
    
    return ranges, ids


def is_fresh(ingredient_id, ranges):
    """
    Check if an ingredient ID falls within any of the fresh ranges.
    """
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def count_fresh_ingredients(ranges, ids):
    """
    Count how many ingredient IDs are fresh.
    """
    count = 0
    for ingredient_id in ids:
        if is_fresh(ingredient_id, ranges):
            count += 1
    return count


def merge_ranges(ranges):
    """
    Merge overlapping ranges to get non-overlapping intervals.
    Returns list of merged (start, end) tuples.
    """
    if not ranges:
        return []
    
    # Sort ranges by start position
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        # Check if current range overlaps with last merged range
        if start <= last_end + 1:
            # Merge by extending the end if necessary
            merged[-1] = (last_start, max(last_end, end))
        else:
            # No overlap, add as new range
            merged.append((start, end))
    
    return merged


def count_all_fresh_ids(ranges):
    """
    Part 2: Count total number of unique ingredient IDs covered by any range.
    """
    merged = merge_ranges(ranges)
    
    total = 0
    for start, end in merged:
        # Range is inclusive, so count is (end - start + 1)
        total += (end - start + 1)
    
    return total


def solve_part1(input_text):
    """
    Parse input and count fresh ingredients from available IDs.
    """
    ranges, ids = parse_input(input_text)
    return count_fresh_ingredients(ranges, ids)


def solve_part2(input_text):
    """
    Parse input and count all unique IDs covered by fresh ranges.
    """
    ranges, _ = parse_input(input_text)
    return count_all_fresh_ids(ranges)


if __name__ == "__main__":
    
    with open('day5_input.txt', 'r') as f:
        input_text = f.read()
    
    print(f"Part 1: {solve_part1(input_text)}")
    print(f"Part 2: {solve_part2(input_text)}")

