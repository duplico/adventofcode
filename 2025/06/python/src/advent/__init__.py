"""Advent of Code solution."""

import functools
import math

import click
from rich.console import Console

console = Console()


def setup() -> None:
    """Perform any setup needed before running solutions."""
    pass


def common_options[F](f: F) -> F:
    """Decorator that adds common CLI options to a command."""
    @click.argument("filename", type=click.Path(exists=True))
    @click.option("-v", "--verbose", count=True, help="Enable verbose output (-v, -vv)")
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper


@click.group()
def cli() -> None:
    """Advent of Code solution."""
    setup()


@cli.command(name="1")
@common_options
def part1(filename: str, verbose: int) -> None:
    """Run part 1 of the solution."""
    with open(filename) as f:
        lines = [line.strip() for line in f]

    if verbose >= 1:
        console.print(f"Read [cyan]{len(lines)}[/cyan] lines from [yellow]{filename}[/yellow]")

    raise NotImplementedError("Part 1 solution is in clojure.")
    # TODO: Implement solution
    result = 0

    console.print(f"Part 1: [bold green]{result}[/bold green]")


@cli.command(name="2")
@common_options
def part2(filename: str, verbose: int) -> None:
    """Run part 2 of the solution."""
    with open(filename) as f:
        lines = [line[:-1] for line in f] # Remove newline characters

    if verbose >= 1:
        console.print(f"Read [cyan]{len(lines)}[/cyan] lines from [yellow]{filename}[/yellow]")

    col = len(lines[-1]) - 1

    operands = []
    magnitude = 1
    result = 0

    assert len(lines[0]) == len(lines[1]) == len(lines[2]) == len(lines[3]) 

    while col >= 0:
        operand = 0
        row_index = len(lines) - 2
        magnitude = 1
        while row_index >= 0:
            row = lines[row_index]
            if row[col] != ' ':
                operand += int(row[col]) * magnitude
                if verbose >= 2:
                    console.print(f"Reading digit [cyan]{row[col]}[/cyan] from row {row_index}, col {col} with value [cyan]{int(row[col]) * magnitude}[/cyan]")
                magnitude *= 10
            elif verbose >= 2:
                console.print(f"Skipping blank space in row")
            row_index -= 1

        operands.append(operand)
        if verbose >= 1:
            console.print(f"Column {col}: operand = [cyan]{operand}[/cyan]")
        
        if lines[-1][col] == '+':
            result += sum(operands)
            operands = []
            if verbose >= 1:
                console.print(f"Processed addition, intermediate result = [cyan]{result}[/cyan]")
            col -= 2 # The column before the operator is blank, so we need to skip it
        elif lines[-1][col] == '*':
            result += math.prod(operands)
            operands = []
            if verbose >= 1:
                console.print(f"Processed multiplication, intermediate result = [cyan]{result}[/cyan]")
            col -= 2 # The column before the operator is blank, so we need to skip it
        else:
            col -= 1

    console.print(f"Part 2: [bold green]{result}[/bold green]")


if __name__ == "__main__":
    cli()
