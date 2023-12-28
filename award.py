# Task 04 Logical Programming - Operators student id CC23110012010
# Triathlon Award Calculator

a = 5
b = 10
result = a ** b
print(result)

competitor_name = str(input("Please enter the the name of the competitor: "))

swim_time = int(input("Please enter the time of the swim as a whole number in minutes: "))

cycle_time = int(input("Please enter the time of the cycle ride as a whole number in minutes: "))

run_time = int(input("Please enter the time of the run as a whole number in minutes: "))

overall_time = swim_time+cycle_time+run_time

if overall_time >=0 and overall_time <=100:
    print("Congratulations",competitor_name,", you have been awarded the Provincial Colours!")

elif overall_time >= 101 and overall_time <= 105:
    print("Congratulations",competitor_name,", you have been awarded the Provincial Half Colours!")

elif overall_time >= 106 and overall_time <= 110:
    print("Congratulations",competitor_name,", you have been awarded the Provincial Scroll!")

else:
    print("You overall time was",overall_time,", regrettably",\
        competitor_name,",on this occasion you have received No Award.")
