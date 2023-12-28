# Task 03 Control Structures student id CC23110012010
# Age Quiz

age = int(input("Please enter your age as a whole number: "))

if age <13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age >= 40 and age <65:
    print("You're over the hill")
elif age >= 65 and age <= 100:
    print("Enjoy your retirement!")
elif age > 100:
    print("Sorry, you're dead.")
else:
    print("Age is but a number.")
