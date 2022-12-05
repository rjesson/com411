def print_list(teams_list):
    length_list = len(teams_list)
    print(f"There are {length_list} teams.  These are the teams you've entered:")
    for team in teams_list:
        print(team)


def add_to_list(teams_list):
    print("How many teams will you enter?")
    no_teams = int(input())
    for i in range(no_teams):
        print("Please enter a team")
        team = input()
        teams_list.append(team)


teams = []
add_to_list(teams)
print_list(teams)

print("Do you want to add any more teams")
response = input()
if response == "yes":
    add_to_list(teams)
    print_list(teams)

print("Who do you want to win?")
winner = input()
if winner == "Eng":
    print("Its coming home")


