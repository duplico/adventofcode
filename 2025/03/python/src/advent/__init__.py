"""Advent of Code solution."""

import functools

import click
from rich.console import Console

console = Console()


def setup() -> None:
    """Perform any setup needed before running solutions."""
    pass

def condense_number(number_str: str, target_len: int, verbose: int = 0) -> int:
    window_start = 0
    digits = [int(ch) for ch in number_str]
    result = []
    while target_len:
        target_len -= 1
        highest_digit = -1
        highest_index = -1
        window_end = len(digits) - target_len
        for i in range(window_start, window_end):
            if digits[i] > highest_digit:
                highest_digit = digits[i]
                highest_index = i
        result.append(highest_digit)
        window_start = highest_index + 1
        if verbose >= 2:
            console.print(f"Chose digit [green]{highest_digit}[/green] at index [yellow]{highest_index}[/yellow], new window start is [cyan]{window_start}[/cyan]")
    condensed_number = int(''.join(map(str, result)))
    if verbose >= 1:
        console.print(f"Condensed number from [yellow]{number_str}[/yellow] to [green]{condensed_number}[/green]")
    return condensed_number
        

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

    result = sum(condense_number(line, 2, verbose) for line in lines)

    console.print(f"Part 1: [bold green]{result}[/bold green]")


@cli.command(name="2")
@common_options
def part2(filename: str, verbose: int) -> None:
    """Run part 2 of the solution."""
    with open(filename) as f:
        lines = [line.strip() for line in f]

    if verbose >= 1:
        console.print(f"Read [cyan]{len(lines)}[/cyan] lines from [yellow]{filename}[/yellow]")

    result = sum(condense_number(line, 12, verbose) for line in lines)

    console.print(f"Part 2: [bold green]{result}[/bold green]")


if __name__ == "__main__":
    cli()
