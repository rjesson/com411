# take another loops 2 and break up into functions to simplify the code
# These functions will take a list parameter
# break into create a list function and print the list function

# the list is empty but does exist.  The function allows us to enter items into the list
def add_list():
    number_items = int(input("How many items would you like to add: "))
    for i in range(number_items):
        item = input("Please enter an item: ")
        shopping_list.append(item)

def print_list():
    # need to determine how many items are in the shopping list
    number_items = len(shopping_list)
    print(f"You have entered {number_items} items. They are:")
    for item in shopping_list:
        print(item)


# What happens if I dont include a parameter?
shopping_list = []
add_list()
print_list()

# need to create a new variable here to determine how many items are in the list using len function
# WHY did it do it before but not now.  Is it because that variable now only exists locally within that function
# Could I have returned it?





print("Is there anything you have forgotten?")
response = input()
if response == "yes" or "Yes":
    print("How many more items would you like to add?")
    number_items = int(input())
    for i in range(number_items):
        print("Please enter another item")
        item = input()
        shopping_list.append(item)


length_list = len(shopping_list)
print(f"You have now entered {length_list} items. The full list is:")
for item in shopping_list:
    print(item)
