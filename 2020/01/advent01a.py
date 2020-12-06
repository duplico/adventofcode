import itertools
import click

@click.command()
@click.argument('input_file', type=click.Path(dir_okay=False))
def main(input_file='input.txt'):
     expenses = [int(line.strip()) for line in open(input_file)]
     
     expenses_product = itertools.product(expenses, expenses)

     for candidate in expenses_product:
          if candidate[0] + candidate[1] == 2020:
               print(candidate[0] * candidate[1])
               exit(0)

if __name__ == '__main__':
     main()
