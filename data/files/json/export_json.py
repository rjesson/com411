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
def save (file_path, data):
    print("Exporting...",end="")
    with open(file_path,"w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Done!")

def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)

if __name__=="__main__":
    run()



