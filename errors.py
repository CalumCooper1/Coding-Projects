"""
This example program is meant to demonstrate errors.
There are some errors in this program. Run the program, look at the error messages, 
and find and fix the errors.
"""
print("\n")
print("Welcome to the error program")    # Missing parentheses - syntax error
print("\n")                              # Indentation and parentheses missing - syntax errors

# Variables declaring the user's age, casting the str to an int, and printing the results
age_Str = "24"                           # indent, logical op == instead of =, syntax errors
age = int(age_Str)                       # indent, syntax error, logical error - assign letters to an int
print("I'm " + age_Str + " years old.")  # indent, syntax error, logical error trying to concatenate an int

# Variables declaring additional years and printing the total years of age  # indentation - syntax error
years_from_now = 3                         # indent, syntax error
total_years = age + years_from_now         # indent, syntax error, logical error trying to add an int and string

print("The total number of years in 3 years:", total_years) # missing parentheses - syntax error, logical error answer_years is a string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = age * 12                  # logical error "total" not defined, should be age
age_offset_months = 42                   # age offset needed for print statement below
total_months += age_offset_months        # actual age plus the age offset to get the correct answer
print("In 3 years and 6 months, I'll be ", total_months, " months old.")    # missing parantheses - syntax error, concatenate an int - logic error
print("\n")
