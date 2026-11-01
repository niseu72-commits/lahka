# A worker earns ₱100 per hour. Hours above 40 are paid 1.5 times the rate. 
# Ask for the hours worked and print the total pay. 
# Tests: 30 hours, 40 hours, 45 hours. 

hours_worked = int(input("Enter the number of hours worked: "))
pay = 100 * hours_worked

if hours_worked > 40:
    print(f"You worked for {hours_worked} hours. The total pay with overtime is: ₱{pay * 1.5:.2f}")
else:
    print(f"You worked for {hours_worked} hours. The total pay is: ₱{pay:.2f}")