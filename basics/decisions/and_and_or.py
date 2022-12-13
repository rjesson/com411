variant = 3
option = int(input("Please select an option: "))
if variant == 1 and option in range(1,5) or variant == 2 and option in range(1,4) or variant == 3 and option in range(1,3):
    print(option)
else:
    print("Invalid option selected")
    print(0)