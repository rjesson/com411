import json

# define read function
def read (file_path):
    with open(file_path) as json_file:
        # load json file and store in a variable
        data = json.load(json_file)
        # extract city and store in a variable
        city_name = data("city")
        # display name of the city
        print(f"City name: {city_name}")
        # extract population and store in a variable
        population_size = data("population")
        # display population
        print(f"Population size: {population_size}")
        # extract stats for each bot
        for bot in data("bots"):
            name = bot('name')
            stats = bot ('stats')
            print(f"{name} has the following stats: {stats}")

def run():
    read("robocity.json")

if __name__ == "__main__":
    run()




