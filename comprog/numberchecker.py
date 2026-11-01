# Ask for a whole number.
# Without using if, print two True/False answers: is it even, and is it between 1 and 100 (inclusive)? 
# Test: 84, then 105. 

number = int(input("Enter a whole number: "))
is_even = number % 2 == 0
is_between_1_and_100 = 1 <= number <= 100

print(f"Is the number even? {is_even}")
print(f"Is the number between 1 and 100? {is_between_1_and_100}")