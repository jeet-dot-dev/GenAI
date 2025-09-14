# Python Comprehensions Complete Guide 🐍

## Table of Contents
1. [Introduction to Comprehensions](#introduction-to-comprehensions)
2. [Why Use Comprehensions?](#why-use-comprehensions)
3. [Comprehensions vs Loops](#comprehensions-vs-loops)
4. [Types of Comprehensions](#types-of-comprehensions)
5. [List Comprehensions](#list-comprehensions)
6. [Set Comprehensions](#set-comprehensions)
7. [Dictionary Comprehensions](#dictionary-comprehensions)
8. [Generator Expressions](#generator-expressions)
9. [Advanced Techniques](#advanced-techniques)
10. [Performance Comparison](#performance-comparison)
11. [Best Practices](#best-practices)
12. [Common Pitfalls](#common-pitfalls)

---

## Introduction to Comprehensions

**Comprehensions** are a concise and elegant way to create collections (lists, sets, dictionaries) and generators in Python. They provide a more readable and often faster alternative to traditional loops for creating collections.

### Basic Syntax Pattern
```python
[expression for item in iterable if condition]
```

**Components:**
- **expression**: What to include in the result
- **for clause**: Iteration over an iterable
- **if clause**: Optional filtering condition

---

## Why Use Comprehensions?

### 1. **Readability and Conciseness**
- More expressive and closer to natural language
- Reduces code from 3-4 lines to a single line
- Makes intent clearer

### 2. **Performance Benefits**
- Generally faster than equivalent loops
- Optimized at the C level in CPython
- Less function call overhead

### 3. **Functional Programming Style**
- Encourages immutable programming patterns
- Reduces side effects
- More declarative approach

### 4. **Memory Efficiency** (for generators)
- Lazy evaluation for generator expressions
- Lower memory footprint for large datasets

---

## Comprehensions vs Loops

### Traditional Loop Approach
```python
# Creating a list of squares
squares = []
for x in range(10):
    squares.append(x**2)
```

### Comprehension Approach
```python
# Same result, more concise
squares = [x**2 for x in range(10)]
```

### Key Differences

| Aspect | Loops | Comprehensions |
|--------|-------|----------------|
| **Lines of Code** | 3-4 lines | 1 line |
| **Readability** | More verbose | More concise |
| **Performance** | Slower (function calls) | Faster (optimized) |
| **Debugging** | Easier to debug step-by-step | Harder to debug |
| **Complexity** | Better for complex logic | Best for simple transformations |
| **Memory Usage** | Creates intermediate variables | More memory efficient |

---

## Types of Comprehensions

Python supports four types of comprehensions:

1. **List Comprehensions** `[...]`
2. **Set Comprehensions** `{...}`
3. **Dictionary Comprehensions** `{key: value ...}`
4. **Generator Expressions** `(...)`

---

## List Comprehensions

### Basic Syntax
```python
[expression for item in iterable if condition]
```

### Simple Examples

#### 1. Basic Transformation
```python
# Squares of numbers
squares = [x**2 for x in range(1, 6)]
# Result: [1, 4, 9, 16, 25]
```

#### 2. String Operations
```python
# Convert to uppercase
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
# Result: ['HELLO', 'WORLD', 'PYTHON']
```

#### 3. With Conditional Filtering
```python
# Even numbers only
evens = [x for x in range(20) if x % 2 == 0]
# Result: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

#### 4. Conditional Expression
```python
# Positive or negative labels
numbers = [-2, -1, 0, 1, 2]
labels = ['positive' if x > 0 else 'negative' if x < 0 else 'zero' for x in numbers]
# Result: ['negative', 'negative', 'zero', 'positive', 'positive']
```

### Advanced List Comprehensions

#### 1. Nested Loops
```python
# Cartesian product
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
# Result: [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

#### 2. Flattening Lists
```python
# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 3. Working with Functions
```python
# Apply function to each element
def square_if_even(x):
    return x**2 if x % 2 == 0 else x

numbers = [1, 2, 3, 4, 5, 6]
result = [square_if_even(x) for x in numbers]
# Result: [1, 4, 3, 16, 5, 36]
```

---

## Set Comprehensions

### Basic Syntax
```python
{expression for item in iterable if condition}
```

### Examples

#### 1. Unique Values
```python
# Remove duplicates and transform
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_squares = {x**2 for x in numbers}
# Result: {1, 4, 9, 16, 25}
```

#### 2. String Processing
```python
# Unique first letters
words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']
first_letters = {word[0].upper() for word in words}
# Result: {'A', 'B', 'C'}
```

#### 3. Complex Filtering
```python
# Prime numbers (simplified check)
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primes = {x for x in range(2, 50) if is_prime(x)}
# Result: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
```

---

## Dictionary Comprehensions

### Basic Syntax
```python
{key_expression: value_expression for item in iterable if condition}
```

### Examples

#### 1. Basic Key-Value Creation
```python
# Numbers and their squares
squares_dict = {x: x**2 for x in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### 2. String to Length Mapping
```python
words = ['python', 'java', 'javascript', 'go']
word_lengths = {word: len(word) for word in words}
# Result: {'python': 6, 'java': 4, 'javascript': 10, 'go': 2}
```

#### 3. Dictionary Inversion
```python
# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {value: key for key, value in original.items()}
# Result: {1: 'a', 2: 'b', 3: 'c'}
```

#### 4. Filtering Dictionary
```python
# Filter by condition
prices = {'apple': 2.5, 'banana': 1.2, 'cherry': 8.0, 'date': 12.0}
expensive = {fruit: price for fruit, price in prices.items() if price > 5}
# Result: {'cherry': 8.0, 'date': 12.0}
```

#### 5. Nested Dictionary Processing
```python
# Process nested data
students = {
    'alice': {'math': 85, 'science': 92},
    'bob': {'math': 78, 'science': 88},
    'charlie': {'math': 95, 'science': 87}
}
averages = {name: sum(scores.values()) / len(scores) for name, scores in students.items()}
# Result: {'alice': 88.5, 'bob': 83.0, 'charlie': 91.0}
```

---

## Generator Expressions

### Basic Syntax
```python
(expression for item in iterable if condition)
```

### Key Characteristics
- **Lazy evaluation**: Values computed on demand
- **Memory efficient**: Don't store all values in memory
- **One-time iteration**: Can only be consumed once

### Examples

#### 1. Basic Generator
```python
# Memory-efficient squares
squares_gen = (x**2 for x in range(1000000))
# No memory allocated until values are requested
```

#### 2. File Processing
```python
# Read large file efficiently
def process_large_file(filename):
    return (line.strip().upper() for line in open(filename) if line.strip())
```

#### 3. Infinite Sequences
```python
# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Use with comprehension
fib_gen = (x for x in fibonacci() if x % 2 == 0)  # Even Fibonacci numbers
```

#### 4. Chaining Generators
```python
# Pipeline processing
numbers = range(1000)
evens = (x for x in numbers if x % 2 == 0)
squares = (x**2 for x in evens)
filtered = (x for x in squares if x > 100)
```

---

## Advanced Techniques

### 1. Nested Comprehensions
```python
# 2D matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# Result: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### 2. Multiple Conditions
```python
# Multiple filtering conditions
numbers = range(1, 100)
special = [x for x in numbers if x % 3 == 0 if x % 5 == 0 if x > 20]
# Numbers divisible by both 3 and 5, and greater than 20
```

### 3. Walrus Operator (Python 3.8+)
```python
# Assignment within comprehension
def expensive_function(x):
    return x**3 + x**2 + x

# Avoid calling expensive_function twice
results = [(x, result) for x in range(10) if (result := expensive_function(x)) > 100]
```

### 4. Comprehensions with enumerate()
```python
# Index and value together
items = ['a', 'b', 'c', 'd', 'e']
indexed = {i: item.upper() for i, item in enumerate(items) if i % 2 == 0}
# Result: {0: 'A', 2: 'C', 4: 'E'}
```

---

## Performance Comparison

### Timing Example
```python
import timeit

# Traditional loop
def traditional_loop():
    result = []
    for i in range(1000):
        result.append(i**2)
    return result

# List comprehension
def list_comp():
    return [i**2 for i in range(1000)]

# Generator expression
def gen_expr():
    return (i**2 for i in range(1000))

# Performance results (approximate):
# List comprehension: ~40% faster than traditional loop
# Generator expression: Fastest for one-time iteration
```

### Memory Usage Comparison
```python
import sys

# List comprehension - stores all values
list_comp = [x for x in range(1000)]
print(f"List size: {sys.getsizeof(list_comp)} bytes")

# Generator expression - minimal memory
gen_expr = (x for x in range(1000))
print(f"Generator size: {sys.getsizeof(gen_expr)} bytes")
```

---

## Best Practices

### 1. **Keep It Simple**
```python
# Good: Simple and readable
evens = [x for x in numbers if x % 2 == 0]

# Avoid: Too complex for comprehension
# Instead use regular loop for complex logic
```

### 2. **Use Appropriate Type**
```python
# Use set for unique values
unique_items = {process(item) for item in data}

# Use generator for large datasets
processed_data = (heavy_process(item) for item in huge_dataset)
```

### 3. **Meaningful Variable Names**
```python
# Good
valid_emails = [email for email in email_list if is_valid(email)]

# Avoid
result = [x for x in data if check(x)]
```

### 4. **Consider Readability**
```python
# If comprehension becomes too long, use regular loop
# Or break into multiple steps
```

---

## Common Pitfalls

### 1. **Modifying List During Iteration**
```python
# Don't do this
items = [1, 2, 3, 4, 5]
# filtered = [x for x in items if not items.remove(x)]  # Wrong!

# Do this instead
filtered = [x for x in items if condition(x)]
```

### 2. **Late Binding in Loops**
```python
# Pitfall with functions in comprehension
# funcs = [(lambda: i) for i in range(5)]  # All return 4!

# Correct way
funcs = [(lambda x=i: x) for i in range(5)]  # Each returns correct value
```

### 3. **Generator Exhaustion**
```python
# Generators can only be consumed once
gen = (x**2 for x in range(5))
list1 = list(gen)  # [0, 1, 4, 9, 16]
list2 = list(gen)  # [] - empty! Generator exhausted
```

### 4. **Unnecessary Comprehensions**
```python
# Don't use comprehension for simple existence check
# found = any([x > 10 for x in numbers])  # Creates unnecessary list

# Better
found = any(x > 10 for x in numbers)  # Uses generator
```

---

## When to Use Each Type

### Use List Comprehension When:
- Need to store all results
- Small to medium datasets
- Need to iterate multiple times
- Need indexing or slicing

### Use Set Comprehension When:
- Need unique values only
- Order doesn't matter
- Want to eliminate duplicates

### Use Dictionary Comprehension When:
- Creating mappings
- Transforming existing dictionaries
- Need key-value relationships

### Use Generator Expression When:
- Large datasets
- Memory is a concern
- One-time iteration
- Pipeline processing
- Working with files or streams

---

## Summary

Comprehensions are a powerful Python feature that make code more readable, concise, and often more efficient. They're particularly useful for:

- **Data transformation and filtering**
- **Creating collections from other iterables**
- **Functional programming patterns**
- **Memory-efficient processing**

Master comprehensions to write more Pythonic and efficient code! 🚀

---

*This guide covers the essential concepts and practical applications of Python comprehensions. Practice with different examples to become proficient in using them effectively.*
