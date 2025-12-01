import click
from rich.console import Console
import functools

console = Console()

def setup():
    pass

def common_options(f):
    @click.argument('filename', type=click.Path(exists=True))
    @click.option('-v', '--verbose', count=True, help='Enable verbose output (-v, -vv)')
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@click.group()
def cli():
    """Advent of Code solution."""
    setup()

@cli.command(name='1')
@common_options
def part1(filename: str, verbose: int):
    pass

@cli.command(name='2')
@common_options
def part2(filename: str, verbose: int):
    pass

if __name__ == '__main__':
    cli()
