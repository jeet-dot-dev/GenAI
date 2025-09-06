# Python while Loop

The `while` loop in Python repeats a block of code as long as a condition is true.

## Syntax
```python
while condition:
    # code block
```

## Using while Loop with Lists
```python
fruits = ['apple', 'banana', 'cherry']
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

## Using while Loop with Tuples
```python
tuple_data = (1, 2, 3)
i = 0
while i < len(tuple_data):
    print(tuple_data[i])
    i += 1
```

## Using while Loop with Dictionaries
```python
d = {'a': 1, 'b': 2}
keys = list(d.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(key, d[key])
    i += 1
```

## Walrus Operator
The walrus operator (`:=`) can be used to assign values within the loop condition.
```python
while (data := input('Enter: ')) != 'exit':
    print(data)
```

## Comparison: Python vs C while Loop
- Python's while loop is similar to C's, but Python uses indentation instead of braces.

Python:
```python
i = 0
while i < 5:
    print(i)
    i += 1
```
C:
```c
int i = 0;
while (i < 5) {
    printf("%d", i);
    i++;
}
```

## Notes
- Use while loops for indefinite iteration when the number of repetitions is not known in advance.
- Be careful to update the loop variable to avoid infinite loops.
