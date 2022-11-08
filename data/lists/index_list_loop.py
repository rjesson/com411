# define function to create a list of movements
def movements():
    # create list of movements called path
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    # call the first function and return list into a local variable
    path = movements()
    for index in range(0, len(path), 2):
        print(f"{path[index]} for {path[index+1]} steps")

if __name__=="__main__":
    run()