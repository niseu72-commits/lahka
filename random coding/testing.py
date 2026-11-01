def calculate_total():
    snack_name = input("Enter the name of the snack: ")
    price = float(input("Enter the price per unit: "))
    quantity = int(input("Enter the quantity purchased: "))
    calculate_total = price * quantity
    return snack_name, price, quantity, calculate_total

snack_name, price, quantity, total = calculate_total()

print(f"You purchased {quantity} {snack_name} for {price} each, with a total of {total}.")