# Ask user to enter a type of adventure
print("What type of adventure should I have?")

# Read user's input
adventure = input()

# Determine the adventure type
if (adventure == "short") or (adventure == "scary"):
    print("Entering the dark forest")
elif (adventure == "safe") or (adventure == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take")



