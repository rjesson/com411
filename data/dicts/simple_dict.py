# Define function to create a dictionary
def pattern():
    sequences = {'Short Sequence':3, 'Medium Sequence':2, 'Long Sequence':1}
    # Return dictionary
    return sequences

#Define function to call the first function and display the dictionary
def run():
    print(pattern())

if __name__=="__main__":
    run()