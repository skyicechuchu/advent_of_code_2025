# Advent of Code 2025 🎄

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) - a series of daily programming puzzles throughout December.

## About

Advent of Code is an annual event featuring 25 days of programming challenges. Each day typically includes two parts, with the second part building upon or modifying the first.

## Structure

Each day's solution is organized in its own directory:

```
dayX/
├── dayX.py          # Solution code
└── dayX_input.txt   # Puzzle input
```

## Solutions

### Day 1: Safe Dial Puzzle 🔐

A puzzle involving a circular dial numbered 0-99, starting at position 50.

**Part 1**: Count how many times the dial lands exactly on 0 after following rotation instructions.
- Instructions format: `R<distance>` (rotate right) or `L<distance>` (rotate left)
- The dial wraps around (modulo 100)

**Part 2**: Count how many times the dial passes through 0 during rotations, including when it lands on 0.
- Tracks all passes through position 0, not just final positions

#### Running Day 1

```bash
cd day1
python day1.py
```

### Day 2: Invalid ID Detection 🔢

A puzzle involving detecting invalid IDs based on pattern matching rules.

**Part 1**: Find IDs with the "mirror property" - where the first half of digits equals the second half.
- Example: `1010` (10|10), `446446` (446|446), `1188511885` (11885|11885)
- Only even-length numbers can have this property
- Sum all invalid IDs found in the given ranges

**Part 2**: Find IDs made of repeating patterns (at least twice).
- Example: `11` (1×2), `123123` (123×2), `565656` (56×3), `1111111` (1×7)
- Any sequence repeated 2+ times makes the ID invalid
- This catches more IDs than Part 1 (e.g., `111`, `565656`, `2121212121`)
- Sum all invalid IDs found in the given ranges

**Input Format**: Comma-separated ranges like `11-22,95-115,998-1012`
- Each range expands to all numbers between start and end (inclusive)

#### Running Day 2

```bash
cd day2
python day2.py
```

### Day 3: Battery Joltage Optimization 🔋

A puzzle about maximizing joltage output by selecting batteries from banks.

**Part 1**: Select exactly 2 batteries from each bank to maximize the 2-digit joltage.
- Example: From `987654321111111`, select batteries at positions 0,1 → `98` jolts
- Batteries must maintain their original order (cannot rearrange)
- Use greedy algorithm with suffix maximum tracking
- Time complexity: O(n) with single pass optimization
- Sum all maximum joltages across all banks

**Part 2**: Select exactly 12 batteries from each bank to maximize the 12-digit joltage.
- Example: From `234234234234278`, select 12 batteries → `434234234278` jolts
- Use monotonic stack with index tracking to greedily select largest digits
- Maintains original order by tracking (digit, index) pairs
- Algorithm removes smaller digits when larger ones appear later
- Time complexity: O(n), Space complexity: O(k) where k=12
- Sum all maximum joltages across all banks

**Key Algorithm**: Greedy monotonic stack
1. Calculate how many digits to remove: `n - k`
2. For each digit, remove smaller digits from stack if beneficial
3. Maintains indices to preserve original order
4. Example: `234234234234278` → skips first 3 digits to keep larger `4` at position 2

#### Running Day 3

```bash
cd day3
python day3.py
```

### Day 4: Paper Roll Accessibility 📦

A puzzle about determining which paper rolls can be accessed by forklifts based on neighbor density.

**Part 1**: Count rolls that can be accessed immediately.
- A roll (`@`) can be accessed if it has fewer than 4 adjacent rolls (out of 8 possible neighbors)
- Check all 8 directions: horizontal, vertical, and diagonal
- Simple neighbor counting - no graph algorithms needed
- Time complexity: O(rows × cols), Space: O(1)

**Part 2**: Simulate iterative removal process.
- Once accessible rolls are removed, more rolls may become accessible
- Continue removing newly accessible rolls until none remain
- This creates a cascading effect as neighbor counts decrease
- Example progression: 13 → 12 → 7 → 5 → 2 → 1 → 1 → 1 → 1 rolls removed
- Returns total number of rolls removed across all iterations

**Algorithm**: Iterative simulation
1. Find all rolls with < 4 adjacent rolls
2. Remove them all simultaneously (mark as `.`)
3. Recalculate which rolls are now accessible
4. Repeat until no more rolls can be removed

#### Running Day 4

```bash
cd day4
python day4.py
```

### Day 5: Fresh Ingredient Database 🥗

A puzzle about checking ingredient freshness using ID ranges.

**Part 1**: Count how many available ingredients are fresh.
- Input has two sections: fresh ID ranges, then available IDs
- An ingredient ID is fresh if it falls within any range (inclusive)
- Ranges can overlap - an ID is fresh if in ANY range
- Example: ID 17 is fresh because it's in both 16-20 and 12-18
- Simple range membership checking

**Part 2**: Count all unique IDs considered fresh by the ranges.
- Ignore the available IDs section
- Count total coverage of all fresh ranges
- Requires merging overlapping ranges to avoid double-counting
- Example: Ranges 10-14, 12-18, 16-20 → merged to 10-20 → 11 IDs

**Algorithm**: Interval merging
1. Sort ranges by start position
2. Merge overlapping ranges: if `start ≤ last_end + 1`, extend last range
3. Count IDs in all merged ranges: `sum(end - start + 1)`
4. Time complexity: O(n log n) for sorting, Space: O(n)

#### Running Day 5

```bash
cd day5
python day5.py
```

## Requirements

- Python 3.x

No external dependencies required for current solutions.

## Usage

1. Clone this repository
2. Navigate to the specific day's directory
3. Run the Python script for that day
4. Solutions will print to the console

## Progress

| Day | Part 1 | Part 2 | Solution |
|-----|--------|--------|----------|
| 1   | ⭐     | ⭐     | [Python](day1/day1.py) |
| 2   | ⭐     | ⭐     | [Python](day2/day2.py) |
| 3   | ⭐     | ⭐     | [Python](day3/day3.py) |
| 4   | ⭐     | ⭐     | [Python](day4/day4.py) |
| 5   | ⭐     | ⭐     | [Python](day5/day5.py) |
| ... | ...    | ...    | ... |

## Notes

- Input files are specific to each user and are included in each day's directory
- Solutions prioritize clarity and correctness over performance (unless optimization is part of the challenge)

---

*Happy Coding! 🎅*

*Enjoy with Bro coding! 👨‍💻🤝💪✨*

