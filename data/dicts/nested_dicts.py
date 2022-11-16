# Program to identify patterns
# Define function to create a dictionary
def short_pattern():
    pattern = {"sequence":"101", "occurrences":5 }
    return pattern

# Define a function to create a second dictionary
def medium_pattern():
    pattern = {"sequence":"111000", "occurrences": 25}
    return pattern

def long_pattern():
    pattern = {"sequence":"1100110011001100","occurrences":50}
    return pattern

# Define function to run
def run():
    # Display message
    print("Analysing patterns...")
    # Create a dictionary with Key value pairs calling the previous functions
    patterns = {"short sequence": short_pattern(),
                "medium sequence": medium_pattern(),
                "long sequence": long_pattern()
                }
    # Loop through contents of dictionary to display items
    for key, value in patterns.items():
        print(f"{key}:{value}")

if __name__ == "__main__":
    run()

