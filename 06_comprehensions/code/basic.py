"""
Python Comprehensions - Complete Code Examples
=============================================

This file demonstrates all types of comprehensions with practical examples:
1. List Comprehensions
2. Set Comprehensions
3. Dictionary Comprehensions
4. Generator Expressions
"""

import sys
import timeit
from typing import Generator

print("=" * 60)
print("PYTHON COMPREHENSIONS - PRACTICAL EXAMPLES")
print("=" * 60)

# =============================================================================
# 1. LIST COMPREHENSIONS
# =============================================================================
print("\n🔹 LIST COMPREHENSIONS")
print("-" * 30)

# Basic list comprehension
print("1. Basic Transformation:")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With conditional filtering
print("\n2. With Filtering:")
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")

# String operations
print("\n3. String Operations:")
menu = ["Masala Chai", "Iced Tea", "Green Tea", "Iced Peach Tea"]
iced_tea = [tea for tea in menu if "Iced" in tea]
print(f"Iced teas: {iced_tea}")

uppercase_menu = [tea.upper() for tea in menu]
print(f"Uppercase menu: {uppercase_menu}")

# Conditional expressions
print("\n4. Conditional Expressions:")
numbers = [-2, -1, 0, 1, 2]
labels = ['positive' if x > 0 else 'negative' if x < 0 else 'zero' for x in numbers]
print(f"Number labels: {list(zip(numbers, labels))}")

# Nested loops - Cartesian product
print("\n5. Nested Loops:")
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
print(f"Color-Size combinations: {combinations}")

# Flattening 2D lists
print("\n6. Flattening Lists:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Original matrix: {matrix}")
print(f"Flattened: {flattened}")

# Working with functions
print("\n7. Function Applications:")
def square_if_even(x):
    return x**2 if x % 2 == 0 else x

numbers = [1, 2, 3, 4, 5, 6]
transformed = [square_if_even(x) for x in numbers]
print(f"Transform (square if even): {transformed}")

# =============================================================================
# 2. SET COMPREHENSIONS
# =============================================================================
print("\n\n🔹 SET COMPREHENSIONS")
print("-" * 30)

# Remove duplicates and transform
print("1. Unique Values:")
fav_chai = ["Masala Chai", "Lemon Tea", "Green Tea", "Masala Chai"]
unique_chai = {chai for chai in fav_chai}
print(f"Original list: {fav_chai}")
print(f"Unique values: {unique_chai}")

# Unique squares
print("\n2. Unique Transformations:")
numbers_with_duplicates = [1, 2, 2, 3, 3, 4, 5, 5]
unique_squares = {x**2 for x in numbers_with_duplicates}
print(f"Original: {numbers_with_duplicates}")
print(f"Unique squares: {unique_squares}")

# Complex nested extraction
print("\n3. Nested Data Extraction:")
recipes = {
    "Masala Chai": ["ginger", "cardamom", "clover"],
    "Elaichi Chai": ["ginger", "milk", "clover"],
    "Spicy Chai": ["ginger", "black pepper", "clover"],
}
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(f"Recipes: {recipes}")
print(f"All unique spices: {unique_spices}")

# String processing
print("\n4. String Processing:")
words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']
first_letters = {word[0].upper() for word in words}
print(f"Words: {words}")
print(f"Unique first letters: {first_letters}")

# Prime numbers (with helper function)
print("\n5. Prime Numbers:")
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primes = {x for x in range(2, 30) if is_prime(x)}
print(f"Prime numbers (2-30): {primes}")

# =============================================================================
# 3. DICTIONARY COMPREHENSIONS
# =============================================================================
print("\n\n🔹 DICTIONARY COMPREHENSIONS")
print("-" * 30)

# Basic key-value creation
print("1. Numbers and Squares:")
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# String to length mapping
print("\n2. String Length Mapping:")
programming_languages = ['python', 'java', 'javascript', 'go', 'rust']
word_lengths = {lang: len(lang) for lang in programming_languages}
print(f"Language lengths: {word_lengths}")

