# Program for Convert DOLLARS to EUROS and Program for convert EUROS en Dollars
option = int(input("Please enter an option \n--> 1. for Dollars to Euros \n---> 2. for Euros to Dollars \n--> "))


def convert_to(option_params):
    if option_params == 1:
        dollars = float(input("Please enter dollar's value: "))
        print(f"The Dollar's value {dollars} in Euros is {(dollars * 2)}")
    elif option_params == 2:
        euros = float(input("Please enter euros' value: "))
        print(f"The Euros' value {euros} in Dollars is {euros / 2}")
    else:
        print("Incorrect Option, Please choose between 1 to 2 ")


# Call the  Method to Convert xd
convert_to(option)
