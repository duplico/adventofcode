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

def merge_range_into_set(range_in: tuple[int, int], ranges: list[tuple[int, int]], verbose: int = 0) -> None:
    start_in, end_in = range_in
    pop_range = None
    for existing_range in ranges:
        start, end = existing_range
        # If ranges overlap or are adjacent, pop the existing range from the set,
        #  merge them to create a new range, and recursively merge that new range back into the set.
        if start_in <= end + 1 and end_in >= start - 1:
            pop_range = existing_range
            break
    
    if pop_range is None:
        ranges.append(range_in)
        if verbose >= 2:
            console.print(f"Adding range [cyan]{range_in}[/cyan] to ranges")
    else:
        ranges.remove(pop_range)
        start, end = pop_range
        new_start = min(start, start_in)
        new_end = max(end, end_in)
        if verbose >= 2:
            console.print(f"Merging range [cyan]{range_in}[/cyan] with existing range [cyan]{pop_range}[/cyan] to form new range [cyan]({new_start}, {new_end})[/cyan]")
        merge_range_into_set((new_start, new_end), ranges)

@cli.command(name="2")
@common_options
def part2(filename: str, verbose: int) -> None:
    """Run part 2 of the solution."""

    ranges = []

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if '-' in line:
                start_str, end_str = line.split('-')
                start, end = int(start_str), int(end_str)
                merge_range_into_set((start, end), ranges, verbose)
                if verbose >= 1:
                    console.print(f"Added [cyan]{(start, end)}[/cyan]; merged ranges: [cyan]{ranges}[/cyan]")

    result = 0
    # The result is the total number covered by all ranges, inclusive of start and end.
    for start, end in ranges:
        result += end - start + 1

    console.print(f"Part 2: [bold green]{result}[/bold green]")


if __name__ == "__main__":
    cli()
