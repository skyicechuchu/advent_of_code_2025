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
| ... | ...    | ...    | ... |

## Notes

- Input files are specific to each user and are included in each day's directory
- Solutions prioritize clarity and correctness over performance (unless optimization is part of the challenge)

---

*Happy Coding! 🎅*

