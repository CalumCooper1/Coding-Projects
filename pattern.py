""" Task 08 Star Pattern Exercise stdnt id CC23110012010 """
#  Determinate duration loop using 'for', plus use of 'if else'

counter = 0                         # set a counter to zero
print("")                           # throw a blank line
for x in range(1, 10):              # 9 lines of stars needed so set range to 10

    if x <= 5:
        print("*" * x)              # this will get us the stars from 1 to 5
        print("")                   # throw a blank line each time

    else:
        counter += 2                # increment the counter by 2 to now decrease num of stars
        print("*" * (x - counter))  # print out the decreasing num of stars using the counter
        print("")                   # throw a blank line each time
