# My budget for a trip to Pisgah National Forest
# 9/20/2022
# CTI-110 P1HW2 - Travel expense
# Cody Dyrdahl
#
print("This program calculates and displays travel expenses")
print()
initial_budget = float(input("How much do we have?: "))
print()
destination = input("Where are we going?: ", )
print()
gas = float(input("The gas budget: "))
print()
hotel = float(input("How much are we spending on the hotel?: "))
print()
food = float(input("Sustainance Budget: "))
remainder = float(initial_budget - gas - hotel - food)
print()
print("------------Travel Expenses------------")
print("The destination: ", destination)
print("What we have: ", initial_budget)
print()
print("Gas money: ", gas)
print("Hotel: ", hotel)
print("Food: ", food)
print()
print("Here is whats left: ", remainder)
# Request user input for (initial budget, destination, gas, hotel, food)
# Display the user's input for each respective variable
# Use the input to calculate the remaining budget after expenses.
