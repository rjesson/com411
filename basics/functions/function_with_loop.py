# Define function
def cross_bridge(steps):
    # Display each step
    for step in range(steps):
        print("Crossed step.")

    # Display message
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

# calls to function
cross_bridge(10)
cross_bridge(5)



