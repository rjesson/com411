# Import csv module
import csv

# define function to read the file
def read_file (file_path):
    with open(file_path) as csv_file:
    # read the variable I ve just opened above
        csv_reader = csv.reader(csv_file)

    # create variable to assign the headings
        headings = next(csv_reader)
        print(f"Headings: \n{headings}\n")
        print("Values:")
    # for loop to go through each row of reader and print out
        for values in csv_reader:
            print(values)

# Create run function
def run():
    read_file("bots.csv")

# call the function
if __name__ == "__main__":
    run()










