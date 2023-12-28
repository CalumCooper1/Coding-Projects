"""
Defensive programming student id CC23110012010

Deliberate logic error using len to get the string length to define index in the slice operation.

Correct logic would seem to be user_name[::-1] or  user_name[len(user_name)::-1]

The way I have done it has given unexpected results

Instructions
============
Run the program
Type in any name or string of any length as the answer to the name question

using user_name[len(user_name):0:-1] does not work

correct logic is using user_name[::-1] or user_name[len(user_name)::-1]
"""
correct_in_reverse = False

while not correct_in_reverse:
    print("\n")
    user_name = str(input("Enter your full name: "))    # get user name
    print("\n")
    print (f"Hello there {user_name}!")                 # courteous greeting
    print("\n")

    str_length = 0
    str_length = len(user_name) # get actual length of users name

    print (f"Length of name {str_length}")  # show how long the name is
    print("\n")
    print (f"Your name backwards using ext variable string length is {user_name[str_length:0:-1]}.")
    print("\n")
    print ("Now using embedded length function of user_name just to try every possibility!")
    print("\n")
    print (f"Your name backwards is {user_name[len(user_name):0:-1]}.")  # print in reverse order
    print("\n")

    user_response = str(input("Is that correct? Please enter 'yes' to exit or 'no' to try again: "))

    if user_response.upper() == "YES":
        correct_in_reverse = True

print("\n")
print(f"Thank you {user_name}.")
print("\n")
