# Python Functions: Complete Guide

## 1. What is a Function?
A function is a reusable block of code that performs a specific task. Functions help organize code, avoid repetition, and improve readability.

**Syntax:**
```python
def function_name(parameters):
    # code block
    return value
```

## 2. Types of Functions
- **Built-in Functions:** Provided by Python (e.g., `print()`, `len()`, `sum()`).
- **User-defined Functions:** Created by the programmer using `def`.
- **Lambda Functions:** Anonymous, single-expression functions using `lambda`.
- **Recursive Functions:** Functions that call themselves.

**Examples:**
```python
# User-defined function
def greet(name):
    print(f"Hello, {name}!")

# Lambda function
square = lambda x: x * x
print(square(5))  # Output: 25

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

## 3. Function Definition and Calling
- **Defining:** Use `def` keyword.
- **Calling:** Use function name followed by parentheses and arguments.

```python
def add(a, b):
    return a + b

result = add(2, 3)  # Output: 5
```

## 4. Return Statement
- **Purpose:** Send a result back to the caller.
- **Multiple Returns:** Return multiple values as tuple.

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

min_val, max_val, total = get_stats([1, 2, 3])
```

## 5. Importing and Exporting Functions/Files
- **Importing:** Use `import` or `from ... import ...`.
- **Exporting:** Any function defined in a `.py` file can be imported elsewhere.

**Example:**
Suppose you have `math_utils.py`:
```python
def add(a, b):
    return a + b
```
To use in another file:
```python
from math_utils import add
print(add(2, 3))
```

- **Importing entire module:**
```python
import math_utils
print(math_utils.add(2, 3))
```

- **Exporting:** Just define functions in a `.py` file. To make a module reusable, avoid running code on import (use `if __name__ == "__main__":`).

## 6. Scope in Python
- **Local Scope:** Variables defined inside a function.
- **Global Scope:** Variables defined outside all functions.
- **Nonlocal Scope:** Used in nested functions to refer to variables in the enclosing function.
- **LEGB Rule:** Python looks for variables in Local, Enclosing, Global, Built-in scopes (in order).

**Examples:**
```python
global_var = "I am global"

def outer():
    enclosing_var = "I am enclosing"
    def inner():
        local_var = "I am local"
        print(local_var)
        print(enclosing_var)
        print(global_var)
    inner()
outer()
```

- **global keyword:**
```python
def set_global():
    global global_var
    global_var = "Changed globally"
```

- **nonlocal keyword:**
```python
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)  # Output: inner
```

## 7. Best Practices
- Use descriptive function names.
- Keep functions short and focused.
- Document functions with docstrings.
- Avoid using global variables unless necessary.
- Use type hints for clarity.

**Example with docstring and type hints:**
```python
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b
```

## Using *args and **kwargs in Python Functions

### What are *args and **kwargs?
- `*args` allows a function to accept any number of positional arguments as a tuple.
- `**kwargs` allows a function to accept any number of keyword arguments as a dictionary.

### Why use them?
- They make your functions flexible and able to handle varying numbers of arguments.
- Useful for writing generic, reusable code.

### Example
```python
def secialChai(*ing, **extra):
    print("Ingredients:", ing)      # Tuple of positional arguments
    print("Extras:", extra)         # Dictionary of keyword arguments

secialChai("chineman", "Cardmom", sweetner="honey", foam="yes")
```
**Output:**
```
Ingredients: ('chineman', 'Cardmom')
Extras: {'sweetner': 'honey', 'foam': 'yes'}
```

### How it works
- All positional arguments after the function name are collected into the tuple `ing`.
- All keyword arguments are collected into the dictionary `extra`.

### When to use
- When you don’t know in advance how many arguments will be passed.
- When you want to allow optional configuration via keywords.

### Best Practices
- Name them `*args` and `**kwargs` by convention, but any name works (e.g., `*ing`, `**extra`).
- You can combine regular parameters, `*args`, and `**kwargs` in one function.

### Advanced Usage
You can also unpack arguments when calling functions:
```python
ingredients = ("ginger", "cinnamon")
extras = {"sweetner": "jaggery", "foam": "no"}
secialChai(*ingredients, **extras)
```

---

This guide covers all essential aspects of Python functions, types, return statements, importing/exporting, and scopes. Refer to this document for quick revision and deeper understanding.
