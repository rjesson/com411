print("How many teams will you enter?")
no_teams = int(input())
teams = []
for i in range(no_teams):
    print("Please enter a team")
    team = input()
    teams.append(team)

print(f"You've entered {no_teams} teams.  These are the teams you've entered:")
for team in teams:
    print(team)

print("Do you want to add any more teams")
response = input()
if response == "yes":
    print("How many more teams?")
    no_teams = int(input())
    for i in range(no_teams):
        print("Please enter a team")
        team = input()
        teams.append(team)
    length_list = len(teams)
    print(f"There are {length_list} teams in this list")
    for team in teams:
        print(team)

print("Who do you want to win?")
winner = input()
if winner == "Eng":
    print("Its coming home")


