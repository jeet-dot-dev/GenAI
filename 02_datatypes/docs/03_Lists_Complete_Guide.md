# Python Lists - Complete Guide

## Overview
Lists are one of the most versatile and commonly used data structures in Python. They are ordered, mutable collections that can store elements of different data types.

## List Basics

### Definition & Creation
```python
# Empty list
empty_list = []
empty_list = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]  # Different data types
nested = [[1, 2], [3, 4], [5, 6]]         # Nested lists

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

### Key Characteristics
- **Ordered**: Elements maintain their position
- **Mutable**: Can be modified after creation
- **Allow Duplicates**: Same elements can appear multiple times
- **Dynamic Size**: Can grow and shrink during runtime
- **Heterogeneous**: Can store different data types

## List Indexing & Slicing

### Indexing (Same as Strings)
```python
fruits = ["apple", "banana", "cherry", "date"]
#          0        1         2        3     (positive)
#         -4       -3        -2       -1     (negative)

print(fruits[0])   # "apple"
print(fruits[-1])  # "date"
print(fruits[2])   # "cherry"
```

### Slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(numbers[2:6])     # [2, 3, 4, 5]
print(numbers[:5])      # [0, 1, 2, 3, 4]
print(numbers[5:])      # [5, 6, 7, 8, 9]
print(numbers[:])       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copy)

# Step slicing
print(numbers[::2])     # [0, 2, 4, 6, 8] (every 2nd element)
print(numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)
print(numbers[1:8:2])   # [1, 3, 5, 7]
```

## List Methods & Operations

### Adding Elements
```python
fruits = ["apple", "banana"]

# append() - adds single element at end
fruits.append("cherry")         # ["apple", "banana", "cherry"]

# insert() - adds element at specific index
fruits.insert(1, "orange")      # ["apple", "orange", "banana", "cherry"]

# extend() - adds multiple elements
fruits.extend(["grape", "kiwi"]) # ["apple", "orange", "banana", "cherry", "grape", "kiwi"]

# + operator - concatenation (creates new list)
new_fruits = fruits + ["mango", "pear"]
```

### Removing Elements
```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# remove() - removes first occurrence
fruits.remove("banana")    # ["apple", "cherry", "banana", "date"]

# pop() - removes and returns element by index
last_item = fruits.pop()   # Returns "date", list becomes ["apple", "cherry", "banana"]
second_item = fruits.pop(1) # Returns "cherry", list becomes ["apple", "banana"]

# del statement - removes by index or slice
del fruits[0]              # ["banana"]
# del fruits[1:3]          # Remove slice

# clear() - removes all elements
fruits.clear()             # []
```

### Finding & Counting
```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# index() - returns index of first occurrence
idx = numbers.index(2)     # 1 (first occurrence)
# idx = numbers.index(2, 2)  # 3 (search starting from index 2)

# count() - counts occurrences
count = numbers.count(2)   # 3

# in operator - membership testing
print(3 in numbers)        # True
print(10 in numbers)       # False
```

### Sorting & Reversing
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - sorts in place (modifies original list)
numbers.sort()             # [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True) # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - returns new sorted list
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)  # [1, 1, 3, 4, 5], original unchanged

# reverse() - reverses in place
numbers.reverse()          # Reverses the list

# Custom sorting
words = ["banana", "pie", "apple", "book"]
words.sort(key=len)        # Sort by length: ["pie", "book", "apple", "banana"]
```

## List Comprehensions

### Basic Syntax
```python
# Basic comprehension: [expression for item in iterable]
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition: [expression for item in iterable if condition]
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

# Nested comprehensions
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

### Advanced Comprehensions
```python
# String processing
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]  # ["HELLO", "WORLD", "PYTHON"]

# Conditional expression
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
# ["odd", "even", "odd", "even", "odd"]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4, 5, 6]
```

## Memory & Performance

