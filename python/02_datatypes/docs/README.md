# Python Data Types - Complete Documentation

Welcome to the comprehensive guide on Python data types! This documentation covers all the fundamental data types in Python with detailed explanations, examples, and important concepts for interviews and practical programming.

## 📚 Documentation Structure

### 1. [Numbers Complete Guide](./01_Numbers_Complete_Guide.md)
- **Integer (int)**: Unlimited precision whole numbers
- **Float (float)**: IEEE 754 double precision decimals  
- **Complex (complex)**: Numbers with real and imaginary parts
- **Key Topics**: Integer caching, floating point precision, type conversion
- **Interview Concepts**: Memory efficiency, precision handling, arithmetic operations

### 2. [Strings Complete Guide](./02_Strings_Complete_Guide.md)
- **String Operations**: Creation, manipulation, formatting
- **Indexing & Slicing**: Positive/negative indexing, advanced slicing techniques
- **Encoding & Decoding**: UTF-8, ASCII, Unicode handling
- **Key Topics**: Immutability, string methods, f-strings
- **Interview Concepts**: Memory efficiency, encoding issues, string vs bytes

### 3. [Lists Complete Guide](./03_Lists_Complete_Guide.md)
- **List Operations**: Creation, modification, methods
- **Performance**: Time complexity of operations
- **List Comprehensions**: Elegant syntax for transformations
- **Key Topics**: Mutability, dynamic sizing, memory layout
- **Interview Concepts**: Shallow vs deep copy, performance characteristics

### 4. [Tuples Complete Guide](./04_Tuples_Complete_Guide.md)
- **Tuple Operations**: Creation, unpacking, named tuples
- **Immutability**: Benefits and use cases
- **Tuple vs List**: When to choose which
- **Key Topics**: Hashability, memory efficiency, tuple packing/unpacking
- **Interview Concepts**: Single element tuples, as dictionary keys

### 5. [Dictionaries Complete Guide](./05_Dictionaries_Complete_Guide.md)
- **Dictionary Operations**: CRUD operations, methods
- **Advanced Features**: Comprehensions, default dictionaries
- **Performance**: Hash tables, time complexity
- **Key Topics**: Key requirements (hashable), dictionary views
- **Interview Concepts**: vs JavaScript objects, hash collisions

### 6. [Data Types Comparison Guide](./06_Data_Types_Comparison_Guide.md)
- **Side-by-Side Comparisons**: All data types compared
- **Performance Analysis**: Memory usage, time complexity
- **Decision Guide**: When to use which data type
- **Common Pitfalls**: Mistakes to avoid
- **Interview Questions**: Frequently asked concepts

## 🎯 Quick Reference

### Data Type Selection Guide

```python
# Numbers
age = 25                    # int - whole numbers
height = 5.9               # float - decimals
signal = 3 + 4j           # complex - mathematical computations

# Text
name = "Alice"            # str - text data

# Collections
tasks = ["buy milk", "exercise"]        # list - mutable, ordered
coordinates = (10, 20)                  # tuple - immutable, ordered
person = {"name": "Alice", "age": 25}   # dict - key-value mapping
```

### Common Interview Questions

1. **What's the difference between list and tuple?**
   - Lists are mutable, tuples are immutable
   - Tuples are faster and use less memory
   - Tuples can be dictionary keys (if elements are hashable)

2. **Why use dictionaries over lists for lookups?**
   - Dictionary lookup: O(1) average time
   - List search: O(n) time
   - Dictionaries use hash tables for fast access

3. **What are hashable types in Python?**
   - Immutable types: int, float, str, tuple (with hashable elements)
   - Can be used as dictionary keys
   - Mutable types (list, dict) are not hashable

4. **Explain Python's integer caching:**
   - Integers from -5 to 256 are cached (singleton objects)
   - Same object in memory for cached integers
   - Affects `is` vs `==` comparison results

## 💡 Key Concepts to Remember

### Mutability Impact
```python
# Immutable - creates new object
text = "hello"
text = text.upper()  # New string object

# Mutable - modifies existing object  
numbers = [1, 2, 3]
numbers.append(4)    # Same list object, modified
```

### Performance Considerations
```python
# Efficient membership testing
vowels = set("aeiou")          # O(1) lookup
if char in vowels: pass

# Efficient string building
words = ["Hello", "World"]
sentence = " ".join(words)     # Better than += in loop

# Appropriate data structure choice
cache = {}                     # Dict for key-value mapping
items = []                     # List for ordered, changing data
point = (x, y)                # Tuple for fixed coordinates
```

### Common Pitfalls
```python
# 1. Mutable default arguments
def bad_func(items=[]):        # DON'T DO THIS
    items.append("new")
    return items

def good_func(items=None):     # DO THIS
    if items is None:
        items = []
    items.append("new")
    return items

# 2. Shallow vs deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()      # References same inner lists
deep = copy.deepcopy(original) # Completely separate copy

# 3. Dictionary key requirements
valid_key = (1, 2)            # Hashable tuple
# invalid_key = [1, 2]        # List not hashable
```

## 🚀 Advanced Topics

### Memory Optimization
- Use `__slots__` for classes with fixed attributes
- Consider `array.array` for homogeneous numeric data
- Use generators for large datasets

### Performance Profiling
```python
import sys
import time

# Memory usage
data = [1, 2, 3, 4, 5]
print(sys.getsizeof(data))

# Timing operations
start = time.time()
# Your operation here
duration = time.time() - start
```

### Type Hints (Modern Python)
```python
from typing import List, Dict, Tuple, Optional

def process_data(
    numbers: List[int], 
    mapping: Dict[str, int],
    coordinates: Tuple[float, float]
) -> Optional[str]:
    # Function implementation
    pass
```

## 📖 How to Use This Documentation

1. **Learning Path**: Start with Numbers → Strings → Lists → Tuples → Dictionaries
2. **Interview Prep**: Focus on comparison guide and key concepts
3. **Quick Reference**: Use for syntax and method lookups
4. **Deep Dive**: Read individual guides for comprehensive understanding

## 🔗 Related Topics

- **Collections Module**: `defaultdict`, `Counter`, `namedtuple`
- **Type System**: Type hints, `typing` module
- **Performance**: Profiling, optimization techniques
- **Memory Management**: Garbage collection, reference counting

---

*This documentation is designed to be a comprehensive reference for Python data types. Whether you're preparing for interviews, learning Python, or need a quick reference, these guides cover everything you need to know about Python's fundamental data structures.*
