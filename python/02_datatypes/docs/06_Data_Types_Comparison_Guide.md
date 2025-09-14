# Python Data Types Comparison Guide

## Quick Reference Table

| Data Type | Mutable | Ordered | Indexed | Allows Duplicates | Hashable | Syntax |
|-----------|---------|---------|---------|-------------------|----------|--------|
| **int** | No | N/A | N/A | N/A | Yes | `42` |
| **float** | No | N/A | N/A | N/A | Yes | `3.14` |
| **complex** | No | N/A | N/A | N/A | Yes | `3+4j` |
| **str** | No | Yes | Yes | Yes | Yes | `"hello"` |
| **list** | Yes | Yes | Yes | Yes | No | `[1, 2, 3]` |
| **tuple** | No | Yes | Yes | Yes | Yes* | `(1, 2, 3)` |
| **dict** | Yes | Yes** | No | No (keys) | No | `{"key": "value"}` |

*Hashable if all elements are hashable  
**Insertion order preserved since Python 3.7

## Detailed Comparisons

### Numbers (int, float, complex)

#### When to Use Each
```python
# int - for counting, indexing, exact arithmetic
count = 42
index = 0
exact_result = 10 // 3  # 3 (exact division)

# float - for measurements, scientific calculations
height = 5.9
pi = 3.14159
temperature = 98.6

# complex - for mathematical computations
impedance = 3 + 4j
signal = 2.5 + 1.8j
```

#### Key Differences
```python
# Precision differences
print(0.1 + 0.2)        # 0.30000000000000004 (float precision issue)
print(1/3)              # 0.3333333333333333 (limited precision)

# Integer unlimited precision
big_int = 10**100       # Works fine in Python
# big_float = 10.0**308  # May overflow to inf

# Type conversion behavior
print(5 + 3.0)          # 8.0 (int + float = float)
print(2 + 3j)           # (2+3j) (int + complex = complex)
```

### String vs List vs Tuple

#### Mutability Comparison
```python
# String - immutable
text = "hello"
# text[0] = 'H'  # TypeError!
text = text.upper()  # Creates new string

# List - mutable
numbers = [1, 2, 3]
numbers[0] = 10      # [10, 2, 3] - modifies original
numbers.append(4)    # [10, 2, 3, 4]

# Tuple - immutable
coordinates = (10, 20)
# coordinates[0] = 15  # TypeError!
coordinates = (15, 20)  # Creates new tuple
```

#### Performance Comparison
```python
import time

# Creation time
start = time.time()
for _ in range(100000):
    data = [1, 2, 3, 4, 5]  # List creation
list_time = time.time() - start

start = time.time()
for _ in range(100000):
    data = (1, 2, 3, 4, 5)  # Tuple creation
tuple_time = time.time() - start

print(f"List creation: {list_time}")
print(f"Tuple creation: {tuple_time}")  # Faster

# Memory usage
import sys
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)
string_data = "12345"

print(f"List size: {sys.getsizeof(list_data)}")
print(f"Tuple size: {sys.getsizeof(tuple_data)}")    # Smaller
print(f"String size: {sys.getsizeof(string_data)}")  # Smallest
```

### List vs Tuple - Detailed Comparison

#### Functional Differences
```python
# List methods (many available)
my_list = [1, 2, 3]
my_list.append(4)       # Modify in place
my_list.extend([5, 6])  # Add multiple elements
my_list.sort()          # Sort in place
my_list.reverse()       # Reverse in place
my_list.insert(0, 0)    # Insert at position
my_list.remove(2)       # Remove first occurrence
popped = my_list.pop()  # Remove and return last element

# Tuple methods (only 2 available)
my_tuple = (1, 2, 3, 2, 4)
count = my_tuple.count(2)    # Count occurrences
index = my_tuple.index(3)    # Find index
# That's it! No modification methods
```

