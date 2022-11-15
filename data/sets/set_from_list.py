# Define a function to create a list of observations
def observed():
    observations = []
    # Populate the "observations" list with 7 values input from the user
    for count in range(7):
        print("Please enter an observation")
        observations.append(input())
    return observations

# Define run function to call the first function and store the returned list in a local variable
def run():
    # Display message
    print("Counting observations...")
    # Store the returned list from the observed function in a variable local to this function
    observations = observed()
    # Create an empty set
    observations_set = set()
    # Count the number of times an observation appears
    # loop through the observations list to extract each observation
    for observation in observations:
        # Creating a tuple the first element "observation" has the value the second has the count of times it appears on the list
        data = observation, observations.count(observation)
        # Once you have the tuple you add it to the set
        observations_set.add(data)
    # For own reference just printing out the set
    print(f"{observations_set}")
    # looping through the set to print out the values
    for item in observations_set:
        print(f"{item[0]} observed {item[1]} times.")

run()

