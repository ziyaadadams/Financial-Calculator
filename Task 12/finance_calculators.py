# Tasl 12 finance_calculator.py 

import math

# User must input either 'Investment' or 'Bond'

print("Please input the financial calculator you would like to use ")
print("Options:")
print("- Investment ")
print("- Bond ")

#user input stored in option variable
option = input("Please input your option: ")

#if to test what user has inputed which is stored in option variable 
if option == "investment" or option == 'Investment' or option == "INVESTMENT": #to test if user inputed investment
    
    amount = int(input("Please insert the amount of money you are depositing? ")) #user input stored in variable amount 
    interest_rate = float(input("Please insert the interest rate percentage? ")) #User prompt to input interest rate
    years = int(input("Please insert the amount of years? ")) # User prompt to insert years 
    interest = input("Please insert if you would like Compund or Simple interest? ") #user prompt to input between 2 option for different formulas IE compound and simple
    simple = (amount * (1 + interest_rate * years)) #Formula if user inputs simple
    compound = amount * math.pow((1 + interest_rate),years) #formula if user inputs compound
    
    #Nested Ifs statements after user has inserted simple or compound option
    if interest == "Simple" or interest == "simple" or interest == "SIMPLE":
        print("The amount of Simple interest for your amount is: R", (simple))
    
    elif interest == "Compound" or interest == "compound" or interest == "COMPOUND":
        print("The amount with Compound interest is: R",(compound))
         
# Else if statement if user insert 'bond' option which is in LINE 13
elif option == 'bond' or option == "Bond" or option == "BOND":
    
    amount = int(input("Please insert the value of the house? ")) #Amount user inputs for the house
    interest_rate = float(input("Please insert the monthly interest rate? ")) # prompts user to imput interest rate
    number_of_months = int(input("Please insert the amount of month the bond will be paid? ")) # prompts user to input how many months they will be repaying
    bond_repay = amount * ((interest_rate * (1 + interest_rate)**number_of_months))/(((1 + interest_rate)**number_of_months)- 1) #monthly repayment formula
    print("Your monthly repayments for the bond are: R", (bond_repay))
    print("R")

else:
    print("You have inserted an invalid option")










