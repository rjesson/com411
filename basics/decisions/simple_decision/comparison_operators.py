# Prompt user to enter the first number
print("Please enter the first number")

# Read the user's response
first_number = int(input())

# Prompt user to enter the second number
print("Please enter the second number")

# Read the user's response
second_number = int(input())

# Determine which of the numbers is the largest
if first_number < second_number:
    print("The first number is the smallest")
elif first_number > second_number:
    print("The second number is the smallest")
else:
    print("Both are equal!")




