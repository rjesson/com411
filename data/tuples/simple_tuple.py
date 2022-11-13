# Define a function to create a tuple of likelihoods
def likelihoods():
    likelihoods = (50, 38, 27, 99, 4)
    # Return minimum likelihood
    return min(likelihoods)

def run():
    # Have to call the likelihood function within this display function
    print(f"Minimum likelihood of falling is: {likelihoods()}%")

if __name__ == "__main__":
    run()