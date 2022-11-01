# Define search function with one parameter of the file path
def search(file_path):
    print("Searching.....")

    # open a string variable named sections
    sections = ""

    # open a string variable named books
    books = "Books:\n"

    # open specified file to read
    with open (file_path) as file:
        # loop through each line of text
        for line in file:
            # Determine which action to take
            if line.startswith("Section"):
                sections += line
            else:
                books += line
    print("Done!")

    return f"{sections}\n\n{books}"

# define function for file path and the data to be stored
def save(file_path, data):
    print("Saving...")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")

def run():
    data = search("books.txt")
    save("exported_books.txt", data)

if __name__ == "__main__":
    run()







