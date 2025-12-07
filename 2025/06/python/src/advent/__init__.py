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
    with open(filename) as f:
        lines = [line.strip() for line in f]

    if verbose >= 1:
        console.print(f"Read [cyan]{len(lines)}[/cyan] lines from [yellow]{filename}[/yellow]")

    # TODO: Implement solution
    result = 0

    console.print(f"Part 1: [bold green]{result}[/bold green]")


@cli.command(name="2")
@common_options
def part2(filename: str, verbose: int) -> None:
    """Run part 2 of the solution."""
    with open(filename) as f:
        lines = [line.strip() for line in f]

    if verbose >= 1:
        console.print(f"Read [cyan]{len(lines)}[/cyan] lines from [yellow]{filename}[/yellow]")

    # TODO: Implement solution
    result = 0

    console.print(f"Part 2: [bold green]{result}[/bold green]")


if __name__ == "__main__":
    cli()
