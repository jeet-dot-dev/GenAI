# Python for Loop

The `for` loop in Python is used to iterate over sequences like lists, tuples, dictionaries, strings, and more.

## Syntax
```python
for item in sequence:
    # code block
```

## Using for Loop with Lists
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

## Using for Loop with Tuples
```python
tuple_data = (1, 2, 3)
for num in tuple_data:
    print(num)
```

## Using for Loop with Dictionaries
```python
d = {'a': 1, 'b': 2}
for key in d:
    print(key, d[key])
# To iterate over items:
for key, value in d.items():
    print(key, value)
```

## enumerate()
`enumerate()` returns both index and value while looping.
```python
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
```

## zip()
`zip()` allows parallel iteration over multiple sequences.
```python
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
```

## Walrus Operator
The walrus operator (`:=`) assigns values within expressions.
```python
while (line := input()) != '':
    print(line)
```

## Comparison: Python vs C for Loop
- Python's for loop iterates directly over items in a sequence.
- C's for loop uses an index and requires manual increment.

Python:
```python
for x in [1, 2, 3]:
    print(x)
```
C:
```c
for (int i = 0; i < 3; i++) {
    printf("%d", arr[i]);
}
```

## Notes
- Python for loop is more readable and concise for sequence iteration.
- Use `range()` for numeric loops: `for i in range(5): ...`
