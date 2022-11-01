# Define function to open specified file for reading
def search(file_path):
    print("Searching...")
    # Open file path to be determined when you call the function
    with open(file_path) as file:
        # create for loop to read each line of file stripping out blank spaces
        for location in file:
            print(f"Looked in {location.strip()}")
        print("Done!")

def run():
    search("library.txt")

if __name__ == "__main__":
    run()









