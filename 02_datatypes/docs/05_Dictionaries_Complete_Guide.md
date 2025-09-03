# Python Dictionaries - Complete Guide

## Overview
Dictionaries are unordered (Python 3.7+ maintains insertion order), mutable collections of key-value pairs. They are one of the most powerful and frequently used data structures in Python, providing fast lookup, insertion, and deletion operations.

## Dictionary Basics

### Definition & Creation
```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with initial values
person = {"name": "Alice", "age": 30, "city": "New York"}
mixed = {1: "one", "2": 2, 3.0: "three"}  # Mixed key types

# Using dict() constructor
person = dict(name="Alice", age=30, city="New York")
from_tuples = dict([("a", 1), ("b", 2), ("c", 3)])

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Key Characteristics
- **Key-Value Pairs**: Maps keys to values
- **Mutable**: Can be modified after creation
- **Unordered**: No guaranteed order (but insertion order preserved in Python 3.7+)
- **Keys Must Be Hashable**: Immutable types only (strings, numbers, tuples)
- **Values Can Be Any Type**: Including other dictionaries
- **No Duplicate Keys**: Each key is unique

## Dictionary Operations

### Accessing Values
```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Direct access (raises KeyError if key doesn't exist)
name = person["name"]        # "Alice"
# age = person["height"]     # KeyError!

# Using get() method (returns None or default if key doesn't exist)
age = person.get("age")      # 30
height = person.get("height")  # None
height = person.get("height", 0)  # 0 (default value)

# Check if key exists
if "age" in person:
    print(person["age"])

print("salary" in person)    # False
print("name" not in person)  # False
```

### Adding & Modifying Values
```python
person = {"name": "Alice", "age": 30}

# Add new key-value pair
person["city"] = "New York"     # {"name": "Alice", "age": 30, "city": "New York"}

# Modify existing value
person["age"] = 31              # {"name": "Alice", "age": 31, "city": "New York"}

# Update multiple values
person.update({"salary": 75000, "department": "Engineering"})
person.update([("bonus", 5000), ("level", "Senior")])  # From list of tuples
person.update(experience=5, skills=["Python", "SQL"])   # Keyword arguments
```

### Removing Elements
```python
person = {"name": "Alice", "age": 30, "city": "New York", "salary": 75000}

# del statement - removes key-value pair
del person["salary"]

# pop() - removes and returns value
age = person.pop("age")         # Returns 30, removes from dict
dept = person.pop("department", "Unknown")  # Returns default if key not found

# popitem() - removes and returns last inserted key-value pair (Python 3.7+)
last_item = person.popitem()    # Returns ("city", "New York")

# clear() - removes all elements
person.clear()                  # {}
```

## Dictionary Methods

### Keys, Values, and Items
```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys
keys = person.keys()          # dict_keys(['name', 'age', 'city'])
key_list = list(person.keys())  # ['name', 'age', 'city']

# Get all values
values = person.values()      # dict_values(['Alice', 30, 'New York'])
value_list = list(person.values())  # ['Alice', 30, 'New York']

# Get all key-value pairs
items = person.items()        # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
item_list = list(person.items())  # [('name', 'Alice'), ('age', 30), ('city', 'New York')]
```

### Copying Dictionaries
```python
original = {"a": 1, "b": [2, 3], "c": {"nested": 4}}

# Shallow copy
shallow = original.copy()
shallow = dict(original)
shallow = {**original}  # Dictionary unpacking

# Deep copy
import copy
deep = copy.deepcopy(original)

# Difference demonstration
shallow["b"].append(99)
print(original["b"])  # [2, 3, 99] - original affected!

deep = copy.deepcopy(original)
deep["b"].append(100)
print(original["b"])  # [2, 3, 99] - original not affected
```

## Advanced Dictionary Features

### Dictionary Comprehensions
```python
# Basic comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# From two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}

# Transform existing dictionary
person = {"name": "alice", "city": "new york"}
upper_person = {k: v.upper() if isinstance(v, str) else v for k, v in person.items()}
```

### Nested Dictionaries
```python
# Nested dictionary
company = {
    "employees": {
        "alice": {"age": 30, "department": "Engineering"},
        "bob": {"age": 25, "department": "Sales"}
    },
    "departments": {
        "Engineering": {"budget": 100000, "head": "alice"},
        "Sales": {"budget": 75000, "head": "charlie"}
    }
}

# Accessing nested values
alice_age = company["employees"]["alice"]["age"]  # 30

# Safe nested access
def safe_get(d, *keys):
    for key in keys:
        try:
            d = d[key]
        except (KeyError, TypeError):
            return None
    return d

age = safe_get(company, "employees", "alice", "age")  # 30
missing = safe_get(company, "employees", "david", "age")  # None
```

### Default Dictionaries
```python
from collections import defaultdict

# Regular dictionary - KeyError for missing keys
regular_dict = {}
# regular_dict["missing"].append(1)  # KeyError!

# defaultdict with list
dd_list = defaultdict(list)
dd_list["fruits"].append("apple")     # Creates list automatically
dd_list["fruits"].append("banana")
print(dd_list)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

# defaultdict with int (useful for counting)
dd_counter = defaultdict(int)
text = "hello world"
for char in text:
    dd_counter[char] += 1
print(dd_counter)  # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 3, ...})

# defaultdict with custom factory
def default_value():
    return "Unknown"

dd_custom = defaultdict(default_value)
print(dd_custom["missing"])  # "Unknown"
```

## Dictionary Performance

### Time Complexity
| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| `dict[key]` | O(1) | O(n) | Hash collision dependent |
| `dict[key] = value` | O(1) | O(n) | Assignment |
| `del dict[key]` | O(1) | O(n) | Deletion |
| `key in dict` | O(1) | O(n) | Membership testing |
| `len(dict)` | O(1) | O(1) | Length |
| `dict.items()` | O(n) | O(n) | All items |

### Memory Efficiency
```python
import sys

# Dictionary memory usage
small_dict = {"a": 1, "b": 2}
large_dict = {str(i): i for i in range(1000)}

print(sys.getsizeof(small_dict))
print(sys.getsizeof(large_dict))

# Over-allocation for performance
# Dictionaries allocate extra space to minimize hash collisions
```

## Important Interview Questions & Concepts

### 1. Dictionary vs List Performance
```python
# Finding element in list vs dictionary
import time

# List lookup - O(n)
large_list = list(range(100000))
start = time.time()
99999 in large_list
list_time = time.time() - start

# Dictionary lookup - O(1) average
large_dict = {i: i for i in range(100000)}
start = time.time()
99999 in large_dict
dict_time = time.time() - start

print(f"List time: {list_time}")
print(f"Dict time: {dict_time}")  # Much faster!
```

### 2. Hashable Keys Requirement
```python
# Valid hashable keys
valid_dict = {
    "string": 1,
    42: 2,
    (1, 2): 3,           # Tuple (if all elements are hashable)
    frozenset([1, 2]): 4  # Frozen set
}

# Invalid keys (not hashable)
invalid_examples = [
    # {[1, 2]: "list"},      # TypeError: unhashable type: 'list'
    # {{1: 2}: "dict"},      # TypeError: unhashable type: 'dict'
    # {set([1, 2]): "set"}   # TypeError: unhashable type: 'set'
]
```

### 3. Dictionary Iteration Patterns
```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Iterate over keys (default)
for key in person:
    print(key, person[key])

# Iterate over keys explicitly
for key in person.keys():
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs (most common)
for key, value in person.items():
    print(f"{key}: {value}")
```

### 4. Dictionary Merging (Python 3.5+)
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"a": 10, "e": 5}  # Note: 'a' conflicts with dict1

# Dictionary unpacking (Python 3.5+)
merged = {**dict1, **dict2, **dict3}  # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Union operator (Python 3.9+)
# merged = dict1 | dict2 | dict3

# Update method (modifies original)
dict1.update(dict2)
```

## Dictionary vs Other Languages

### Python Dictionary vs JavaScript Object
| Feature | Python Dict | JavaScript Object |
|---------|-------------|-------------------|
| **Syntax** | `{"key": "value"}` | `{"key": "value"}` or `{key: "value"}` |
| **Key Types** | Any hashable type | Strings and Symbols only |
| **Ordering** | Insertion order (3.7+) | Insertion order (mostly) |
| **Size** | `len(dict)` | `Object.keys(obj).length` |
| **Membership** | `key in dict` | `"key" in obj` or `obj.hasOwnProperty("key")` |
| **Iteration** | `for k, v in dict.items()` | `for (const [k, v] of Object.entries(obj))` |
| **Method Access** | `dict.get(key)` | `obj.key` or `obj["key"]` |

```python
# Python dictionary
python_dict = {
    "name": "Alice",
    "age": 30,
    123: "number key",  # Any hashable type as key
    (1, 2): "tuple key"
}

# JavaScript equivalent (conceptual)
"""
const jsObject = {
    "name": "Alice",
    "age": 30,
    "123": "number key",     // Keys are always strings
    // "(1,2)": "tuple key"  // No tuple equivalent
};
"""
```

### Dictionary vs Hash Map (Java)
| Feature | Python Dict | Java HashMap |
|---------|-------------|--------------|
| **Type Safety** | Dynamic | Static (generics) |
| **Null Values** | Allowed | Allowed |
| **Null Keys** | No (None is valid key) | One null key allowed |
| **Thread Safety** | No | No (use ConcurrentHashMap) |
| **Ordering** | Insertion order | No guarantee |

## Best Practices

1. **Use `get()` method** for safe key access
2. **Use dictionary comprehensions** for transformations
3. **Use `setdefault()`** for initialization
4. **Be careful with mutable default values**
5. **Use `collections.defaultdict`** when appropriate

```python
# Good practices

# 1. Safe key access
value = person.get("age", 0)  # Better than person["age"]

# 2. Dictionary comprehension
squared = {x: x**2 for x in range(5)}

# 3. setdefault for initialization
word_count = {}
for word in ["apple", "banana", "apple"]:
    word_count.setdefault(word, 0)
    word_count[word] += 1

# 4. Avoid mutable defaults
def process_data(data, cache=None):
    if cache is None:
        cache = {}
    # Use cache...

# 5. Use defaultdict when appropriate
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)
```

## Common Pitfalls

1. **KeyError when accessing non-existent keys**
2. **Modifying dictionary while iterating**
3. **Using mutable objects as keys**
4. **Not understanding dictionary view objects**

```python
# Pitfall examples

# 1. KeyError
person = {"name": "Alice"}
# age = person["age"]  # KeyError!
age = person.get("age", 0)  # Safe

# 2. Modifying while iterating
data = {"a": 1, "b": 2, "c": 3}
# for key in data:
#     if data[key] > 1:
#         del data[key]  # RuntimeError!

# Correct way
data = {k: v for k, v in data.items() if v <= 1}

# 3. Mutable keys
# bad_dict = {[1, 2]: "value"}  # TypeError!
good_dict = {(1, 2): "value"}   # OK

# 4. View objects
keys = person.keys()
person["age"] = 30
print(list(keys))  # Shows updated keys! Views are dynamic
```

## Advanced Use Cases

### Dictionary as Switch Statement
```python
def calculate(operation, x, y):
    operations = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: a / b if b != 0 else None
    }
    return operations.get(operation, lambda a, b: None)(x, y)

result = calculate("add", 5, 3)  # 8
```

### Caching/Memoization
```python
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]
```

### Grouping Data
```python
from collections import defaultdict

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "B"}
]

# Group by grade
by_grade = defaultdict(list)
for student in students:
    by_grade[student["grade"]].append(student["name"])

print(dict(by_grade))  # {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'David']}
```

## Summary

Python dictionaries are:
- **Key-Value Store**: Maps keys to values
- **Mutable**: Can be modified after creation
- **Fast**: O(1) average time for basic operations
- **Flexible**: Values can be any type, keys must be hashable
- **Ordered**: Insertion order preserved (Python 3.7+)

Key concepts to remember:
- Use appropriate key types (hashable only)
- Understand the difference between `dict[key]` and `dict.get(key)`
- Dictionary views (keys(), values(), items()) are dynamic
- Performance characteristics make them ideal for lookups
- Comprehensions provide elegant creation syntax
- Integration with other Python features (unpacking, iteration, etc.)
