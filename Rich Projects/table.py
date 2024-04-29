from rich.console import Console
from rich.table import Table

# -------------------------

def add_numbers(x, y):
    console.log(f"{x} + {y} =", x + y)
    return x + y


# -------------------------

def create_table():
    table = Table(title="This is a table")

    table.add_column("Make", style="cyan")
    table.add_column("Model", style="magenta")
    table.add_column("Cost", style="green")

    table.add_row("BMW", "X6", "£49,000")
    table.add_row("Mazda", "6", "£28,500")
    table.add_row("Range Rover", "Discovery", "£37,900")

    console.print(table)

# create a console object from Console Class
console = Console()


print("\n---------- Program 1 -------------------------\n")

add_numbers(24, 6)
add_numbers(25, 75)

print("\n---------- Program 2 -------------------------\n")

create_table()
print()
