# Ask user to enter number
print("Please enter a number")

# Read user input
number = int(input())

# Calculate factorial
count = 0
total = 1

while count < number:
    count = count + 1
    total = total * count

print(f"The factorial is {total}.")


