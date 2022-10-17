# Ask user where beep shoud look
print("Where should I look?")

# Read user response
where = input()

# Decide where to look
if where == "bedroom":
    # Determine where in the bedroom to look
    print("Where in the bedroom should I look?")
    where_bedroom = input ()

    # Determine which response to provide
    if where_bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")
elif where == "bathroom":
    print("Where in the bathroom should I look?")
    where_bathroom = input()
    if where_bathroom == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")
elif where == "lab":
    print("Where in the lab should I look?")
    where_lab = input()
    if where_lab == "on the table":
        print("Yes, I found my battery!")
    else:
        print("Found some tools but no battery")
else:
    print("I do not know where that is but I will keep looking...")





