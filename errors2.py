"""
 This example program is meant to demonstrate errors.
 There are some errors in this program. Run the program, look at the error messages, 
 and find and fix the errors.
"""

animal = "lion"     # Name error - run time, Lion is a string
animal_type = "cub"
number_of_teeth = 16

"""
full_spec = "This is a ", animal, ". It is a ",number_of_teeth," and it has ",animal_type, "teeth"
    logic error as list element logic used inside a string instead of var names. Also nonsense.

print(full_spec)    # syntax error, missing ()

print(f"This is a {animal} {animal_type}. It has {number_of_teeth} teeth.") # or using 
    the string var full_spec see below
"""

full_spec = f"This is a {animal} {animal_type}. It has {number_of_teeth} teeth."

print("\n")
print(full_spec)
print("\n")