### List Memory Layout
- Lists store references to objects, not the objects themselves
- Dynamic array implementation (C array behind the scenes)
- Over-allocation for efficiency (capacity > size)

```python
import sys

# Memory usage
small_list = [1, 2, 3]
large_list = list(range(1000))

print(sys.getsizeof(small_list))  # Memory in bytes
print(sys.getsizeof(large_list))
```

### Performance Characteristics
| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| `list[i]` | O(1) | Index access |
| `list.append(x)` | O(1) amortized | Add to end |
| `list.insert(i, x)` | O(n) | Insert at position |
| `list.remove(x)` | O(n) | Remove first occurrence |
| `list.pop()` | O(1) | Remove from end |
| `list.pop(i)` | O(n) | Remove from position |
| `x in list` | O(n) | Membership testing |
| `list.sort()` | O(n log n) | Sorting |

## Important Interview Questions & Concepts

### 1. List vs Array (NumPy)
```python
# Python list - can store different types
python_list = [1, "hello", 3.14]

# NumPy array - homogeneous, more memory efficient
import numpy as np
numpy_array = np.array([1, 2, 3, 4])  # All same type
```

### 2. Shallow vs Deep Copy
```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy - copies references
shallow = original.copy()  # or list(original) or original[:]
shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] - original affected!

# Deep copy - copies everything
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 999
print(original)  # [[1, 2], [3, 4]] - original not affected
```

### 3. List Mutability Gotchas
```python
# Dangerous default argument
def add_item(item, target_list=[]):  # DON'T DO THIS
    target_list.append(item)
    return target_list

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Unexpected!

# Correct way
def add_item(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

### 4. List Multiplication Pitfall
```python
# Creates references to same list
matrix = [[0] * 3] * 3  # DON'T DO THIS
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - All rows affected!

# Correct way
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]] - Only first row affected
```

## List vs Other Data Structures

### List vs Tuple (Key Differences)
| Feature | List | Tuple |
|---------|------|-------|
| Mutability | Mutable | Immutable |
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Performance | Slower | Faster |
| Memory | More | Less |
| Use Case | Dynamic data | Fixed data |
| Hashable | No | Yes (if elements are hashable) |

### When to Use Lists vs Tuples
```python
# Use list for:
shopping_cart = ["apples", "bananas"]  # Items may change
shopping_cart.append("oranges")

# Use tuple for:
coordinates = (10, 20)  # Fixed point in space
rgb_color = (255, 128, 0)  # Color values don't change
```

## Best Practices

1. **Use list comprehensions** for simple transformations
2. **Prefer `append()` over `+`** for adding single elements
3. **Use `extend()` instead of `+=`** for adding multiple elements in place
4. **Be careful with default mutable arguments**
5. **Consider `collections.deque`** for frequent insertions/deletions at both ends
6. **Use `enumerate()`** when you need both index and value

```python
# Good practices
names = ["Alice", "Bob", "Charlie"]

# Use enumerate for index and value
for i, name in enumerate(names):
    print(f"{i}: {name}")

# Use zip for parallel iteration
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

## Common Pitfalls

1. **Modifying list while iterating**
```python
# Wrong way
numbers = [1, 2, 3, 4, 5]
for i, num in enumerate(numbers):
    if num % 2 == 0:
        numbers.pop(i)  # Can skip elements or cause IndexError

# Right way
numbers = [num for num in numbers if num % 2 != 0]
```

2. **Creating unintended references**
3. **Not understanding list mutability**
4. **Inefficient string concatenation using lists incorrectly**

## Summary

Python lists are:
- **Mutable**: Can be modified after creation
- **Ordered**: Elements maintain their position
- **Versatile**: Support many built-in methods
- **Dynamic**: Can grow and shrink at runtime

Key concepts to remember:
- Indexing and slicing work like strings
- Many methods modify the list in place
- List comprehensions provide elegant syntax
- Understanding shallow vs deep copy is crucial
- Performance characteristics vary by operation
