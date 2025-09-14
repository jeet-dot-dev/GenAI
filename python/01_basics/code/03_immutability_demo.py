#!/usr/bin/env python3
"""
CONCEPT: Immutability of Integers in Python
PURPOSE: Understanding why changing one variable doesn't affect another
LEARNING: Integers are immutable - assignment creates new objects
"""

print("="*50)
print("IMMUTABILITY DEMONSTRATION")
print("="*50)

print("=== Step 1: Initial Assignment ===")
a = 100
b = 100
print(f"a = {a}, ID: {id(a)}")
print(f"b = {b}, ID: {id(b)}")
print(f"Same object? {a is b}")
print("Both variables point to the same cached integer object")

print("\n=== Step 2: Before Modifying b ===")
print(f"a points to object at: {id(a)}")
print(f"b points to object at: {id(b)}")
print("Both are pointing to the same memory location")

print("\n=== Step 3: 'Modifying' b with b = b + 200 ===")
print("What actually happens: b + 200 creates a NEW integer object (300)")
original_b_id = id(b)
b = b + 200
print(f"a = {a}, ID: {id(a)} (unchanged)")
print(f"b = {b}, ID: {id(b)} (NEW object!)")
print(f"Same object? {a is b}")
print(f"b's object changed? {original_b_id != id(b)}")

print("\n=== VISUAL EXPLANATION ===")
print("Before: a ──→ [100] ←── b  (both point to same cached 100)")
print("After:  a ──→ [100]      (a still points to cached 100)")
print("        b ──→ [300]      (b points to new 300 object)")

print("\n=== WHY 'a' DOESN'T CHANGE ===")
print("1. Integers are IMMUTABLE - they cannot be changed")
print("2. b = b + 200 creates a NEW object, doesn't modify the old one")
print("3. 'a' still points to the original 100 object")
print("4. Only b's reference changed to point to the new 300 object")

print("\n=== IMMUTABILITY TEST ===")
print("Demonstrating that the original 100 object is unchanged:")
original_100_id = id(100)
x = 100
y = 100
y = y + 1  # Creates new object 101
print(f"Original 100 object ID: {original_100_id}")
print(f"x (still 100) points to: {id(x)}")
print(f"Same as original? {id(x) == original_100_id}")
print("The 100 object was never modified!")

print("\n💡 KEY INSIGHT:")
print("In Python, you can't modify immutable objects")
print("You can only create new objects and point variables to them")
