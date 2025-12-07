#!/usr/bin/env python3
"""
Regression Test Suite for Advent of Code 2025

Runs all completed day solutions and verifies outputs match expected results.
This ensures code changes don't break existing solutions.

Usage:
    python test_solutions.py          # Run all tests
    python test_solutions.py --day 6  # Run specific day
"""

import sys
import os
import importlib.util
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

console = Console()

# Expected answers for each day (Part 1, Part 2)
EXPECTED_ANSWERS = {
    1: (1097, 7101),
    2: (9188031749, 11323661261),
    3: (16842, 167523425665348),
    4: (1604, 9397),
    5: (782, 353863745078671),
    6: (5782351442566, 10194584711842),
    7: (1678, 357525737893560),
}


def load_day_module(day_num):
    """Dynamically load a day's module."""
    day_dir = f"day{day_num}"
    script_path = os.path.join(day_dir, f"day{day_num}.py")
    
    if not os.path.exists(script_path):
        return None
    
    spec = importlib.util.spec_from_file_location(f"day{day_num}", script_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"day{day_num}"] = module
    spec.loader.exec_module(module)
    
    return module


def read_input(day_num):
    """Read input file for a day."""
    input_path = os.path.join(f"day{day_num}", f"day{day_num}_input.txt")
    
    if not os.path.exists(input_path):
        return None
    
    with open(input_path, 'r') as f:
        return f.read()


def test_day(day_num):
    """
    Test a specific day's solution.
    Returns (success, part1_result, part2_result, error_message)
    """
    module = load_day_module(day_num)
    if not module:
        return False, None, None, "Module not found"
    
    input_text = read_input(day_num)
    if input_text is None:
        return False, None, None, "Input file not found"
    
    expected_p1, expected_p2 = EXPECTED_ANSWERS.get(day_num, (None, None))
    
    # Test Part 1
    p1_result = None
    p1_pass = True
    p1_error = None
    
    if hasattr(module, 'solve_part1'):
        try:
            p1_result = module.solve_part1(input_text)
            if expected_p1 is not None and p1_result != expected_p1:
                p1_pass = False
                p1_error = f"Expected {expected_p1}, got {p1_result}"
        except Exception as e:
            p1_pass = False
            p1_error = str(e)
    
    # Test Part 2
    p2_result = None
    p2_pass = True
    p2_error = None
    
    if hasattr(module, 'solve_part2'):
        try:
            p2_result = module.solve_part2(input_text)
            if expected_p2 is not None and p2_result != expected_p2:
                p2_pass = False
                p2_error = f"Expected {expected_p2}, got {p2_result}"
        except Exception as e:
            p2_pass = False
            p2_error = str(e)
    
    success = p1_pass and p2_pass
    error_msg = None
    if not success:
        error_msg = f"P1: {p1_error or 'OK'}, P2: {p2_error or 'OK'}"
    
    return success, p1_result, p2_result, error_msg


def run_all_tests():
    """Run tests for all completed days."""
    days_to_test = [day for day in EXPECTED_ANSWERS.keys() 
                    if EXPECTED_ANSWERS[day] != (None, None)]
    
    console.print("\n[bold cyan]🧪 Running Regression Test Suite[/bold cyan]\n")
    
    results = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        console=console,
        transient=False,
    ) as progress:
        
        task = progress.add_task("[cyan]Testing days...", total=len(days_to_test))
        
        for day in days_to_test:
            progress.update(task, description=f"[cyan]Testing Day {day}...")
            success, p1, p2, error = test_day(day)
            results.append((day, success, p1, p2, error))
            progress.advance(task)
    
    # Display results table
    table = Table(title="\n📊 Test Results")
    table.add_column("Day", justify="right", style="cyan", no_wrap=True)
    table.add_column("Status", style="bold")
    table.add_column("Part 1", justify="right")
    table.add_column("Part 2", justify="right")
    table.add_column("Notes", style="dim")
    
    passed = 0
    failed = 0
    
    for day, success, p1, p2, error in results:
        if success:
            passed += 1
            status = "[green]✓ PASS[/green]"
            notes = ""
        else:
            failed += 1
            status = "[red]✗ FAIL[/red]"
            notes = error or ""
        
        table.add_row(
            f"{day}",
            status,
            str(p1) if p1 is not None else "-",
            str(p2) if p2 is not None else "-",
            notes
        )
    
    console.print(table)
    
    # Summary
    total = passed + failed
    if failed == 0:
        console.print(f"\n[bold green]✨ All {total} tests passed! ✨[/bold green]\n")
    else:
        console.print(f"\n[bold red]❌ {failed}/{total} tests failed[/bold red]\n")
    
    return failed == 0


def run_single_test(day_num):
    """Run test for a single day."""
    console.print(f"\n[bold cyan]🧪 Testing Day {day_num}[/bold cyan]\n")
    
    success, p1, p2, error = test_day(day_num)
    
    if success:
        console.print(f"[green]✓ Day {day_num} - PASS[/green]")
        console.print(f"  Part 1: {p1}")
        console.print(f"  Part 2: {p2}")
    else:
        console.print(f"[red]✗ Day {day_num} - FAIL[/red]")
        console.print(f"  {error}")
    
    console.print()
    return success


if __name__ == "__main__":
    # Check for specific day argument
    if len(sys.argv) > 1 and sys.argv[1] == "--day":
        if len(sys.argv) > 2:
            try:
                day = int(sys.argv[2])
                success = run_single_test(day)
                sys.exit(0 if success else 1)
            except ValueError:
                console.print("[red]Invalid day number[/red]")
                sys.exit(1)
        else:
            console.print("[red]Please specify a day number: --day <num>[/red]")
            sys.exit(1)
    
    # Run all tests
    success = run_all_tests()
    sys.exit(0 if success else 1)

