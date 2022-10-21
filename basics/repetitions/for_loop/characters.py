# Ask user for input
print("What strange markings do you see?")

# Read user's input
markings = input()

# Display markings
print("\nIdentifying....\n")

for count in range(0, len(markings), 1):
    print(f"index{count}:", markings[count])

print("\nDone!")




