# Task 02 part two Strings programs student id CC23110012010
# Replace function demo

test_string1 = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print (test_string1.replace ("!", " ")) # replace ! with space

test_string2 = (test_string1.replace ("!", " "))    # assign the stripped version to test string 2
print (test_string2.upper()) # print the stripped string upper case

print (test_string2.upper()[::-1])  # print the stripped upper case string in reverse order