# Currency conversion
print("\n3. Currency Conversion:")
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200,
    "Earl Grey": 150
}
tea_prices_usd = {tea: round(price/80, 2) for tea, price in tea_prices_inr.items()}
print(f"Prices in INR: {tea_prices_inr}")
print(f"Prices in USD: {tea_prices_usd}")

# Dictionary filtering
print("\n4. Dictionary Filtering:")
expensive_teas = {tea: price for tea, price in tea_prices_inr.items() if price > 100}
print(f"Expensive teas (>₹100): {expensive_teas}")

# Dictionary inversion
print("\n5. Dictionary Inversion:")
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
inverted = {value: key for key, value in original.items()}
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# Nested dictionary processing
print("\n6. Nested Dictionary Processing:")
students = {
    'alice': {'math': 85, 'science': 92, 'english': 88},
    'bob': {'math': 78, 'science': 88, 'english': 82},
    'charlie': {'math': 95, 'science': 87, 'english': 91}
}
averages = {name: round(sum(scores.values()) / len(scores), 1) 
           for name, scores in students.items()}
print(f"Student averages: {averages}")

# Conditional key transformation
print("\n7. Grade Classification:")
grade_classification = {
    name: 'Excellent' if avg >= 90 else 'Good' if avg >= 80 else 'Average'
    for name, avg in averages.items()
}
print(f"Grade classifications: {grade_classification}")

# =============================================================================
# 4. GENERATOR EXPRESSIONS
# =============================================================================
print("\n\n🔹 GENERATOR EXPRESSIONS")
print("-" * 30)

# Basic generator
print("1. Basic Generator:")
squares_gen = (x**2 for x in range(1, 6))
print(f"Generator object: {squares_gen}")
print(f"Generator values: {list(squares_gen)}")

# Memory comparison
print("\n2. Memory Usage Comparison:")
list_comp = [x for x in range(1000)]
gen_expr = (x for x in range(1000))
print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")
print(f"Generator expression size: {sys.getsizeof(gen_expr)} bytes")

# Generator for large datasets
print("\n3. Large Dataset Processing:")
def large_dataset_generator():
    return (x**2 for x in range(10000) if x % 100 == 0)

large_gen = large_dataset_generator()
first_10 = [next(large_gen) for _ in range(10)]
print(f"First 10 values from large generator: {first_10}")

# File processing simulation
print("\n4. File Processing Simulation:")
sample_lines = ["  hello world  ", "", "  python programming  ", "   ", "data science"]
processed_lines = (line.strip().title() for line in sample_lines if line.strip())
print(f"Processed lines: {list(processed_lines)}")

# Chain generators
print("\n5. Generator Chaining:")
numbers = range(100)
evens = (x for x in numbers if x % 2 == 0)
squares = (x**2 for x in evens)
large_squares = (x for x in squares if x > 100)
result = list(large_squares)[:10]  # First 10 results
print(f"Chained processing result (first 10): {result}")

# Fibonacci generator
print("\n6. Fibonacci Generator:")
def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
first_fibonacci = [next(fib_gen) for _ in range(15)]
print(f"First 15 Fibonacci numbers: {first_fibonacci}")

# Even Fibonacci numbers
even_fib_gen = (x for x in fibonacci() if x % 2 == 0)
first_even_fib = [next(even_fib_gen) for _ in range(10)]
print(f"First 10 even Fibonacci numbers: {first_even_fib}")

# =============================================================================
# 5. ADVANCED TECHNIQUES
# =============================================================================
print("\n\n🔹 ADVANCED TECHNIQUES")
print("-" * 30)

# Matrix operations
print("1. Matrix Transpose:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Original matrix: {matrix}")
print(f"Transposed matrix: {transpose}")

# Multiple conditions
print("\n2. Multiple Filtering Conditions:")
numbers = range(1, 100)
special_numbers = [x for x in numbers if x % 3 == 0 if x % 5 == 0 if x > 20]
print(f"Numbers divisible by 3 and 5, greater than 20: {special_numbers[:5]}")

