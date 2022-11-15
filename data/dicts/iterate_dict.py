# Define a function to create a dictionary
def pattern():
    sequences = {'Short Sequence':3, 'Medium Sequence':2, 'Long Sequence':1}
    # Return dictionary
    return sequences

# Define a function to iterate through the dictionary and display the keys
# The data parameter which needs to be passed to the function will be defined later
def display_keys(data):
    print("\nKeys:")
    for key in data:
        print(key)

# Define a function to iterate through dictionary and display values
def display_values(data):
    print("\nValues:")
    for value in data.values():
        print (value)

# define function to iterate through the dictionary using the method items and display each key value pair
def display_pairs(data):
    print("\nPairs:")
    for key, value in data.items():
        print(f"{key}: {value}")

def run():
    data = pattern()
    print(f"Dictionary:\n{data}")

    display_keys(data)
    display_values(data)
    display_pairs(data)

run()
