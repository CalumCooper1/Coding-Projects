""" Task 08 For Loops statements stdnt id CC23110012010 """
#  Indeterminate duration loops using 'while', plus counting and averaging

iteration_count = 0
accumulated_value = 0
minus_one_entered = False

while not minus_one_entered:        # continue in loop until minus 1 is entered by the user
    number = int(input("Please enter a number or -1 to stop: "))

    if number == -1:
        minus_one_entered = True

        if iteration_count != 0:
            average = accumulated_value / iteration_count
            print ("The average of the numbers entered excluding -1 is: "\
                ,round(average, 2)) # round the average to 2 places

        else:
            print ("No numbers have been entered to calculate an average.") # if -1 is first up

    else:
        iteration_count += 1            # increment counter by 1
        accumulated_value += number     # sum num entered with running total
