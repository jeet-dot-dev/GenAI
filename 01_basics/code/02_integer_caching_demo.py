#!/usr/bin/env python3
"""
CONCEPT: Python Integer Caching (Small Integer Optimization)
PURPOSE: Understanding why some integers share the same memory location
LEARNING: Python caches small integers (-5 to 256) for performance
"""

print("="*60)
print("PYTHON INTEGER CACHING DEMONSTRATION")
print("="*60)

print("\n=== WHY IDs ARE SAME FOR a=100, b=100 ===")
a = 100
b = 100
print(f"a = {a}, ID: {id(a)}")
print(f"b = {b}, ID: {id(b)}")
print(f"Same object? {a is b}")

print("\n=== EXPLANATION ===")
print("Python caches small integers for performance optimization.")
print("When you assign the same small integer to different variables,")
print("they all reference the SAME object in memory.")

print("\n=== TESTING CACHE BOUNDARIES ===")

def test_caching(num):
    """Test if a number is cached by creating two variables"""
    x = num
    y = num
    return x is y

# Test different ranges
test_numbers = [-10, -6, -5, 0, 50, 100, 255, 256, 257, 300, 1000]

print("Number | Cached Status")
print("-" * 25)
for num in test_numbers:
    is_cached = test_caching(num)
    status = "CACHED" if is_cached else "NOT CACHED"
    print(f"{num:6d} | {status}")

print("\n=== DYNAMIC CREATION TEST ===")
# This might show different behavior
def create_number():
    return 1000

x = create_number()
y = create_number()
print(f"Dynamic 1000s: same object? {x is y}")

# Compare with literal assignment
p = 1000
q = 1000
print(f"Literal 1000s: same object? {p is q}")

print("\n=== MEMORY EFFICIENCY DEMO ===")
# Create a list of same numbers
numbers = [42] * 5
print("List of same numbers:", numbers)
print("Memory addresses of each 42:")
for i, num in enumerate(numbers):
    print(f"numbers[{i}] = {num}, ID: {id(num)}")

print("\n=== PRACTICAL IMPLICATIONS ===")
print("✅ GOOD - Use == for value comparison:")
print("   if x == 100:")
print("❌ BAD - Don't rely on 'is' for numbers:")  
print("   if x is 100:  # This might fail for large numbers!")

print("\n=== KEY TAKEAWAYS ===")
print("- Small integers (-5 to 256) are cached and reused")
print("- This saves memory and improves performance") 
print("- Don't rely on 'is' for value comparison - use '==' instead")
print("- 'is' checks object identity, '==' checks value equality")
print("- Caching is an implementation detail, not a language feature")
