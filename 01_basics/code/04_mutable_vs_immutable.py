#!/usr/bin/env python3
"""
CONCEPT: Mutable vs Immutable Objects Comparison
PURPOSE: Understanding the difference between mutable and immutable types
LEARNING: How assignment and modification behave differently
"""

print("="*60)
print("COMPARISON: MUTABLE vs IMMUTABLE OBJECTS")
print("="*60)

print("\n=== PART 1: IMMUTABLE INTEGERS ===")
print("Integers cannot be modified in-place")

a = 100
b = a  # Both point to same object
print(f"Initial state:")
print(f"  a = {a} (ID: {id(a)})")
print(f"  b = {b} (ID: {id(b)})")
print(f"  Same object? {a is b}")

b = b + 200  # Creates NEW object, doesn't modify existing
print(f"\nAfter b = b + 200:")
print(f"  a = {a} (ID: {id(a)}) ← unchanged")
print(f"  b = {b} (ID: {id(b)}) ← NEW object")
print(f"  Same object? {a is b}")
print("Result: 'a' is unchanged because integers are immutable!")

print("\n=== PART 2: MUTABLE LISTS ===")
print("Lists CAN be modified in-place")

list_a = [1, 2, 3]
list_b = list_a  # Both point to SAME list object
print(f"Initial state:")
print(f"  list_a = {list_a} (ID: {id(list_a)})")
print(f"  list_b = {list_b} (ID: {id(list_b)})")
print(f"  Same object? {list_a is list_b}")

list_b.append(4)  # Modifies the SAME object
print(f"\nAfter list_b.append(4):")
print(f"  list_a = {list_a} (ID: {id(list_a)}) ← CHANGED!")
print(f"  list_b = {list_b} (ID: {id(list_b)}) ← same object")
print(f"  Same object? {list_a is list_b}")
print("Result: BOTH lists changed because they share the same object!")

print("\n=== COMPARISON TABLE ===")
print("| Type    | Mutability | Assignment Effect | Modification Effect |")
print("|---------|------------|-------------------|---------------------|")
print("| int     | Immutable  | New object        | Not possible        |")
print("| str     | Immutable  | New object        | Not possible        |")
print("| tuple   | Immutable  | New object        | Not possible        |")
print("| list    | Mutable    | Same object*      | Modifies original   |")
print("| dict    | Mutable    | Same object*      | Modifies original   |")
print("| set     | Mutable    | Same object*      | Modifies original   |")
print("*when assigned from another variable")

print("\n=== SAFE COPYING FOR MUTABLE OBJECTS ===")
print("How to avoid shared reference issues:")

original_list = [1, 2, 3]
shallow_copy = original_list.copy()  # or original_list[:]
slice_copy = original_list[:]

print(f"Original: {original_list} (ID: {id(original_list)})")
print(f"Copy:     {shallow_copy} (ID: {id(shallow_copy)})")
print(f"Same object? {original_list is shallow_copy}")

shallow_copy.append(4)
print(f"\nAfter copy.append(4):")
print(f"Original: {original_list} ← unchanged")
print(f"Copy:     {shallow_copy} ← only copy changed")

print("\n=== DEMONSTRATION: STRING IMMUTABILITY ===")
s1 = "hello"
s2 = s1
print(f"Initial: s1='{s1}' (ID: {id(s1)}), s2='{s2}' (ID: {id(s2)})")

s1 = s1 + " world"  # Creates NEW string object
print(f"After s1 += ' world':")
print(f"  s1 = '{s1}' (ID: {id(s1)}) ← NEW object")
print(f"  s2 = '{s2}' (ID: {id(s2)}) ← unchanged")

print("\n💡 KEY INSIGHTS:")
print("IMMUTABLE (int, str, tuple):")
print("  ✓ Assignment creates NEW objects")
print("  ✓ Variables pointing to same value stay independent after reassignment")
print("  ✓ Thread-safe by default")

print("\nMUTABLE (list, dict, set):")
print("  ✓ Methods modify the EXISTING object")
print("  ✓ All variables pointing to same object see changes")
print("  ✓ Need explicit copying to avoid shared references")
