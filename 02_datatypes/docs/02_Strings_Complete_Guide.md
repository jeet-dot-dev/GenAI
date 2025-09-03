# Python Strings - Complete Guide

## Overview
Strings in Python are sequences of Unicode characters, immutable, and one of the most frequently used data types. Understanding string operations, indexing, slicing, and encoding is crucial for text processing.

## String Basics

### Definition & Creation
```python
# Different ways to create strings
single_quote = 'Hello World'
double_quote = "Hello World"
triple_quote = """Multi-line
string example"""
raw_string = r"C:\Users\name"  # Raw string (ignores escape characters)
```

### String Immutability
```python
# Strings are immutable - cannot be changed in place
text = "Hello"
# text[0] = 'h'  # This would raise TypeError
text = text.lower()  # Creates new string, doesn't modify original
```

## String Indexing

### Positive Indexing (Left to Right)
```python
text = "Python"
#       012345
print(text[0])   # 'P' (first character)
print(text[5])   # 'n' (last character)
```

### Negative Indexing (Right to Left)
```python
text = "Python"
#      -654321
print(text[-1])  # 'n' (last character)
print(text[-6])  # 'P' (first character)
```

### Index Out of Range
```python
text = "Hello"
# print(text[10])  # IndexError: string index out of range
```

## String Slicing

### Basic Slicing Syntax: `string[start:stop:step]`

```python
text = "Python Programming"

# Basic slicing
print(text[0:6])    # "Python" (start to stop-1)
print(text[:6])     # "Python" (beginning to stop-1)
print(text[7:])     # "Programming" (start to end)
print(text[:])      # "Python Programming" (entire string)

# Negative slicing
print(text[-11:])   # "Programming" (from -11 to end)
print(text[:-12])   # "Python" (from start to -12)

# Step slicing
print(text[::2])    # "Pto rgamn" (every 2nd character)
print(text[::-1])   # "gnimmargorP nohtyP" (reverse string)
```

### Advanced Slicing Examples
```python
text = "Hello World"

# Get every other character
print(text[1::2])   # "el ol"

# Reverse slicing
print(text[8:4:-1]) # "roW "

# Slicing with negative step
print(text[::-2])   # "drWolH"
```

## String Encoding & Decoding

### Understanding Encoding
- **Encoding**: Converting string to bytes
- **Decoding**: Converting bytes to string
- **UTF-8**: Default encoding in Python 3 (Unicode)

### Common Encoding Operations
```python
# String to bytes (encoding)
text = "Hello 🐍"
encoded_utf8 = text.encode('utf-8')
encoded_ascii = text.encode('ascii', errors='ignore')  # Ignores non-ASCII

print(encoded_utf8)     # b'Hello \xf0\x9f\x90\x8d'
print(type(encoded_utf8))  # <class 'bytes'>

# Bytes to string (decoding)
decoded = encoded_utf8.decode('utf-8')
print(decoded)          # "Hello 🐍"
```

### Encoding Error Handling
```python
text = "Café"

# Different error handling strategies
try:
    ascii_strict = text.encode('ascii')  # UnicodeEncodeError
except UnicodeEncodeError:
    ascii_ignore = text.encode('ascii', 'ignore')     # b'Caf'
    ascii_replace = text.encode('ascii', 'replace')   # b'Caf?'
    ascii_xmlchar = text.encode('ascii', 'xmlcharrefreplace')  # b'Caf&#233;'
```

## String Methods & Operations

### Common String Methods
```python
text = "  Hello World  "

# Case methods
print(text.upper())      # "  HELLO WORLD  "
print(text.lower())      # "  hello world  "
print(text.title())      # "  Hello World  "
print(text.capitalize()) # "  hello world  "

# Whitespace methods
print(text.strip())      # "Hello World"
print(text.lstrip())     # "Hello World  "
print(text.rstrip())     # "  Hello World"

# Search methods
print(text.find("World"))     # 8 (index of first occurrence)
print(text.index("World"))    # 8 (like find, but raises exception if not found)
print(text.count("l"))        # 3 (number of occurrences)

# Boolean methods
print(text.startswith("  He"))  # True
print(text.endswith("ld  "))    # True
print("123".isdigit())          # True
print("abc".isalpha())          # True
print("abc123".isalnum())       # True
```

### String Formatting
```python
name = "Alice"
age = 30

# f-strings (Python 3.6+) - Recommended
formatted = f"My name is {name} and I'm {age} years old"

# .format() method
formatted = "My name is {} and I'm {} years old".format(name, age)

# % formatting (older style)
formatted = "My name is %s and I'm %d years old" % (name, age)
```

## Important Interview Questions & Concepts

### 1. String Immutability Impact
```python
# Inefficient string concatenation
result = ""
for i in range(1000):
    result += str(i)  # Creates new string each time

# Efficient alternative
result = "".join(str(i) for i in range(1000))
```

### 2. Difference between `==` and `is` for strings
```python
# String interning for small strings
a = "hello"
b = "hello"
print(a == b)  # True (same content)
print(a is b)  # True (same object due to interning)

# Large strings or runtime creation
a = "hello" * 1000
b = "hello" * 1000
print(a == b)  # True (same content)
print(a is b)  # False (different objects)
```

### 3. Memory efficiency of string operations
```python
# Memory efficient
words = ["apple", "banana", "cherry"]
result = " ".join(words)  # "apple banana cherry"

# Memory inefficient
result = ""
for word in words:
    result += word + " "  # Creates new string each iteration
```

## String vs Other Languages

### Python String vs JavaScript String
| Feature | Python | JavaScript |
|---------|--------|------------|
| Mutability | Immutable | Immutable |
| Indexing | `str[i]` or `str[-i]` | `str[i]` only |
| Slicing | Built-in `str[start:end]` | `str.slice(start, end)` |
| Multi-line | Triple quotes `"""` | Template literals `` ` `` |
| Encoding | Explicit `.encode()` | Usually automatic |

### Python String vs C String
| Feature | Python | C |
|---------|--------|---|
| Memory Management | Automatic | Manual |
| Bounds Checking | Automatic | Manual |
| Unicode Support | Built-in | Requires libraries |
| String Length | `len()` function | `strlen()` function |
| Null Termination | Not null-terminated | Null-terminated |

## Best Practices

1. **Use f-strings** for string formatting (Python 3.6+)
2. **Use `join()`** for concatenating multiple strings
3. **Be aware of encoding** when working with files or network data
4. **Use raw strings** for regex patterns and file paths
5. **Understand slicing notation** for text processing

## Common Pitfalls

1. **String concatenation in loops** (inefficient)
2. **Assuming strings are mutable** (like in C)
3. **Not handling encoding errors** properly
4. **Confusing `find()` and `index()`** methods
5. **Forgetting negative indexing** capabilities

## Performance Tips

```python
# Fast membership testing
vowels = "aeiou"
if char in vowels:  # O(n) for strings, use set for O(1)
    pass

# Better for frequent lookups
vowels_set = set("aeiou")
if char in vowels_set:  # O(1)
    pass
```

## Summary

Python strings are:
- **Immutable**: Cannot be changed in place
- **Unicode**: Full Unicode support by default
- **Flexible**: Rich set of methods and operations
- **Efficient**: Optimized for common operations

Key concepts to remember:
- Indexing (positive and negative)
- Slicing with start:stop:step syntax
- Encoding/decoding for byte conversion
- Immutability implications for performance
