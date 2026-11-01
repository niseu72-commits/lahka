# Ask whether the enrollment fee is paid (yes/no). If not, print "Please pay the enrollment fee first." 
# If paid, ask for the number of units and print "Overload: needs dean approval" above 26 units, "Regular load" for 12 to 26, and "Underload" below 12. 
# Tests: no, yes with 30; yes with 21; yes with 9.

enrollment_fee = input("Have you paid the enrollment fee? (yes/no): ").lower()

if enrollment_fee == "no":
    print("Please pay the enrollment fee first.")
else:
    number_of_units = int(input("Enter the number of units: "))
    print(f"You have enrolled in {number_of_units} units.")
    if number_of_units > 26:
        print("Overload: needs dean approval")
    elif 12 <= number_of_units <= 26:
        print("Regular load")
    else:
        print("Underload")