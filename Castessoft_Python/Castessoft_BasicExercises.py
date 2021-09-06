# -----------------------------
#  AGE RANGE VERIFICATOR
# -----------------------------
personAge = int(input("Please Enter your age: \n --> "))
if personAge >= 18:
    print("you're an Adult !!")
else:
    print("You're a Minor !!")

age = int(input("Enter your age: \n --> "))

# Simple Logic --> twenties = 20 <= age < 30
twenties = age >= 20 and age < 30
print(f"Twenties value: {twenties}")

thirties = age >= 30 and age < 40

print(f"thirties value: {thirties}")

if twenties or thirties:
    if twenties:
        print("Into the Twenties !! :) ")
    else:
        print("Into the Thirties !! :) ")
else:
    print("Out of the appropriated Range !!")

#--------------------------------
# LARGER NUMBERS
# ------------------------------

print("-----------The greatest number between two numbers-------")
number1 = int(input("Provide the first number: "))
number2 = int(input("Provide the second number: "))

if number1 > number2:
    print(f"The greatest number is {number1}")
elif number1 == number2:
    print(f"The numbers are equal")
else:
    print(f"The greatest number is {number2}")

#-----------------------------
# TERNARY OPERATOR
# -----------------------------
print("The Ternary Operator")

validator = int(input("Please enter 1 or 2: "))

print(f"The validator's value is: {validator}") if validator == 1 else print(f"The validator's value is {validator}")

#------------------------------
# THE STATIONS OF YEAR 
# -----------------------------

print("----------THE STATIONS OF YEAR-------------")
print("---------\tWELCOME TO MY CODE \t------------")
print("------\tAuthor: Juan Castellanos ------\n-------\tTel: 3223067599 --------\n-------\temail: "
      "juan.castellanosj@usantoto.edu.co -------")

season = int(input("Please input the season\n --> "))

if 3 <= season <= 5:
    print("This is Spring")
elif 6 <= season <= 8:
    print("This is Summer")
elif 9 <= season <= 11:
    print("This is Fall")
elif season == 12 or season == 1 or season == 2:
    print("This is winter")

# -----------------------------
# THE GRADING SYSTEMS 
# -----------------------------
grade = float(input("Please input your grade between 0 to 10 \n---> "))
if 9 <= grade <= 10:
    print("--- A ---")
elif 8 <= grade < 9:
    print('--- B ---')
elif 7 <= grade < 8:
    print("--- C ---")
elif 6 <= grade < 7:
    print("--- D ---")
elif 0 <= grade < 6:
    print("--- F ---")
else:
    print(" NO FOUND OPTION, please input the correct value between 0 to 10! ")