#### Use Case Guidelines
```python
# Use List when:
shopping_cart = ["apples", "bananas"]  # Items can be added/removed
scores = [85, 90, 78, 92]              # Scores can be updated
tasks = []                             # Empty, will be populated

# Use Tuple when:
coordinates = (10, 20)                 # Fixed point
rgb_color = (255, 128, 0)              # Color values don't change
database_record = ("Alice", 25, "Engineer")  # Fixed record structure

def get_name_age():
    return "Bob", 30  # Multiple return values (tuple)

name, age = get_name_age()  # Tuple unpacking
```

### Dictionary vs Other Structures

#### Dictionary vs List for Lookups
```python
# List lookup - O(n) time complexity
employees_list = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Finding employee by ID (slow for large lists)
def find_employee_list(emp_id):
    for emp in employees_list:
        if emp["id"] == emp_id:
            return emp
    return None

# Dictionary lookup - O(1) time complexity
employees_dict = {
    1: {"name": "Alice"},
    2: {"name": "Bob"},
    3: {"name": "Charlie"}
}

# Finding employee by ID (fast)
def find_employee_dict(emp_id):
    return employees_dict.get(emp_id)
```

#### Python Dictionary vs JavaScript Object
```python
# Python Dictionary
python_data = {
    "name": "Alice",
    "age": 30,
    123: "numeric key",      # Non-string keys allowed
    (1, 2): "tuple key",     # Complex keys allowed
    None: "null key"         # None as key
}

# Access patterns
name = python_data["name"]           # Bracket notation
name = python_data.get("name")       # Safe access with default
exists = "age" in python_data        # Membership testing

# JavaScript Object (conceptual comparison)
"""
const jsData = {
    "name": "Alice",
    "age": 30,
    "123": "numeric key",    // All keys converted to strings
    // No tuple equivalent
    // undefined/null handling different
};

// Access patterns
const name = jsData.name;            // Dot notation
const name = jsData["name"];         // Bracket notation
const exists = "age" in jsData;      // Membership testing
"""
```

## Memory and Performance Summary

### Memory Usage (Typical)
```python
import sys

# Memory comparison for same data
data = [1, 2, 3, 4, 5]

string_version = "12345"
list_version = [1, 2, 3, 4, 5]
tuple_version = (1, 2, 3, 4, 5)
dict_version = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

print(f"String: {sys.getsizeof(string_version)} bytes")  # Smallest
print(f"Tuple:  {sys.getsizeof(tuple_version)} bytes")   # Small
print(f"List:   {sys.getsizeof(list_version)} bytes")    # Medium
print(f"Dict:   {sys.getsizeof(dict_version)} bytes")    # Largest
```

### Performance Characteristics
| Operation | String | List | Tuple | Dict |
|-----------|--------|------|-------|------|
| **Creation** | Fast | Medium | Fast | Medium |
| **Access by index** | O(1) | O(1) | O(1) | N/A |
| **Access by key** | N/A | N/A | N/A | O(1) avg |
| **Search element** | O(n) | O(n) | O(n) | O(1) avg |
| **Append/Add** | O(n)* | O(1) amortized | N/A | O(1) avg |
| **Insert middle** | O(n)* | O(n) | N/A | N/A |
| **Delete** | O(n)* | O(n) | N/A | O(1) avg |

*Creates new object due to immutability

## Interview Questions & Concepts

### 1. When to Choose Which Data Type?

**Decision Tree:**
```
Need to store numbers?
├─ Whole numbers → int
├─ Decimals → float
└─ Complex math → complex

Need to store text?
└─ Always use str

Need ordered collection?
├─ Will it change?
│  ├─ Yes → list
│  └─ No → tuple
└─ Need fast lookups? → dict

Need key-value mapping?
└─ Always use dict
```

### 2. Mutability Impact on Function Parameters
```python
def modify_data(num, text, lst, tpl, dct):
    num += 1      # No effect on original (immutable)
    text += "!"   # No effect on original (immutable)
    lst.append(4) # Modifies original (mutable)
    # tpl += (4,)  # No effect on original (immutable)
    dct["new"] = "value"  # Modifies original (mutable)

# Example
number = 10
string = "hello"
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {"key": "value"}

modify_data(number, string, my_list, my_tuple, my_dict)

print(number)    # 10 (unchanged)
print(string)    # "hello" (unchanged)
print(my_list)   # [1, 2, 3, 4] (changed!)
print(my_tuple)  # (1, 2, 3) (unchanged)
print(my_dict)   # {"key": "value", "new": "value"} (changed!)
```

