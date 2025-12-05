"""Advent of Code solution."""

import functools

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

    fresh_ranges = set()
    ids = []

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if '-' in line:
                start_str, end_str = line.split('-')
                start, end = int(start_str), int(end_str)
                fresh_ranges.add((start, end))
            elif line:
                ids.append(int(line))

    if verbose >= 1:
        console.print(f"Read [cyan]{len(lines)}[/cyan] lines from [yellow]{filename}[/yellow]")

    result = 0

    for id_ in ids:
        for start, end in fresh_ranges: # Note: inclusive
            if start <= id_ <= end:
                result += 1
                break

    console.print(f"Part 1: [bold green]{result}[/bold green]")

def merge_range_into_set(range_in: tuple[int, int], range_set: set[tuple[int, int]]) -> None:
    start_in, end_in = range_in
    for existing_range in range_set:
        start, end = existing_range
        # If ranges overlap or are adjacent, pop the existing range from the set,
        #  merge them to create a new range, and recursively merge that new range back into the set.

@cli.command(name="2")
@common_options
def part2(filename: str, verbose: int) -> None:
    """Run part 2 of the solution."""

    fresh_ranges_in = set()

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if '-' in line:
                start_str, end_str = line.split('-')
                start, end = int(start_str), int(end_str)
                fresh_ranges_in.add((start, end))

    fresh_ranges = set()
    fresh_ranges.add(fresh_ranges_in.pop())

    while fresh_ranges_in:
        start_in, end_in = fresh_ranges_in.pop()
        for fresh_range in fresh_ranges:
            start, end = fresh_range
            # If ranges overlap or are adjacent, merge them
            if not (end_in < start - 1 or start_in > end + 1):
                # Merge ranges
                new_start = min(start, start_in)
                new_end = max(end, end_in)
                fresh_ranges.remove(fresh_range)
                fresh_ranges.add((new_start, new_end))
                break
            else: # Otherwise, add the input range to the 
                fresh_ranges.add((start_in, end_in))

    if verbose >= 1:
        console.print(f"Read [cyan]{len(lines)}[/cyan] lines from [yellow]{filename}[/yellow]")

    # TODO: Implement solution
    result = 0

    console.print(f"Part 2: [bold green]{result}[/bold green]")


if __name__ == "__main__":
    cli()
