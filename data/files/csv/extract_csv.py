import csv

# define 'extract' function to dd....
def extract (file_path):
    print("Extracting....", end="")
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        # read in the headings
        headings = next(csv_reader)
        # create variable to read in names of each robot
        names = ""
        # loop to extract each of the robot names
        for values in csv_reader:
            # Display only the names
            names += f"{values[1]}\n"
        print("Done!")
        print(f"The extracted names are:\n{names}")

# Create run function
def run():
    extract("bots.csv")

if __name__ == "__main__":
    run()


