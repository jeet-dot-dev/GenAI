# Python Decorators: Complete Guide

## What are Decorators?
Decorators are a powerful feature in Python that allow you to modify or enhance the behavior of functions or classes without changing their code. They are often used for logging, access control, timing, caching, and more.

## How Decorators Work
A decorator is a function that takes another function (or class) as an argument and returns a new function (or class) with added functionality.

## Syntax
- Decorators use the `@decorator_name` syntax above a function definition.
- You can also apply them manually: `func = decorator(func)`

## Why Use Decorators?
- **Code Reusability:** Apply common logic to multiple functions.
- **Separation of Concerns:** Keep business logic separate from cross-cutting concerns (logging, timing, etc.).
- **DRY Principle:** Avoid code duplication.

## Real-Life Examples
- Logging function calls
- Measuring execution time
- Access control (authentication/authorization)
- Caching results
- Input validation

## Basic Decorator Example
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

## Decorators with Arguments
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

greet()  # Prints "Hi!" three times
```

## Built-in Decorators
- `@staticmethod`: Defines a static method in a class.
- `@classmethod`: Defines a class method.
- `@property`: Defines a property.

## Chaining Multiple Decorators
```python
def deco1(func):
    def wrapper(*args, **kwargs):
        print("deco1")
        return func(*args, **kwargs)
    return wrapper

def deco2(func):
    def wrapper(*args, **kwargs):
        print("deco2")
        return func(*args, **kwargs)
    return wrapper

@deco1
@deco2
def foo():
    print("foo")

foo()
# Output:
# deco1
# deco2
# foo
```

## Preserving Function Metadata
Use `functools.wraps` to preserve the original function’s name, docstring, etc.
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Class Decorators
Decorators can also be applied to classes to modify their behavior.
```python
def add_repr(cls):
    cls.__repr__ = lambda self: f"{self.__class__.__name__}({self.__dict__})"
    return cls

@add_repr
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(repr(p))  # Person({'name': 'Alice'})
```

## Practical Use Cases
### Logging
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

add(2, 3)
```

### Timing
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start}")
        return result
    return wrapper

@timer
def slow_func():
    time.sleep(1)

slow_func()
```

## Summary Table
| Feature         | Decorator         | Function         |
|-----------------|------------------|------------------|
| Purpose         | Modify behavior  | Perform action   |
| Syntax          | @decorator       | def function     |
| Use Case        | Logging, timing  | Business logic   |

## Recap
- Decorators wrap functions/classes to add or change behavior.
- Use `@decorator` syntax for clean code.
- Decorators can take arguments, be chained, and preserve metadata.
- Practice writing decorators for logging, timing, and access control to master their use!

---
**Tip:** Try creating your own decorators for validation, caching, or debugging to see their power in real projects!
