import matplotlib.pyplot as plt

# Define function to display a line plot
def display (x,y):
    plt.plot(x,y)
    plt.show()

# Define run function to create lists
def run ():
    # Create lists for x and y axis
    x_values = [1, 2, 3, 4, 5 ]
    y_values = [1, 4, 9, 16, 25]
    # Call display function and pass paramters
    display(x_values, y_values)

run()

