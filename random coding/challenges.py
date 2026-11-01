# mini grade calculator
# 1. Ask the user to enter a score from 0 to 100.
# 2. Determine the grade using these rules:
# Score	Grade
# 90–100	A
# 80–89	B
# 70–79	C
# 60–69	D
# 0–59	F
# 3. If the score is below 0 or above 100, display Invalid score.
# 4. Display the result clearly.

score = int(input("Please enter your score from 0 to 100"))
if score < 0 or < 100:
print("It is invalid")