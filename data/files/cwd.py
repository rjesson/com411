# Import OS module

import os

# Define function to retrieve file path
def cwd():
    path = os.getcwd()
    print(f"The current working directory: {path}.")
    print("The directory contains the following files...")
    for file in os.listdir(path):
        print(file)


# Define the run function which calls the first function
def run():
    print("Processing....")
    cwd()


# Not sure about this bit of solution.  Why not just call run()
if __name__ == "__main__":
    run()







