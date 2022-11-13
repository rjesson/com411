# Define function to create a list of tuples
def steps():
    all_steps = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    # Return list of tuples
    return all_steps

# Define function to call steps() and store returned list in a local variable
def run():
    all_steps = steps()
    # Create two empty lists
    good_steps = []
    bad_steps = []
    # Loop through list and apply steps to relevant list based on criteria
    for step in all_steps:
        if (step[1] >= 50):
            bad_steps.append(step)
        else:
            good_steps.append(step)
    # Included displaying list of tuples to aid learning
    print(good_steps)
    print(bad_steps)
    # Display message showing the number of good and bad steps
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

if __name__ == "__main__":
    run()
