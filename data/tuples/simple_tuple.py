# Define a function to create a tuple of likelihoods
def likelihoods():
    likelihoods = (50, 38, 27, 99, 4)
    # Return minimum likelihood
    return min(likelihoods)

def run():
    min_likelihood = likelihoods()
    print(f"Minimum likelihood of falling is: {min_likelihood}%")

if __name__ == "__main__":
    run()