# Enumerate with comprehensions
print("\n3. Enumerate in Comprehensions:")
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
indexed_items = {i: item.upper() for i, item in enumerate(items) if i % 2 == 0}
print(f"Even-indexed items (uppercase): {indexed_items}")

# Nested comprehensions
print("\n4. Nested Comprehensions (Pascal's Triangle):")

# Simpler Pascal's triangle using traditional approach
pascal_rows = []
for i in range(6):
    if i == 0:
        row = [1]
    else:
        prev_row = pascal_rows[-1]
        row = [1] + [prev_row[j] + prev_row[j+1] for j in range(len(prev_row)-1)] + [1]
    pascal_rows.append(row)

print("Pascal's triangle (first 6 rows):")
for i, row in enumerate(pascal_rows):
    print(f"Row {i}: {row}")

# Complex nested list comprehension example
print("\n   Complex nested comprehension:")
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("5x5 Multiplication table:")
for i, row in enumerate(multiplication_table, 1):
    print(f"Row {i}: {row}")

# =============================================================================
# 6. PERFORMANCE COMPARISON
# =============================================================================
print("\n\n🔹 PERFORMANCE COMPARISON")
print("-" * 30)

def traditional_loop():
    result = []
    for i in range(1000):
        result.append(i**2)
    return result

def list_comprehension():
    return [i**2 for i in range(1000)]

def generator_expression():
    return (i**2 for i in range(1000))

print("Performance timing (1000 iterations):")

# Time traditional loop
time_loop = timeit.timeit(traditional_loop, number=1000)
print(f"Traditional loop: {time_loop:.6f} seconds")

# Time list comprehension
time_list_comp = timeit.timeit(list_comprehension, number=1000)
print(f"List comprehension: {time_list_comp:.6f} seconds")

# Time generator (creation only)
time_gen = timeit.timeit(generator_expression, number=1000)
print(f"Generator creation: {time_gen:.6f} seconds")

improvement = ((time_loop - time_list_comp) / time_loop) * 100
print(f"List comprehension is ~{improvement:.1f}% faster than traditional loop")

# =============================================================================
# 7. REAL-WORLD EXAMPLES
# =============================================================================
print("\n\n🔹 REAL-WORLD EXAMPLES")
print("-" * 30)

# Data cleaning
print("1. Data Cleaning:")
raw_data = ["  John Doe  ", "", "jane smith", "  ", "BOB WILSON", None, "alice cooper  "]
cleaned_data = [name.strip().title() for name in raw_data 
                if name and name.strip()]
print(f"Cleaned names: {cleaned_data}")

# Email validation (simplified)
print("\n2. Email Validation:")
emails = ["user@example.com", "invalid-email", "test@domain.org", "bad@", "good@test.co.uk"]
valid_emails = [email for email in emails if "@" in email and "." in email.split("@")[-1]]
print(f"Valid emails: {valid_emails}")

# Log processing
print("\n3. Log Processing:")
log_entries = [
    "2024-01-15 ERROR: Database connection failed",
    "2024-01-15 INFO: User logged in",
    "2024-01-15 ERROR: Memory limit exceeded", 
    "2024-01-15 WARNING: Slow query detected",
    "2024-01-15 INFO: Backup completed"
]
errors = [entry for entry in log_entries if "ERROR:" in entry]
error_messages = {entry.split()[2]: entry.split("ERROR: ")[1] 
                 for entry in errors}
print(f"Error messages: {error_messages}")

# Configuration processing
print("\n4. Configuration Processing:")
config_items = [
    "DATABASE_URL=postgresql://localhost",
    "DEBUG=True", 
    "PORT=8000",
    "SECRET_KEY=my-secret-key",
    "# This is a comment",
    ""
]
config_dict = {item.split("=")[0]: item.split("=")[1] 
              for item in config_items 
              if item and not item.startswith("#") and "=" in item}
print(f"Configuration: {config_dict}")

print("\n" + "=" * 60)
print("COMPREHENSIONS DEMONSTRATION COMPLETED!")
print("=" * 60) 