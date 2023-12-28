'''
For loop example
'''
# user_num = int(input("Enter a number: "))

# for y in range(1, 11):
#     product = y * user_num
#     print(f"{y} x {user_num} =", product)

# list_of_items = ["sugar", "honey", "ice", "lightsabre", "tea", "bread", "dogshit", "wank mag", "ninja stars"]
# for item in list_of_items:
#     if item == "lightsabre" or item == "ninja stars":
#         print("Weapons: ",item)
#         continue

#     elif item == "wank mag":
#         print("Entertainment:",item)

#     else:
#         print("Food:",item)

# dic_of_items = {1:"sugar: 100", 2:"honey: 800", 3:"ice: 10"}
# print(dic_of_items[2])
# tuple_of_items = (1, "sugar", 2, "dogshit")
# print(tuple_of_items[0])
# print("hellow world")

choice = ''
while choice != '3':
    print('\n')
    print("*** Menu *** \n\n"
    "1. Option 1 \n"
    "2. Option 2 \n"
    "3. Option 3 \n")

    choice = input("Enter your choice: ")
    if choice == '1':
        print("You chose option 1.")

playing_game = True
while playing_game:
    guess = input("Enter number")
    playing_game = False
    if not guess.isdigit() or int(guess) <= 0 or int(guess) >=0:
        print("Invalid")

user_input = ''
while user_input.upper() not in ["STOP", "EXIT", "END"]:
    print("Hello")
    user_input = input("Please press enter or enter the word 'stop' to exit:")
