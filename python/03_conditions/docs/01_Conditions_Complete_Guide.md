# Python Conditions: Complete Guide

This document covers all major conditional constructs in Python, including syntax, examples, and notes.

## 1. if Statement

The `if` statement is used to execute a block of code if a condition is true.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## 2. if-else Statement

The `if-else` statement provides an alternative block if the condition is false.

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## 3. elif Statement

`elif` allows checking multiple conditions sequentially.

```python
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## 4. Nested if-else

You can nest `if-else` statements inside each other.

```python
x = 10
y = 20
if x > 5:
    if y > 15:
        print("x > 5 and y > 15")
    else:
        print("x > 5 but y <= 15")
else:
    print("x <= 5")
```

## 5. match Statement (Python 3.10+)

The `match` statement is used for pattern matching, similar to switch-case in other languages.

```python
status = "success"
match status:
    case "success":
        print("Operation was successful")
    case "error":
        print("There was an error")
    case _:
        print("Unknown status")
```

## 6. Conditional Expressions (Ternary Operator)

Python supports conditional expressions for inline conditions.

```python
x = 10
result = "High" if x > 5 else "Low"
print(result)
```

## 7. Notes
- Indentation is crucial in Python for defining code blocks.
- Conditions can use logical operators (`and`, `or`, `not`).
- The `match` statement is available from Python 3.10 onwards.
- You can combine multiple conditions using parentheses and logical operators.

---

This guide covers all basic and advanced conditional constructs in Python.

## 8. Logical Operators in Conditions
You can use `and`, `or`, and `not` to combine multiple conditions.

```python
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are True")
if x > 5 or y < 15:
    print("At least one condition is True")
if not x < 5:
    print("x is not less than 5")
```

## 9. Chained Comparisons
Python allows chaining of comparison operators for concise checks.

```python
x = 7
if 5 < x < 10:
    print("x is between 5 and 10")
```

## 10. Membership Conditions
Check if a value exists in a sequence using `in` and `not in`.

```python
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")
if "orange" not in fruits:
    print("Orange is not in the list")
```

## 11. Identity Conditions
Use `is` and `is not` to check object identity.

```python
a = None
if a is None:
    print("a is None")
if a is not None:
    print("a is not None")
```

## 12. Short-Circuit Evaluation
Python evaluates conditions left to right and stops at the first decisive result.

```python
def check():
    print("Function called")
    return True

if True or check():
    print("Short-circuit: check() not called")
if False and check():
    print("Short-circuit: check() not called")
```

## 13. Multiple Conditions in match
You can use patterns and guards in `match` statements.

```python
value = 42
match value:
    case x if x > 40:
        print("Value is greater than 40")
    case x if x < 10:
        print("Value is less than 10")
    case _:
        print("Value is between 10 and 40")
```

---

These examples cover even more types of conditions in Python for practical use.
