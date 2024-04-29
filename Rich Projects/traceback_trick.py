from rich.traceback import install
# better traceback user interface
install()

x = 10
y = "Oranges"
print(x + y)

"""
This script will return a traceback error message onto console.
However, it will be displayed in a beatufiul design.
"""