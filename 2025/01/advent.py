import click
from rich.console import Console
import functools

console = Console()

def setup():
    pass

def common_options(f):
    @click.argument('filename', type=click.Path(exists=True))
    @click.option('-v', '--verbose', is_flag=True, help='Enable verbose output')
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@click.group()
def cli():
    """Advent of Code 2025 Day 1 solution."""
    setup()

@cli.command(name='1')
@common_options
def part1(filename: str, verbose: bool):
    pos = 50
    zeroes = 0

    if verbose:
        console.print(f"The dial starts by pointing at [bold cyan]{pos}[/bold cyan].")

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            dir = -1 if line[0] == 'L' else 1
            dist = int(line[1:]) % 100

            pos = (pos + dir * dist) % 100

            if verbose:
                console.print(f"The dial is rotated [yellow]{line}[/yellow] to point at [bold cyan]{pos}[/bold cyan].")
            if pos == 0:
                zeroes += 1

    console.print(f"The dial pointed at 0 a total of [bold green]{zeroes}[/bold green] times.")


@cli.command(name='2')
@common_options
def part2(filename: str, verbose: bool):
    pass

if __name__ == '__main__':
    cli()
