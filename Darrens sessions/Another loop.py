# Ask user how many things they went to enter into a list
# Create a list
# Print list

print("How many items do you want to add to your shopping list?")
# Read users input and store in a variable
number_items = int(input())
# Create an empty list to store user's input
shopping_list = []
# depending on how many items user wants to add loop to ask to enter an item.
# referred to as i for integer by Programmers, range parameter is user input
for i in range(number_items):
    print("Please enter an item")
    # Read users input and store in a variable
    item = input()
    # Append each item to the variable shopping list
    shopping_list.append(item)
# Print shopping list
print("Here is your shopping list:")
for item in shopping_list:
    print(item)





