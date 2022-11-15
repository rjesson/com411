# Define function to create an empty list of observations
def observed():
    # Create an empty list of observations to populate from user input
    observations = []
    # need to ask user for 5 inputs to observations
    for count in range(5):
        print("Please enter an observation:")
        # append the user input to the blank observations list
        observations.append(input())
        # Return the final list in a variable
    return observations

# Define function to ask user if they would like to remove any values from the list of observations returned above
# function to take one parameter which represents the list of observations.  Call this function and pass this value
def remove_observations(observations):
    # Ask the user IF they which to remove any observations
    # but as they may answer yes more times I need to create an infinite while loop to keep asking until they respond with anything other than yes
    # Create a variable to use in the while loop which determines that as long as that is true the loop will continue to ask if the user wishes to remove an observation.
    keep_asking = True
    while(keep_asking):
        print("Do you wish to remove an observation (yes/no)?")
        # Capture user response
        user_response = input()
        # Need a conditional statement to determine what action to take next depending on user response
        if user_response == "yes":
            # Display message to ask the user which observation they wish to remove
            print("Please enter the observation you wish to remove")
            # Capture user response in local variable
            observation = input()
            # remove whichever 'observation' the user inputs stored in the variable above
            observations.remove(observation)
        # For anything other than a 'yes' response from the user then change the keep_asking variable to false
        else:
            keep_asking = False

# Define function to call the first function and store the returned list in a local variable
def run():
    observations = observed()
    # Then also call the second function once the first one is finished
    # I have added the line below to show the user the list to then determine if they want to remove an item
    print(f"{observations}")
    # This second function uses the list stored in the local var 'observations' as the parameter it needs to run the function
    remove_observations(observations)

    # Need the function to create and display a sorted set of the observations and how many times each of the observations have been made.
    # create an empty set
    observations_set = set()
    # Loop through the list of observations stored in the variable above 'observations'
    for observation in observations:
        # create a tuple called data which shows the value held in observations and how many times it appears
        data = (observation, observations.count(observation))
        # add tuples to the empty set 'observation_set'
        observations_set.add(data)
    # Display a sorted set of the observations with the value and how many times they occur
    # if you print data variable you will see the value 'obs', 'how many times it appears' index position 0 and 1
    # For own reference just printing out the set
    print(f"{observations_set}")

    # loop through the observation_set using the built in 'sorted' function which will sort in numerical/alphabetical order
    for item in sorted(observations_set):
        print(f"{item[0]}, observed {item[1]} times.")

run()





