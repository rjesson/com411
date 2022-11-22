import matplotlib.pyplot as plt

# Define small function to display a small red square using a line plot
# Square needs to be made with a red dotted line and circle markers
def small():
    x = [3,3,4,4,3]
    y = [3,4,4,3,3]
    plt.plot(x,y,'ro:')

def medium():
    x = [2,2,5,5,2]
    y = [2,5,5,2,2]
    plt.plot(x,y,'gs--')

def large():
    x = [1,1,6,6,1]
    y = [1,6,6,1,1]
    plt.plot(x,y,'p-')


def run ():
    small()
    medium()
    large()
    plt.show()

run()



