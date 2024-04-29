import os  # Importing the os module for operating system functionalities.
import inspect  # Importing the inspect module for introspecting live objects.
import sys  # Importing the sys module for interacting with the Python interpreter.

# Getting the directory path of the current script file.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Getting the parent directory of the current directory.
parentdir = os.path.dirname(currentdir)

# Inserting the parent directory into the beginning of the Python module search path.
sys.path.insert(0, parentdir)

# Printing the path of the current directory.
print(currentdir)
