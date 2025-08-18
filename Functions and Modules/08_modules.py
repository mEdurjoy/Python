"""
mainly module two types
1. Built-in modules
2. User-defined modules
"""

# Built-in Modules
import math
import mymodule

a= math.sqrt(16)
print(f"Square root of 16 is: {a}")

mymodule.hello()
result = mymodule.add(5, 10)
print(f"Addition result is: {result}")
print(mymodule.add.__doc__)  # This will print the docstring of the add function