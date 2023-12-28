""" Task 05 Capstone Project stdnt id CC23110012010 """
#  Investment calculator and home loan calculator
import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")

calc_choice = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))
calc_choice_upper = calc_choice.upper()

if calc_choice_upper == "INVESTMENT":
    amount_inv = int(input("Enter the amount of money you are investing: "))
    int_rate = int(input("Enter the interest rate as a whole number: "))      # annual rate
    percent_int_rate = int_rate / 100                       # convert to a %
    tenure = int(input("Enter the number of years you wish to invest: "))
    int_type = str(input("Enter whether you wish to have 'simple' or 'compound' interest: "))
    int_type_upper = int_type.upper()     # convert to upper case for comparison

    if int_type_upper == "SIMPLE":
        simp_int = amount_inv * (1 + percent_int_rate * tenure) # simple interest calc
        print("The total amount of interest and capital you will receive will be"\
            ,round(simp_int, 2))  # round to 2 dec places

    elif int_type_upper == "COMPOUND":
        comp_int = amount_inv * math.pow((1 + percent_int_rate), tenure)
        print("The total amount of interest and capital you will receive will be"\
            ,round(comp_int, 2))  # round to 2 dec places

    else:
        print("The interest rate type you entered does not match the types we offer.")

elif calc_choice_upper == "BOND":
    house_value = int(input("Enter the value of your house: "))
    int_rate = int(input("Enter the interest rate as a whole number: "))
    percent_int_rate = (int_rate / 100) / 12     # covert to a monthly int rate %
    loan_duration = int(input("Enter the number of months over which you wish to repay the loan: "))
    repayment = (percent_int_rate * house_value) / (1 - (1 + percent_int_rate)**(-loan_duration))
    print("Your monthly repayment will be:",round(repayment,2))

else:
    print ("The choice you entered does not match the products we offer.")
