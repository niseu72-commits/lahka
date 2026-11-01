def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    difference = num1 - num2
    return difference

def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(num1, num2):
    if num1 != 0:
        quotient = num2 / num1
        return quotient
    else:
        return 0

def modulo(num1, num2):
    if num1 != 0:
        remainder = num2 % num1
        return remainder
    else:
        return 0

num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter a second number: "))
operator = input("What is your operation? Enter + - * / or % only.: ")

if operator == "+":
    answer = add(num1, num2)
elif operator == "-":
    answer = subtract(num1, num2)
elif operator == "*":
    answer = multiply(num1, num2)
elif operator == "/":
    answer = divide(num1, num2)
elif operator == "%":
    answer = modulo(num1, num2)
else:
    print("This is not a valid operation!")

print(str(answer))