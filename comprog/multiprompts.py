#input multiple prompts

print("Please enter five grades. One at a time.")

grade1 = input("Grade 1: ")
grade2 = input("Grade 2: ")
grade3 = input("Grade 3: ")
grade4 = input("Grade 4: ")
grade5 = input("Grade 5: ")
sum_grades = int(grade1) + int(grade2) + int(grade3) + int(grade4) + int(grade5)
average = sum_grades / 5
print(average)
