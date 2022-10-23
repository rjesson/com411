# Display message
print("Program started...")

# Ask user for a single character
print("Please enter a single character")

# Read user's input
character = input()

# Determine if single character entered
if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("A single character was expected!")
print("\nProgram ended.")




