# Python Generators: Complete Guide

## What are Generators?
Generators are a special type of iterable in Python that allow you to iterate over data one item at a time, without storing the entire sequence in memory. They are defined using functions but use the `yield` keyword instead of `return`.

## Difference Between Generator and Function
- **Function:** Executes all statements and returns a value using `return`. Once returned, the function terminates.
- **Generator:** Uses `yield` to return a value and pause its state. It can be resumed later, continuing from where it left off. This allows for lazy evaluation and memory efficiency.

## Why Use Generators?
- **Memory Efficient:** Generates items one at a time, useful for large datasets.
- **Lazy Evaluation:** Only computes values as needed.
- **Pipeline Processing:** Can be chained for complex data processing.

## Real-Life Examples
- Reading large files line by line.
- Streaming data from APIs.
- Generating infinite sequences (e.g., Fibonacci numbers).
- Processing logs or sensor data.

## Key Concepts
### `yield`
- Pauses the function and returns a value to the caller.
- Remembers the function’s state for next invocation.

### `next()`
- Used to get the next value from a generator.
- Raises `StopIteration` when no more items.

### `send(value)`
- Sends a value into the generator, resuming execution and assigning the value to the last `yield` expression.

### `yield from`
- Used to delegate part of a generator’s operations to another generator.
- Useful for composing generators.

## How to Call Generators
1. Define a generator function using `yield`.
2. Call the function to get a generator object.
3. Use `next()` or loop to get values.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Create generator
gen = count_up_to(5)
print(next(gen))  # 1
print(next(gen))  # 2
for num in gen:
    print(num)    # 3, 4, 5
```

## Sending Values to Generators
```python
def echo():
    received = yield "Start"
    while True:
        received = yield received

g = echo()
print(next(g))         # "Start"
print(g.send("Hello")) # "Hello"
print(g.send("World")) # "World"
```

## Using `yield from`
```python
def subgen():
    yield 1
    yield 2

def main_gen():
    yield "A"
    yield from subgen()
    yield "B"

for val in main_gen():
    print(val)  # "A", 1, 2, "B"
```

## More Examples
### Infinite Generator
```python
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))  # 0, 1, 2, 3, 4
```

### File Reader
```python
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

for line in read_lines("large_file.txt"):
    print(line)
```

## Summary Table
| Feature         | Function         | Generator         |
|-----------------|------------------|-------------------|
| Returns         | Value            | Iterator          |
| Memory Usage    | High (all at once)| Low (one at a time)|
| State Retention | No               | Yes               |
| Use Case        | Simple return    | Large/streamed data|

## Recap
- Use generators for large, streamed, or infinite data.
- Use `yield` to produce values, `next()` to get them, `send()` to inject values, and `yield from` to delegate.
- Generators are called like functions but return an iterator.

---
**Tip:** Practice writing and using generators for file processing, pipelines, and custom iterators to master their use!
