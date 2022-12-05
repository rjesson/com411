# Ask user how many things they went to enter into a list
# Create a list
# tell user how many items theyve added and then print list
# Ask if they want to add any more items to list
# Add more items
# tell user how many items are in the list and print list.
# if one item is something print a separate message eg milk semi skimmed.

print("How many items would you like to add to your shopping list?")
number_items = int(input())
shopping_list = []
for i in range(number_items):
    print("Please enter an item")
    item = input()
    shopping_list.append(item)
print(f"You have entered {number_items} items. They are:")
for item in shopping_list:
    print(item)


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








