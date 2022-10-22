# Display message
print("What phrase do you see?")

# Read user's input
phrase = input()

# Identify markings
print("\nReversing...")
print("The phrase is ", end="")

for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")


