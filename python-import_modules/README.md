# Python - Import & Modules

This project covers the fundamentals of importing modules and using functions from other files in Python.

## Learning Objectives

- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code from being executed when imported
- How to use command line arguments with your Python programs

## Requirements

- Python 3.12.x
- All files are executable
- Code follows PEP8 style guide
- All files end with a new line
- First line of all files: `#!/usr/bin/python3`

## Files

### Mandatory Tasks

| File | Description |
|------|-------------|
| `0-add.py` | Imports the function `add(a, b)` from `add_0.py` and prints the result |
| `1-calculation.py` | Imports functions from `calculator_1.py` and prints the result of basic operations |
| `2-args.py` | Prints the number of and the list of arguments passed to the program |
| `3-infinite_add.py` | Prints the result of the addition of all arguments |
| `4-hidden_discovery.py` | Prints all names defined by the compiled module `hidden_4.pyc` |
| `5-variable_load.py` | Imports the variable `a` from `variable_load_5.py` and prints its value |

### Module Files

| File | Description |
|------|-------------|
| `add_0.py` | Module containing the `add()` function |
| `calculator_1.py` | Module containing calculator functions (add, sub, mul, div) |
| `variable_load_5.py` | Module containing a variable `a` |

## Usage

Each file can be executed directly:

```bash
./0-add.py
./1-calculation.py
./2-args.py arg1 arg2 arg3
./3-infinite_add.py 1 2 3 4 5
./4-hidden_discovery.py
./5-variable_load.py
```

## Authors

- Alison Amblard
- Damien Rossi
- Yanis Leroy
- Valentin Planchon

Holberton School Project
