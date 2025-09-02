# Mutable vs Immutable Objects in Python

## Introduction

In Python, every object has an **identity**, a **type**, and a **value**. Understanding mutability is crucial because it affects how Python handles memory, variable assignment, and function parameters.

- **Mutable objects**: Can be changed after creation
- **Immutable objects**: Cannot be changed after creation

## Python Object Identity and Memory

### Behind the Scenes: Object References

```python
# When you create a variable, Python creates an object and assigns a reference
x = 42  # Creates an integer object with value 42
y = x   # y now points to the same object as x

print(id(x))  # Memory address of the object
print(id(y))  # Same memory address!
print(x is y) # True - they reference the same object
```

**Key Concept**: Variables in Python are **references** to objects, not containers holding values.

## Immutable Types

### Common Immutable Types:
- `int`, `float`, `bool`
- `str` (strings)
- `tuple`
- `frozenset`
- `bytes`

### How Immutability Works

```python
# String example
s1 = "hello"
s2 = s1
print(id(s1), id(s2))  # Same memory address

# When we "modify" s1, a new object is created
s1 = s1 + " world"
print(id(s1), id(s2))  # Different memory addresses now!
print(s2)              # Still "hello" - unchanged
```

### Integer Caching (Small Integer Optimization)

Python caches small integers (-5 to 256) for performance:

```python
a = 100
b = 100
print(a is b)  # True - same cached object

c = 1000
d = 1000
print(c is d)  # May be False - new objects created
```

### Tuple Immutability Gotcha

```python
# Tuple itself is immutable, but can contain mutable objects
t = ([1, 2], [3, 4])
# t[0] = [5, 6]  # This would raise TypeError
t[0].append(3)   # But this works! The list inside is mutable
print(t)         # ([1, 2, 3], [3, 4])
```

## Mutable Types

### Common Mutable Types:
- `list`
- `dict`
- `set`
- `bytearray`
- Custom classes (by default)

### How Mutability Works

```python
# List example
list1 = [1, 2, 3]
list2 = list1
print(id(list1), id(list2))  # Same memory address

# Modifying list1 affects list2 (same object!)
list1.append(4)
print(list2)  # [1, 2, 3, 4] - both variables see the change
```

### Dictionary Mutation

```python
original_dict = {'a': 1, 'b': 2}
alias_dict = original_dict

# Modifying through either reference affects the same object
alias_dict['c'] = 3
print(original_dict)  # {'a': 1, 'b': 2, 'c': 3}
```

## Function Parameters and Mutability

### Immutable Arguments

```python
def modify_immutable(x):
    x = x + 10  # Creates new object, doesn't affect original
    return x

num = 5
result = modify_immutable(num)
print(num)     # 5 - unchanged
print(result)  # 15
```

### Mutable Arguments (The Gotcha!)

```python
def modify_mutable(lst):
    lst.append(4)  # Modifies the original object!
    return lst

my_list = [1, 2, 3]
result = modify_mutable(my_list)
print(my_list)  # [1, 2, 3, 4] - original is modified!
print(result)   # [1, 2, 3, 4] - same object
```

### Safe Practices with Mutable Arguments

```python
def safe_modify_list(lst):
    # Create a copy to avoid side effects
    new_lst = lst.copy()  # or lst[:]
    new_lst.append(4)
    return new_lst

def safe_modify_dict(d):
    # Create a copy for dictionaries
    new_dict = d.copy()
    new_dict['new_key'] = 'new_value'
    return new_dict
```

## Default Mutable Arguments Anti-Pattern

### The Problem

```python
def append_to_list(item, target_list=[]):  # DON'T DO THIS!
    target_list.append(item)
    return target_list

# This creates unexpected behavior
list1 = append_to_list(1)  # [1]
list2 = append_to_list(2)  # [1, 2] - Oops! Same list object
```

### The Solution

```python
def append_to_list(item, target_list=None):
    if target_list is None:
        target_list = []  # Create new list each time
    target_list.append(item)
    return target_list
```

## Memory Management and Performance

### Immutable Objects and Memory

```python
# String concatenation creates many temporary objects
result = ""
for i in range(1000):
    result += str(i)  # Creates new string object each iteration!

# Better approach for strings
result = "".join(str(i) for i in range(1000))
```

### Mutable Objects and Shared References

```python
# Efficient: All elements point to same immutable object
matrix_efficient = [[0] * 3 for _ in range(3)]

# Dangerous: All rows are the same mutable list!
matrix_dangerous = [[0] * 3] * 3
matrix_dangerous[0][0] = 1
print(matrix_dangerous)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

## Copying Objects

### Shallow Copy vs Deep Copy

```python
import copy

# Original list with nested mutable objects
original = [[1, 2], [3, 4]]

# Shallow copy
shallow = original.copy()  # or copy.copy(original)
shallow[0].append(3)
print(original)  # [[1, 2, 3], [3, 4]] - inner list affected!

# Deep copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0].append(3)
print(original)  # [[1, 2], [3, 4]] - unchanged!
```

## Best Practices

### 1. Understand Reference Semantics
```python
# Always be aware of what you're copying
a = [1, 2, 3]
b = a        # Reference copy
c = a[:]     # Shallow copy
d = copy.deepcopy(a)  # Deep copy
```

### 2. Use Immutable Types When Possible
```python
# Use tuples for coordinates, configuration, etc.
point = (10, 20)  # Better than [10, 20] for fixed data
config = ('localhost', 8080, 'production')
```

### 3. Be Careful with Function Parameters
```python
def process_data(data, options=None):
    if options is None:
        options = {}  # Safe default
    # Process data...
```

### 4. Understand Container Mutability
```python
# Immutable container with mutable contents
frozen_data = frozenset([frozenset([1, 2]), frozenset([3, 4])])

# This works - truly immutable
safe_tuple = (1, 2, "hello", (3, 4))

# This is risky - tuple with mutable contents
risky_tuple = ([1, 2], {'key': 'value'})
```

## Common Pitfalls and Solutions

### Pitfall 1: Loop Variable Reference
```python
# Problem
functions = []
for i in range(3):
    functions.append(lambda: i)  # All lambdas reference same 'i'

# All functions return 2!
for f in functions:
    print(f())  # 2, 2, 2

# Solution
functions = []
for i in range(3):
    functions.append(lambda x=i: x)  # Capture current value

for f in functions:
    print(f())  # 0, 1, 2
```

### Pitfall 2: Mutable Class Attributes
```python
class Student:
    grades = []  # Shared among ALL instances!
    
    def add_grade(self, grade):
        self.grades.append(grade)

# Problem
student1 = Student()
student2 = Student()
student1.add_grade(85)
print(student2.grades)  # [85] - Oops!

# Solution
class Student:
    def __init__(self):
        self.grades = []  # Instance-specific list
```

## Advanced Concepts

### Interning
Python interns some objects for performance:

```python
# String interning
a = "hello"
b = "hello"
print(a is b)  # True - same interned object

# Not all strings are interned
c = "hello world"
d = "hello world"
print(c is d)  # May be False
```

### `__slots__` and Mutability
```python
class ImmutablePoint:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        object.__setattr__(self, 'x', x)
        object.__setattr__(self, 'y', y)
    
    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify immutable object")
```

## Conclusion

Understanding mutability in Python is crucial for:
- **Avoiding bugs** related to unexpected object modifications
- **Writing efficient code** by understanding when objects are copied
- **Designing better APIs** that don't have surprising side effects
- **Memory management** and performance optimization

**Remember**: In Python, assignment never copies objects - it only creates new references to existing objects. The mutability of the object determines whether modifications through one reference affect other references to the same object.