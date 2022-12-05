print("How many units do you wish to enter?")
no_units = int(input())
units = []
for i in range(no_units):
    print("Please enter unit name")
    unit_name = input()
    units.append(unit_name)

print("Here are the units you've entered:")
for unit_name in units:
    print(unit_name)
    




