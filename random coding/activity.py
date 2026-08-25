# Start
name = input("Enter student name: ")
score1 = int(input("Enter Quiz 1 score: "))
score2 = int(input("Enter Quiz 2 score: "))
score3 = int(input("Enter Quiz 3 score: "))
total_score = score1 + score2 + score3
average_score = total_score / 3

average = 75

if average_score >= average:
    print("You passed!")
else:
    print("You failed!")
# End