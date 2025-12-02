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
| 2   | -      | -      | - |
| 3   | -      | -      | - |
| ... | ...    | ...    | ... |

## Notes

- Input files are specific to each user and are included in each day's directory
- Solutions prioritize clarity and correctness over performance (unless optimization is part of the challenge)

---

*Happy Coding! 🎅*

