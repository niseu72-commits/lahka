# Ask for the price of a meal, the quantity, and the cash given (all whole pesos).
# Print the total, the change, how many ₱50 bills fit in the change, and the coins left over.

price = float(input("Enter the price of the meal: "))
quantity = int(input("How many meals are you buying? "))
cash_given = float(input("How much cash are you giving? "))

total = price * quantity
change = cash_given - total
change_50_bills = int(change // 50)
coins_leftover = change % 50

print(f"The total of your order is: ₱{total}")
print(f"Your change is: ₱{change}") 
print(f"You will receive {change_50_bills} ₱50 bills and ₱{coins_leftover} in coins as change.")

print("-------------RECEIPT-------------")
print(f"Price of meal: ₱{price}")
print(f"Quantity: {quantity}")
print(f"Total: ₱{total}")
print(f"Cash Given: ₱{cash_given}")
print(f"Change: ₱{change}")
print("-------------RECEIPT-------------")