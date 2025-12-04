def find_max_joltage(bank):
    """
    Find the maximum 2-digit joltage by selecting exactly 2 batteries.
    
    We want to maximize 10*digit[i] + digit[j] where i < j.
    Iterate backwards, tracking the maximum digit seen so far.
    
    Time complexity: O(n) with only one loop
    """
    digits = [int(d) for d in bank.strip()]
    n = len(digits)
    
    if n < 2:
        return 0
    
    max_joltage = 0
    max_second = digits[n-1]  # Best second battery seen so far
    
    # Iterate backwards from second-to-last to first
    for i in range(n-2, -1, -1):
        # Use current digit as first battery, max_second as second battery
        joltage = 10 * digits[i] + max_second
        max_joltage = max(max_joltage, joltage)
        # Update the best second battery
        max_second = max(max_second, digits[i])
    
    return max_joltage


def find_max_joltage_k_batteries(bank, k=12):
    """
    Find the maximum k-digit joltage by selecting exactly k batteries.
    
    Use a greedy monotonic stack with explicit index tracking:
    - Stack stores (digit, original_index) tuples
    - Remove digits when we find a larger digit later (if we can afford to remove)
    - This maximizes the value by putting larger digits in earlier positions
    - Maintains original order through index tracking
    
    Time complexity: O(n)
    Space complexity: O(k)
    """
    digits = bank.strip()
    n = len(digits)
    
    if n < k:
        return int(digits)
    if n == k:
        return int(digits)
    
    to_remove = n - k
    stack = []  # Stack stores (digit, index) to track original positions
    
    for i, digit in enumerate(digits):
        # Greedily remove smaller digits when we find a larger one
        while stack and stack[-1][0] < digit and to_remove > 0:
            stack.pop()
            to_remove -= 1
        
        stack.append((digit, i))  # Store digit with its original index
    
    # If we still need to remove digits, remove from the end
    while to_remove > 0:
        stack.pop()
        to_remove -= 1
    
    # Take only k digits (already in order by index)
    # The indices are: [stack[i][1] for i in range(min(k, len(stack)))]
    result = ''.join(digit for digit, idx in stack[:k])
    return int(result)


def solve_part1(input_text):
    """
    Find the sum of maximum joltages from all banks (2 batteries each).
    """
    lines = input_text.strip().split('\n')
    total = 0
    
    for line in lines:
        line = line.strip()
        if line:
            max_jolt = find_max_joltage(line)
            total += max_jolt
    
    return total


def solve_part2(input_text):
    """
    Find the sum of maximum joltages from all banks (12 batteries each).
    """
    lines = input_text.strip().split('\n')
    total = 0
    
    for line in lines:
        line = line.strip()
        if line:
            max_jolt = find_max_joltage_k_batteries(line, k=12)
            total += max_jolt
    
    return total


def find_max_joltage_k_batteries_debug(bank, k=12):
    """
    Debug version that shows which indices are selected.
    """
    digits = bank.strip()
    n = len(digits)
    
    if n < k:
        return int(digits), list(range(n))
    if n == k:
        return int(digits), list(range(n))
    
    to_remove = n - k
    stack = []
    
    for i, digit in enumerate(digits):
        while stack and stack[-1][0] < digit and to_remove > 0:
            stack.pop()
            to_remove -= 1
        stack.append((digit, i))
    
    while to_remove > 0:
        stack.pop()
        to_remove -= 1
    
    selected = stack[:k]
    indices = [idx for digit, idx in selected]
    result = ''.join(digit for digit, idx in selected)
    return int(result), indices


if __name__ == "__main__":
    # Test Part 2 with examples (with index tracking)
    examples = [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ]
    
    print("Testing Part 2 examples with index tracking:")
    all_correct = True
    for bank, expected in examples:
        result, indices = find_max_joltage_k_batteries_debug(bank, k=12)
        status = '✓' if result == expected else '✗'
        selected_str = ''.join(bank[i] for i in indices)
        print(f"  {status} {bank}")
        print(f"     Indices: {indices}")
        print(f"     Selected: {selected_str} -> {result}")
        if result != expected:
            all_correct = False
    
    if all_correct:
        print("\nAll Part 2 tests passed!\n")
    
    # Calculate example sum
    example_sum = sum(expected for _, expected in examples)
    print(f"Example sum: {example_sum}\n")
    
    # Run on actual input
    with open('day3_input.txt', 'r') as f:
        input_text = f.read()
    
    result_part1 = solve_part1(input_text)
    print(f"Part 1: {result_part1}")
    
    result_part2 = solve_part2(input_text)
    print(f"Part 2: {result_part2}")
