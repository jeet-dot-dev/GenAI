# Python Loop Control Statements

Python provides control statements to alter loop execution: `break`, `continue`, and `else` with loops.

## break Statement
Exits the loop immediately.
```python
for x in [1, 2, 3]:
    if x == 2:
        break
    print(x)
```

## continue Statement
Skips the current iteration and continues with the next.
```python
for x in [1, 2, 3]:
    if x == 2:
        continue
    print(x)
```

## else with Loops
The `else` block after a loop runs only if the loop wasn't terminated by `break`.
```python
for x in [1, 2, 3]:
    if x == 4:
        break
else:
    print("Loop completed without break")
```

## Usage with Lists, Tuples, Dictionaries
- `break` and `continue` work with any iterable (list, tuple, dict, etc.).
- `else` is rarely used but can be useful for search operations.

## Comparison: Python vs C Loop Control
- Python uses keywords (`break`, `continue`, `else`) with indentation.
- C uses keywords with braces and no `else` for loops.

Python:
```python
for x in [1, 2, 3]:
    if x == 2:
        break
```
C:
```c
for (int i = 0; i < 3; i++) {
    if (arr[i] == 2) break;
}
```

## Notes
- Use control statements to manage loop flow and exit conditions.
