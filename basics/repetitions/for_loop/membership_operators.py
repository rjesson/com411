# Display message
print("What phrase do you see?")

# Read users input
phrase = input()

# Identifying markings
print("\nReversing....")
print("The phrase is ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)





