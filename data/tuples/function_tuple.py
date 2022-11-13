# Define a function to create a tuple of likelihoods
def likelihoods():
    likelihoods = (50, 38, 27, 99, 4)
    # Return minimum likelihood
    return (min(likelihoods), max(likelihoods))

def run():
    # Call likelihood function and store returned values as a tuple in a local variable
    probabilities = likelihoods()
    # display values by indexing values in probabilities tuple
    print(f"Minimum likelihood of falling: {probabilities[0]}%")
    print(f"Maximum likelihood of falling:{probabilities[1]}%")

if __name__ == "__main__":
    run()

