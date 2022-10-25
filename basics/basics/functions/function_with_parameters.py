# Define function with two parameters
def climb_ladder(steps_remaining, steps_crossed):
    # Compare values and display determined message
    if steps_remaining>steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

# Calls to function
climb_ladder(5, 2)
climb_ladder(2, 5)

