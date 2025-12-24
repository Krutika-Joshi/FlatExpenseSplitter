# Flat Expense Splitter

print("Welcome to to Flat Expense Splitter")

#Taking inputs from user
rent = float(input("Enter total rent (Rs): "))
food = float(input("Enter total food expense (Rs): "))
electricity = float(input("Enter electricity bill (Rs): "))
people = int(input("Enter number of people int the flat: "))


# Input validation
if people <= 0:
    print("Error: Number of people must be greater than zero.")
else:
    total_expense = rent + food + electricity
    per_person = total_expense / people
    
    #Displaying result
    print("\n ------- Expense Summary ------")
    print(f"Total Expense: Rs {total_expense:.2f}")
    print(f"Each person has to pay: Rs {per_person:.2f}")