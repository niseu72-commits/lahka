numbers = [1,2,3,4,5,6]

count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1
print("Total even numbers: ", count)