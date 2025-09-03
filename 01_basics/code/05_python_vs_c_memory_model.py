#!/usr/bin/env python3
"""
CONCEPT: Python vs C Memory Model Comparison
PURPOSE: Understanding fundamental differences in how variables work
LEARNING: Python variables are labels, C variables are memory containers
"""

print("="*70)
print("PYTHON vs C: FUNDAMENTAL DIFFERENCE IN MEMORY MODEL")
print("="*70)

print("\n=== PYTHON: OBJECTS EXIST FIRST, VARIABLES ARE JUST LABELS ===")

# In Python, these objects exist in memory even without variables!
print("Objects created in memory (even without assignment):")
print(f"Integer 4 exists at: {id(4)}")
print(f"Integer 5 exists at: {id(5)}")
print(f"String 'hello' exists at: {id('hello')}")
print(f"List ['jeet','kartik'] exists at: {id(['jeet','kartik'])}")

print("\n=== DEMONSTRATION: OBJECTS EXIST INDEPENDENTLY ===")

# These are the SAME objects we saw above!
a = 4
b = 5
c = "hello"
d = ["jeet", "kartik"]

print(f"\nAfter assignment:")
print(f"Variable 'a' points to object at: {id(a)} (same as literal 4)")
print(f"Variable 'b' points to object at: {id(b)} (same as literal 5)")
print(f"Variable 'c' points to object at: {id(c)} (same as literal 'hello')")
print(f"Variable 'd' points to object at: {id(d)}")

print(f"\nProof - comparing with literals:")
print(f"a is 4: {a is 4} (same object!)")
print(f"b is 5: {b is 5} (same object!)")
print(f"c is 'hello': {c is 'hello'} (same object!)")

print("\n=== PYTHON MEMORY MODEL ===")
print("Step 1: Objects are created in memory")
print("Step 2: Variables are just 'name tags' pointing to objects")
print("Step 3: Multiple variables can point to the same object")

print("\n=== VARIABLES DON'T HAVE THEIR OWN MEMORY ===")
print("Variables are just references/pointers to objects")

# Multiple variables pointing to same object
x = 42
y = 42
z = x

print(f"\nMultiple variables, same object:")
print(f"x = {x}, ID: {id(x)}")
print(f"y = {y}, ID: {id(y)}")
print(f"z = {z}, ID: {id(z)}")
print(f"All same object? {id(x) == id(y) == id(z)}")

print("\n" + "="*70)
print("COMPARISON: PYTHON vs C MEMORY MODEL")
print("="*70)

print("\nC LANGUAGE MODEL:")
print("1. Declare variable → Allocate memory for variable")
print("2. int x;           → Reserve 4 bytes for 'x'")
print("3. x = 42;          → Put value 42 in x's memory")
print("4. Variable HAS its own memory location")

print("\nPYTHON MODEL:")
print("1. Create object   → Object 42 exists in memory")
print("2. x = 42          → 'x' is a label pointing to object 42")
print("3. y = 42          → 'y' also points to the SAME object 42")
print("4. Variables are just NAMES/REFERENCES to objects")

print("\n=== PRACTICAL DEMONSTRATION ===")

print("\nIn C (conceptual):")
print("int a = 100;  // a gets its own memory with value 100")
print("int b = 100;  // b gets DIFFERENT memory with value 100")
print("// Changing b doesn't affect a because they have separate memory")

print("\nIn Python:")
a_py = 100
b_py = 100
print(f"a_py = 100  # a_py points to cached object 100 at {id(a_py)}")
print(f"b_py = 100  # b_py points to SAME cached object at {id(b_py)}")
print(f"Same object? {a_py is b_py}")

print("\nWhen we 'change' b_py:")
original_b_id = id(b_py)
b_py = b_py + 200
print(f"b_py = b_py + 200")
print(f"a_py still points to: {id(a_py)} (unchanged)")
print(f"b_py now points to: {id(b_py)} (NEW object!)")
print(f"b_py's object changed? {original_b_id != id(b_py)}")

print("\n=== MEMORY VISUALIZATION ===")
print("C Memory Model:")
print("┌─────────┐ ┌─────────┐ ┌─────────┐")
print("│ a: 100  │ │ b: 100  │ │ c: 100  │")
print("└─────────┘ └─────────┘ └─────────┘")
print("Each variable has its own memory box")

print("\nPython Memory Model:")
print("      [Object: 100]")
print("         ↑ ↑ ↑")
print("         a b c")
print("All variables point to the same object")

print("\n=== VARIABLE DELETION DEMONSTRATION ===")
# This shows variables are just labels
temp_var = [1, 2, 3]
temp_id = id(temp_var)
print(f"Object [1,2,3] exists at: {temp_id}")

# Delete the variable (label), object might still exist
del temp_var
# temp_var no longer exists, but object might still be in memory
# (until garbage collected)

print("Variable 'temp_var' deleted, but object might still exist in memory")
print("(until garbage collector cleans it up)")

print("\n=== KEY DIFFERENCES SUMMARY ===")
print("C:")
print("  ✓ Variables have their own memory")
print("  ✓ Assignment copies values")
print("  ✓ Each variable is independent")
print("  ✓ Manual memory management")
print("  ✓ Direct memory access")

print("\nPython:")
print("  ✓ Objects live in memory independently")
print("  ✓ Variables are just names/labels")
print("  ✓ Assignment copies REFERENCES, not values")
print("  ✓ Multiple variables can share same object")
print("  ✓ Automatic garbage collection")

print("\n💡 MIND-BLOWING FACT:")
print("In Python, you can access objects directly without variables!")
print(f"Direct access to 999: {id(999)}")
print(f"Access again: {id(999)} (might be same due to optimization)")

print("\n🎯 CONCLUSION:")
print("Python: Objects First, Variables are Labels")
print("C: Variables First, Values are Stored in Variables")
print("\nThis fundamental difference affects:")
print("- How assignment works")
print("- How function parameters behave") 
print("- How memory is managed")
print("- How to avoid bugs related to shared references")
