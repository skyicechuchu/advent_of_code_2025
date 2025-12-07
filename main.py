import os
import sys
import importlib.util
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint

console = Console()

def get_completed_days():
    days = []
    for item in os.listdir('.'):
        if item.startswith('day') and os.path.isdir(item):
            try:
                day_num = int(item[3:])
                days.append(day_num)
            except ValueError:
                continue
    return sorted(days)

def run_day(day_num):
    day_dir = f"day{day_num}"
    script_path = os.path.join(day_dir, f"day{day_num}.py")
    input_path = os.path.join(day_dir, f"day{day_num}_input.txt")
    
    if not os.path.exists(script_path):
        console.print(f"[red]Error: {script_path} not found[/red]")
        return

    # Load module dynamically
    spec = importlib.util.spec_from_file_location(f"day{day_num}", script_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"day{day_num}"] = module
    spec.loader.exec_module(module)
    
    # Read input
    if os.path.exists(input_path):
        with open(input_path, 'r') as f:
            input_text = f.read()
    else:
        input_text = ""
        console.print("[yellow]Warning: Input file not found[/yellow]")

    console.print(Panel(f"[bold blue]🎄 Running Advent of Code - Day {day_num} 🎄[/bold blue]", expand=False))
    
    # Part 1
    if hasattr(module, 'solve_part1'):
        try:
            p1 = module.solve_part1(input_text)
            console.print(f"[green]Part 1:[/green] [bold white]{p1}[/bold white]")
        except Exception as e:
            console.print(f"[red]Part 1 Error:[/red] {e}")
    
    # Part 2
    if hasattr(module, 'solve_part2'):
        try:
            p2 = module.solve_part2(input_text)
            console.print(f"[green]Part 2:[/green] [bold white]{p2}[/bold white]")
        except Exception as e:
            console.print(f"[red]Part 2 Error:[/red] {e}")

def main():
    # Check if a specific day is requested
    if len(sys.argv) > 1:
        try:
            day_to_run = int(sys.argv[1])
            run_day(day_to_run)
            return
        except ValueError:
            console.print("[red]Invalid day number[/red]")
            return
    
    # No specific day requested - show dashboard
    rprint("[bold green]Welcome to the AI Pair Programming AoC Runner! 🤖[/bold green]")
    
    days = get_completed_days()
    
    table = Table(title="Completed Puzzles")
    table.add_column("Day", justify="right", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Tech Stack", style="green")

    tech_stacks = {
        1: "Basic Math",
        2: "String Parsing",
        3: "Greedy Stack",
        4: "Simulation",
        5: "Interval Merging",
        6: "NumPy Matrix",
        7: "Beam Simulation"
    }

    for d in days:
        stack = tech_stacks.get(d, "Python")
        table.add_row(f"Day {d}", "⭐⭐ Complete", stack)

    console.print(table)
    console.print("\n[dim]Run specific day: python main.py <day_num>[/dim]")

if __name__ == "__main__":
    main()

