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

def part1_valid_id(id: int, verbose: int) -> bool:
    id_str = str(id)
    if len(id_str) % 2 != 0:
        # Odd-length IDs are always valid
        if verbose >= 2:
            console.print(f"  [dim]{id}[/dim]: odd length, [green]valid[/green]")
        return True
    
    half = len(id_str) // 2
    is_valid = id_str[:half] != id_str[half:]
    if verbose >= 2:
        status = "[green]valid[/green]" if is_valid else "[red]invalid[/red]"
        console.print(f"  [dim]{id}[/dim]: [{id_str[:half]}|{id_str[half:]}] {status}")
    return is_valid

@cli.command(name="1")
@common_options
def part1(filename: str, verbose: int) -> None:
    """Run part 1 of the solution."""
    id_sum = 0
    invalid_count = 0

    with open(filename) as f:
        line = f.readline().strip()
        if verbose >= 1:
            console.print(f"Processing ranges: [cyan]{line}[/cyan]")
        ranges = (range(first, second + 1) for first, second in (map(int, r.split("-")) for r in line.split(",")))

        for id_range in ranges:
            for id in id_range:
                if not part1_valid_id(id, verbose):
                    id_sum += id
                    invalid_count += 1

    if verbose >= 1:
        console.print(f"Found [yellow]{invalid_count}[/yellow] invalid IDs")
    console.print(f"Part 1: [bold green]{id_sum}[/bold green]")

def part2_valid_id(id: int, verbose: int) -> bool:
    id_str = str(id)
    for substr_len in range(1, len(id_str) // 2 + 1):
        if len(id_str) % substr_len != 0:
            if verbose >= 3:
                console.print(f"  [dim]{id}[/dim]: skipping pattern length {substr_len} (not a divisor)")
            continue # Cannot evenly divide the string, so skip
        test_pattern = id_str[:substr_len]
        if verbose >= 3:
            console.print(f"  [dim]{id}[/dim]: testing pattern '{test_pattern}'")
        all_match = True
        for substr_index in range(substr_len, len(id_str), substr_len):
            substr = id_str[substr_index:substr_index + substr_len]
            if verbose >= 4:
                console.print(f"    comparing test_pattern '{test_pattern}' to substring '{substr}'")
            if substr != test_pattern:
                all_match = False
                break
        if all_match:
            if verbose >= 1:
                console.print(f"  [dim]{id}[/dim]: repeating pattern '{test_pattern}', [red]invalid[/red]")
            return False
    if verbose >= 2:
        console.print(f"  [dim]{id}[/dim]: no repeating pattern, [green]valid[/green]")
    return True

@cli.command(name="2")
@common_options
def part2(filename: str, verbose: int) -> None:
    """Run part 2 of the solution."""
    id_sum = 0
    invalid_count = 0

    with open(filename) as f:
        line = f.readline().strip()
        if verbose >= 1:
            console.print(f"Processing ranges: [cyan]{line}[/cyan]")
        ranges = (range(first, second + 1) for first, second in (map(int, r.split("-")) for r in line.split(",")))

        for id_range in ranges:
            for id in id_range:
                if not part2_valid_id(id, verbose):
                    id_sum += id
                    invalid_count += 1

    if verbose >= 1:
        console.print(f"Found [yellow]{invalid_count}[/yellow] invalid IDs")
    console.print(f"Part 2: [bold green]{id_sum}[/bold green]")


if __name__ == "__main__":
    cli()
