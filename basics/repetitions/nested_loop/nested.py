# Display message
print("How many rows should I have?")

# Read user's input
rows = int(input())

# Display message
print("How many columns should I have?")

# Read user's input
columns = int(input())

# Display grid
for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()
print("\nDone!")


