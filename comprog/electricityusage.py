# Ask for the monthly usage in kWh. 
# Print "Low" for 100 or less,  "Average" for 101 to 200, "High" for 201 to 400, and "Very high" above 400. 
# Tests: 80, 200, 350, 500. 

monthly_usage = int(input("Enter the monthly usage in kWh: "))

if monthly_usage <=100:
    print(f"Your monthly usage is {monthly_usage} kWh, and your usage is low")
elif 101 <= monthly_usage <= 200:
    print(f"Your monthly usage is {monthly_usage} kWh, and your usage is average")
elif 201 <= monthly_usage <= 400:
    print(f"Your monthly usage is {monthly_usage} kWh, and your usage is high")
else:
    print(f"Your monthly usage is {monthly_usage} kWh, and your usage is very high")