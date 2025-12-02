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
    pos = 50
    zeroes = 0

    if verbose >= 1:
        console.print(f"The dial starts by pointing at [bold cyan]{pos}[/bold cyan].")

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            dir = -1 if line[0] == 'L' else 1
            dist = int(line[1:]) % 100

            pos = (pos + dir * dist) % 100

            if verbose >= 1:
                console.print(f"The dial is rotated [yellow]{line}[/yellow] to point at [bold cyan]{pos}[/bold cyan].")
            if pos == 0:
                zeroes += 1

    console.print(f"The dial pointed at 0 a total of [bold green]{zeroes}[/bold green] times.")

def part2_turn_dial_right(current_pos: int, distance: int, zeroes: int, verbose: int = 0) -> tuple[int, int]:
    # When turning right, we add to the current position, so calibrate it to 0.
    if current_pos == 100:
        current_pos = 0

    if current_pos + distance < 100:
        new_pos = current_pos + distance
        if verbose >= 2:
            console.print(f" - New position without crossing 0: {new_pos}")
        return new_pos, zeroes
    
    # If we're here, then we have to cross 0 at least once
    # Turn the dial to 0.
    distance -= (100 - current_pos)
    current_pos = 0
    zeroes += 1

    if verbose >= 2:
        console.print(f" - Rotated {100 - current_pos} to 0. new distance to move: {distance}, total zeroes: {zeroes}")

    return part2_turn_dial_right(current_pos, distance, zeroes, verbose)

def part2_turn_dial_left(current_pos: int, distance: int, zeroes: int, verbose: int = 0) -> tuple[int, int]:
    # When turning left, we subtract from the current position, so calibrate it to 100.
    if current_pos == 0:
        current_pos = 100

    if current_pos - distance > 0:
        new_pos = current_pos - distance
        if verbose >= 2:
            console.print(f" - New position without crossing 0: {new_pos}")
        return new_pos, zeroes
    
    # If we're here, then we have to cross 0 at least once
    # Turn the dial to 0.
    distance -= current_pos
    zeroes += 1
    if verbose >= 2:
        console.print(f" - Rotated {100 - current_pos} to 0. new distance to move: {distance}, total zeroes: {zeroes}")
    current_pos = 0

    return part2_turn_dial_left(current_pos, distance, zeroes, verbose)

def part2_turn_dial(current_pos: int, distance: int, verbose: int = 0) -> tuple[int, int]:
    zeroes = 0

    if distance > 0:
        return part2_turn_dial_right(current_pos, distance, zeroes, verbose)
    else:
        return part2_turn_dial_left(current_pos, -distance, zeroes, verbose)

@cli.command(name="2")
@common_options
def part2(filename: str, verbose: int) -> None:
    """Run part 2 of the solution."""
    pos = 50
    zeroes = 0

    if verbose >= 1:
        console.print(f"The dial starts by pointing at [bold cyan]{pos}[/bold cyan].")
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            dir = -1 if line[0] == 'L' else 1
            dist = int(line[1:])

            pos, zeroes_to_add = part2_turn_dial(pos, dir * dist, verbose)
            zeroes += zeroes_to_add

            if verbose >= 1:
                console.print(f"The dial is rotated [yellow]{line}[/yellow] to point at [bold cyan]{pos}[/bold cyan]; during this rotation, it points at zero [bold green]{zeroes_to_add}[/bold green] times.")
    console.print(f"The dial pointed at 0 a total of [bold green]{zeroes}[/bold green] times.")

if __name__ == "__main__":
    cli()