### 3. Hashability and Dictionary Keys
```python
# Valid dictionary keys (hashable)
valid_keys = {
    "string": 1,
    42: 2,
    3.14: 3,
    (1, 2): 4,              # Tuple with hashable elements
    frozenset([1, 2]): 5,   # Frozen set
    True: 6,                # Boolean
    None: 7                 # None
}

# Invalid dictionary keys (unhashable)
invalid_examples = [
    # {[1, 2]: "list"},        # TypeError: unhashable type: 'list'
    # {{"a": 1}: "dict"},      # TypeError: unhashable type: 'dict'
    # {set([1, 2]): "set"},    # TypeError: unhashable type: 'set'
    # {([1, [2]]): "mixed"},   # TypeError: unhashable type: 'list'
]

# Mixed tuple (partially hashable)
# mixed_tuple = (1, [2, 3])  # Contains list
# bad_dict = {mixed_tuple: "value"}  # TypeError!
```

### 4. Common Gotchas and Pitfalls

#### List/Dict as Default Parameters
```python
# Wrong way
def add_item(item, container=[]):  # Mutable default!
    container.append(item)
    return container

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Unexpected!

# Right way
def add_item(item, container=None):
    if container is None:
        container = []
    container.append(item)
    return container
```

#### Shallow vs Deep Copy
```python
import copy

# Original with nested structure
original = {"users": ["Alice", "Bob"], "settings": {"theme": "dark"}}

# Shallow copy
shallow = original.copy()
shallow["users"].append("Charlie")  # Affects original!
print(original)  # {"users": ["Alice", "Bob", "Charlie"], ...}

# Deep copy
original = {"users": ["Alice", "Bob"], "settings": {"theme": "dark"}}
deep = copy.deepcopy(original)
deep["users"].append("David")  # Doesn't affect original
print(original)  # {"users": ["Alice", "Bob"], ...}
```

## Best Practices Summary

### 1. Choose the Right Data Type
```python
# Use int for counting, indexing
for i in range(len(items)):  # i is int
    count += 1

# Use float for measurements
height = 5.9
weight = 150.5

# Use string for text
name = "Alice"
message = f"Hello, {name}!"

# Use list for changing collections
tasks = ["task1", "task2"]
tasks.append("task3")

# Use tuple for fixed data
coordinates = (10, 20)
rgb = (255, 128, 0)

# Use dict for mappings
person = {"name": "Alice", "age": 30}
cache = {}
```

### 2. Performance Considerations
```python
# Fast membership testing
vowels_set = set("aeiou")      # O(1) lookup
if char in vowels_set:         # Fast

# Efficient string building
parts = ["Hello", " ", "World"]
message = "".join(parts)       # Efficient

# Appropriate data structure for use case
# Use dict for key-based lookup
# Use list for ordered, changing data
# Use tuple for ordered, fixed data
```

### 3. Memory Efficiency
```python
# Use generator expressions for large datasets
squares = (x**2 for x in range(1000000))  # Memory efficient

# Use appropriate precision
from decimal import Decimal
price = Decimal('19.99')  # For financial calculations

# Consider tuple over list when data doesn't change
fixed_colors = ("red", "green", "blue")  # More memory efficient
```

## Summary

Understanding Python data types is crucial for:
- **Writing efficient code**: Choose the right tool for the job
- **Avoiding bugs**: Understand mutability implications
- **Performance optimization**: Know time/space complexity
- **Interview success**: Common questions about data structures

Key takeaways:
- **Immutable types** (int, float, str, tuple): Safe to pass around, can be dictionary keys
- **Mutable types** (list, dict): Be careful with side effects, cannot be dictionary keys
- **Performance matters**: Dictionary lookup is O(1), list search is O(n)
- **Memory efficiency**: Tuples use less memory than lists
- **Type conversion**: Python handles automatic promotion (int → float → complex)
