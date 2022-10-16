# ask user for a direction to move the paint brush.
print("Towards which direction should I paint? (up, down, left or right")
direction = input()
# Working out which direction Beep should paint based on user input
if direction == "up":
    print("I am painting in the upward direction!")
elif direction == "down":
    print("I am painting in the downward direction")
elif direction == "left":
    print("I am painting in the left direction")
elif direction == "right":
    print("I am painting in the right direction")
else:
    print("I do not know which direction you want me to paint")
    print("\n\tPainting activity complete!")





