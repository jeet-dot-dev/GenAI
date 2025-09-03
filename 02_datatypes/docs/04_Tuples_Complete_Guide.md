# Python Tuples - Complete Guide

## Overview
Tuples are ordered, immutable collections in Python. They are similar to lists but cannot be changed after creation, making them perfect for storing related data that shouldn't be modified.

## Tuple Basics

### Definition & Creation
```python
# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Tuple with elements
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed = (1, "hello", 3.14, True)

# Single element tuple (note the comma!)
single = (42,)     # Correct
# single = (42)    # This is just an integer in parentheses!

# Tuple without parentheses (tuple packing)
point = 10, 20     # Same as (10, 20)
rgb = 255, 128, 0  # Same as (255, 128, 0)
```

### Key Characteristics
- **Ordered**: Elements maintain their position
- **Immutable**: Cannot be modified after creation
- **Allow Duplicates**: Same elements can appear multiple times
- **Hashable**: Can be used as dictionary keys (if all elements are hashable)
- **Heterogeneous**: Can store different data types

## Tuple Indexing & Slicing

### Indexing (Same as Lists and Strings)
```python
colors = ("red", "green", "blue", "yellow")
#          0       1        2       3      (positive)
#         -4      -3       -2      -1      (negative)

print(colors[0])   # "red"
print(colors[-1])  # "yellow"
print(colors[2])   # "blue"
```

### Slicing
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numbers[2:6])     # (2, 3, 4, 5)
print(numbers[:5])      # (0, 1, 2, 3, 4)
print(numbers[5:])      # (5, 6, 7, 8, 9)
print(numbers[:])       # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Step slicing
print(numbers[::2])     # (0, 2, 4, 6, 8)
print(numbers[::-1])    # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

## Tuple Methods & Operations

### Limited Methods (Due to Immutability)
```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - counts occurrences
count = numbers.count(2)  # 3

# index() - returns index of first occurrence
idx = numbers.index(2)    # 1
# idx = numbers.index(2, 2)  # 3 (search starting from index 2)

# Length
length = len(numbers)     # 7

# Membership testing
print(3 in numbers)       # True
print(10 in numbers)      # False
```

### Operations That Work with Tuples
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation (creates new tuple)
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3       # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Comparison (lexicographic)
print((1, 2) < (1, 3))     # True
print((1, 2, 3) == (1, 2, 3))  # True
```

## Tuple Unpacking

### Basic Unpacking
```python
point = (10, 20)
x, y = point  # x = 10, y = 20

# Multiple assignment
a, b, c = (1, 2, 3)

# Swapping variables
a, b = b, a
```

### Advanced Unpacking
```python
# Star expression (Python 3+)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
# first = 1, middle = [2, 3, 4], last = 5

first, *rest = numbers
# first = 1, rest = [2, 3, 4, 5]

*beginning, last = numbers
# beginning = [1, 2, 3, 4], last = 5

# Ignoring values with underscore
data = ("John", "Doe", 30, "Engineer")
first_name, last_name, _, profession = data
```

### Function Arguments Unpacking
```python
def calculate(x, y, z):
    return x + y + z

values = (10, 20, 30)
result = calculate(*values)  # Unpacks tuple as arguments

# Dictionary unpacking (if tuple contains key-value pairs)
def greet(name, age):
    return f"Hello {name}, you are {age} years old"

person_data = ("Alice", 25)
message = greet(*person_data)
```

## Named Tuples

### Creating Named Tuples
```python
from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')  # Can use string with spaces

# Create instances
p1 = Point(10, 20)
person = Person("Alice", 30, "New York")

# Access by name or index
print(p1.x)        # 10 (by name)
print(p1[0])       # 10 (by index)
print(person.name) # "Alice"
print(person[0])   # "Alice"
```

### Named Tuple Methods
```python
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

# _asdict() - convert to dictionary
d = p._asdict()  # {'x': 10, 'y': 20}

# _replace() - create new instance with some fields changed
p2 = p._replace(x=30)  # Point(x=30, y=20)

# _fields - get field names
print(Point._fields)  # ('x', 'y')

# _make() - create from iterable
coords = [15, 25]
p3 = Point._make(coords)  # Point(x=15, y=25)
```

## Memory & Performance

### Memory Efficiency
```python
import sys

# Tuples are more memory efficient than lists
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(sys.getsizeof(list_data))   # More bytes
print(sys.getsizeof(tuple_data))  # Fewer bytes
```

### Performance Characteristics
| Operation | Tuple | List | Notes |
|-----------|-------|------|-------|
| Creation | Faster | Slower | Tuples are optimized |
| Access | Same | Same | Both O(1) |
| Iteration | Slightly faster | Slightly slower | Less overhead |
| Memory | Less | More | No over-allocation |

## Important Interview Questions & Concepts

### 1. When to Use Tuples vs Lists?

**Use Tuples When:**
- Data represents a record (like coordinates, RGB values)
- Data shouldn't change (immutable requirement)
- Need to use as dictionary key
- Want better performance for read-only operations
- Returning multiple values from function

**Use Lists When:**
- Data needs to be modified
- Adding/removing elements frequently
- Need list-specific methods (append, sort, etc.)

```python
# Good tuple usage
def get_name_age():
    return "Alice", 25  # Returns tuple

