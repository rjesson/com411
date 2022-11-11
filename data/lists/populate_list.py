# define function to create list of directions
def directions ():
    directions = ["Move Forward", "Move Backwards", "Turn Left", "Turn Right"]
    return directions

# Define a function to display a menu of directions for the user
def menu ():
    print("Please select a direction:")
    # Call the first function and store in a local variable
    dirs = directions()
    # use a loop to display each direction in the list with an index number
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")
    index = int(input())
    return (dirs[index])

# Define run function to create a route
def run():
    route = []
    print("Working out escape route...\n")
    # Create loop to call menu function and return direction to list route
    for count in range(5):
        route.append(menu())
    print(f"Escape route: {route}")

if __name__ == "__main__":
    run()

