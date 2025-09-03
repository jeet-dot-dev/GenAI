# Python Numbers - Complete Guide

## Overview
Python supports various numeric data types to handle different kinds of numbers. Understanding these types is crucial for memory efficiency and precision in calculations.

## Types of Numbers in Python

### 1. Integer (int)
- **Definition**: Whole numbers without decimal points
- **Range**: Unlimited precision (only limited by available memory)
- **Examples**: `42`, `-17`, `0`, `999999999999999999999`

#### Key Features:
- **Arbitrary Precision**: Python integers can be infinitely large
- **No Overflow**: Unlike C/Java, Python integers don't overflow
- **Memory Efficient**: Small integers (-5 to 256) are cached for performance

#### Integer Caching (Important Interview Concept):
```python
# Small integers are cached
a = 100
b = 100
print(a is b)  # True (same object in memory)

# Large integers are not cached
x = 1000
y = 1000
print(x is y)  # False (different objects in memory)
```

### 2. Float (float)
- **Definition**: Numbers with decimal points
- **Precision**: 64-bit IEEE 754 double precision
- **Examples**: `3.14`, `-2.5`, `1.0`, `1e10`

#### Key Features:
- **Limited Precision**: ~15-17 decimal digits
- **Floating Point Errors**: Due to binary representation
- **Scientific Notation**: Supports `1e6` (1,000,000)

#### Common Issues:
```python
# Floating point precision issues
print(0.1 + 0.2)  # 0.30000000000000004 (not exactly 0.3)

# Solution: Use decimal module for exact decimal arithmetic
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3
```

### 3. Complex (complex)
- **Definition**: Numbers with real and imaginary parts
- **Format**: `a + bj` where `a` is real part, `b` is imaginary part
- **Examples**: `3+4j`, `2j`, `5+0j`

#### Key Features:
- **Built-in Support**: Native complex number arithmetic
- **Mathematical Operations**: All standard operations supported
- **Real/Imaginary Access**: `.real` and `.imag` attributes

```python
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
print(abs(z))  # 5.0 (magnitude)
```

## Type Conversion

### Implicit Conversion (Automatic)
```python
# Python automatically converts to maintain precision
result = 5 + 3.2  # int + float = float (8.2)
result = 2 + 3j   # int + complex = complex (2+3j)
```

### Explicit Conversion
```python
# Converting between types
int_val = int(3.7)      # 3 (truncates, doesn't round)
float_val = float(5)    # 5.0
complex_val = complex(2, 3)  # (2+3j)

# String to number
num = int("42")         # 42
num = float("3.14")     # 3.14
```

## Important Interview Questions & Concepts

### 1. Why are small integers cached in Python?
**Answer**: Python caches integers from -5 to 256 for performance optimization. These numbers are commonly used, so caching them saves memory and improves performance by reusing the same object.

### 2. What's the difference between `/` and `//` operators?
```python
print(7 / 2)   # 3.5 (true division - always returns float)
print(7 // 2)  # 3 (floor division - returns int for int operands)
```

### 3. How to handle floating point precision issues?
**Solutions**:
- Use `decimal.Decimal` for exact decimal arithmetic
- Use `round()` function for display purposes
- Use `math.isclose()` for floating point comparisons

### 4. What's the maximum value for Python integers?
**Answer**: There's no built-in maximum. Python integers have arbitrary precision, limited only by available memory.

## Memory Considerations

### Integer Storage:
- Small integers (-5 to 256): Singleton objects (cached)
- Large integers: Dynamic memory allocation
- Memory usage grows with number size

### Float Storage:
- Fixed 64-bit IEEE 754 format
- Constant memory usage regardless of value

## Best Practices

1. **Use appropriate types**: Don't use float if int suffices
2. **Be aware of precision**: Use Decimal for financial calculations
3. **Understand caching**: Know when `is` vs `==` matters
4. **Handle division carefully**: Choose `/` vs `//` based on needs

## Common Pitfalls

1. **Float precision errors** in calculations
2. **Confusing `is` with `==`** for large integers
3. **Not understanding floor division** behavior with negative numbers
4. **Assuming float can represent all decimals exactly**

## Summary

Python's numeric types are designed for ease of use and mathematical accuracy:
- **int**: Unlimited precision whole numbers
- **float**: IEEE 754 double precision decimals
- **complex**: Built-in complex number support

Understanding these types, their limitations, and Python's automatic type conversion rules is essential for writing robust numerical code.
