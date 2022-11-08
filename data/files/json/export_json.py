import json

# Define function to read Json file
def read (file_path):
    print("Reading...", end="")
    with open(file_path) as json_file:
        # Load Json file and store in a variable
        data = json.load(json_file)
        print("Done!")
        return data

# Define function to save our read data
def save (file_path, saved_data):
    print("Exporting...")
    with open(file_path,"w") as json_file:
        json.dump(data, file_path, indent=4)
    print("Done!")



