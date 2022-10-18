# Ask user for input
print("How many live cables should I avoid?")

# Read user's response
cables_to_avoid = int(input())

# Create a control variable
cables_avoided = 0

# Print blank line as per example
print()

# avoid cables
while cables_avoided < cables_to_avoid:
    print(f"Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print(f"Done! {cables_avoided} live cables avoided.")

# Display final message
print("\nAll live cables have been avoided!")