coordinates = (10, 20)  # Point coordinates don't change
rgb_color = (255, 128, 0)  # Color values are fixed

# Good list usage
shopping_cart = ["apple", "banana"]  # Items can be added/removed
scores = [85, 90, 78]  # Scores can be updated
```

### 2. Tuple Immutability vs Content Mutability
```python
# Tuple itself is immutable
coordinates = ([1, 2], [3, 4])
# coordinates[0] = [5, 6]  # TypeError: cannot assign

# But mutable objects inside can be modified
coordinates[0][0] = 99  # This works!
print(coordinates)  # ([99, 2], [3, 4])

# To make truly immutable, use immutable objects
coordinates = ((1, 2), (3, 4))  # Nested tuples
```

### 3. Tuple Packing and Unpacking
```python
# Tuple packing (implicit tuple creation)
def get_user_info():
    return "Alice", 25, "Engineer"  # Automatically creates tuple

# Tuple unpacking
name, age, job = get_user_info()

# Multiple assignment is tuple unpacking
a, b = 10, 20  # Same as a, b = (10, 20)
```

### 4. Single Element Tuple Gotcha
```python
# Common mistake
not_a_tuple = (42)    # This is just an integer: 42
print(type(not_a_tuple))  # <class 'int'>

# Correct single element tuple
single_tuple = (42,)  # Note the comma!
print(type(single_tuple))  # <class 'tuple'>

# Alternative
single_tuple = tuple([42])
```

## Tuple vs Other Data Structures

### Tuple vs List (Detailed Comparison)
| Aspect | Tuple | List |
|--------|-------|------|
| **Syntax** | `(1, 2, 3)` | `[1, 2, 3]` |
| **Mutability** | Immutable | Mutable |
| **Performance** | Faster creation/access | Slower creation |
| **Memory** | Less memory | More memory |
| **Methods** | 2 methods (count, index) | Many methods |
| **Use as dict key** | Yes (if hashable) | No |
| **Iteration** | Slightly faster | Slightly slower |
| **Type safety** | Better for fixed data | Better for dynamic data |

### Tuple vs String
| Feature | Tuple | String |
|---------|-------|--------|
| Elements | Any type | Only characters |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| Immutability | Yes | Yes |
| Concatenation | Creates new tuple | Creates new string |

### When to Choose What
```python
# Tuple: Fixed structure data
person = ("John", "Doe", 30)  # Name parts and age

# List: Dynamic collection
tasks = ["buy milk", "walk dog"]  # Can add/remove tasks

# String: Text data
message = "Hello World"  # Text content

# Named Tuple: Structured data with named fields
Employee = namedtuple('Employee', 'name department salary')
emp = Employee("Alice", "Engineering", 75000)
```

## Best Practices

1. **Use tuples for returning multiple values** from functions
2. **Use named tuples** for better code readability
3. **Use tuples as dictionary keys** when you need composite keys
4. **Don't confuse single-element tuple syntax**
5. **Use tuple unpacking** for cleaner code

```python
# Good practices

# 1. Function returning multiple values
def analyze_data(data):
    return len(data), sum(data), max(data)

count, total, maximum = analyze_data([1, 2, 3, 4, 5])

# 2. Named tuples for clarity
Rectangle = namedtuple('Rectangle', 'width height')
rect = Rectangle(10, 20)
area = rect.width * rect.height

# 3. Tuple as dictionary key
locations = {
    (0, 0): "origin",
    (1, 0): "right",
    (0, 1): "up"
}

# 4. Tuple unpacking in loops
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"Point: ({x}, {y})")
```

## Common Pitfalls

1. **Forgetting comma in single-element tuple**
2. **Trying to modify tuple elements**
3. **Confusing tuple unpacking behavior**
4. **Not understanding mutable objects inside tuples**

```python
# Pitfall examples

# 1. Single element confusion
coordinates = (42)  # Not a tuple!
coordinates = (42,) # Correct tuple

# 2. Modification attempt
point = (10, 20)
# point[0] = 15  # TypeError!

# 3. Unpacking mismatch
data = (1, 2, 3)
# a, b = data  # ValueError: too many values to unpack

# 4. Mutable content confusion
lists_tuple = ([1, 2], [3, 4])
lists_tuple[0].append(3)  # This works! Tuple is ([1, 2, 3], [3, 4])
```

## Summary

Python tuples are:
- **Immutable**: Cannot be changed after creation
- **Ordered**: Elements maintain their position
- **Hashable**: Can be used as dictionary keys
- **Memory efficient**: Less memory than lists
- **Fast**: Optimized for read operations

Key concepts to remember:
- Use parentheses and commas for creation
- Single-element tuples need trailing comma
- Perfect for fixed, structured data
- Named tuples provide enhanced readability
- Ideal for function return values
- Better performance than lists for read-only data
