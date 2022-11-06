# Import csv module
import csv

# create variable assigned to the file we want
file_path = "bots.csv"

# create program to read the file
with open(file_path) as csv_file:
    # read the variable I ve just opened above
    csv_reader = csv.reader(csv_file)

    # create variable to assign the headings
    headings = next(csv_reader)
    print(f"Headings: \n{headings}\n")
    print("Values:")
    # for loop to go through each row of reader and print out
    for row in csv_reader:
        print(row)



