# while Loop
# The while loop is used to repeatedly execute a block of code as long as a condition is true.

name = ""

while True:
    name = input("enter one-word name, friends use to greet you: ")
    if name.isalpha():
        print("\nGood to see you", name.title())
        break
    else:
        print("\nSorry, enter one-word using letters only")