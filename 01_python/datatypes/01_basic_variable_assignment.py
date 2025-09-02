#!/usr/bin/env python3
"""
CONCEPT: Basic Variable Assignment and Reassignment in Python
PURPOSE: Understanding how variables work when assigned and reassigned
LEARNING: Variables are references to objects, not containers
"""

print("="*50)
print("BASIC VARIABLE ASSIGNMENT AND REASSIGNMENT")
print("="*50)

print("\n=== CONCEPT 1: Initial Assignment ===")
a = 2 
print("First number is", a)
print(f"ID of variable 'a': {id(a)}")
print(f"ID of literal 2: {id(2)}")
print(f"Are they the same object? {a is 2}")

print("\n=== CONCEPT 2: Reassignment ===")
a = 5
print("Second number is", a)
print(f"ID of variable 'a' now: {id(a)}")
print(f"ID of literal 5: {id(5)}")
print(f"Are they the same object? {a is 5}")

print("\n=== CONCEPT 3: Assignment vs Reassignment ===")
print("Key Understanding:")
print("- 'a = 2' means: 'a' points to object 2")
print("- 'a = 5' means: 'a' now points to object 5") 
print("- Variable 'a' doesn't change, it just points to different objects")

print("\n=== CONCEPT 4: Multiple Variables ===")
a = 5
b = a  # b now points to the same object as a
print(f"a = {a}, ID: {id(a)}")
print(f"b = {b}, ID: {id(b)}")
print(f"Same object? {a is b}")

print("\n=== CONCEPT 5: Independent Reassignment ===")
b = 6  # b now points to a different object
print(f"After b = 6:")
print(f"a = {a}, ID: {id(a)} (unchanged)")
print(f"b = {b}, ID: {id(b)} (new object)")
print(f"Same object? {a is b}")

print("\n💡 KEY LEARNING:")
print("Variables in Python are REFERENCES (pointers) to objects")
print("Assignment creates new references, not new memory locations")
