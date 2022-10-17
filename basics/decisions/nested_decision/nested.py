# Ask user to enter cover type of the book
print("What type of cover does the book have? (hard or soft)")

# Read user input
cover_type = input()

# Decide if cover is soft or hard
if cover_type == "soft":
    # Ask if the book is perfect bound
    print("Is the book perfect-bound?")
    perfect_bound = input()

    # Decide which response beep should provide
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular.")
    else:
        print("Soft covers with coils or stitches are great for short books.")

else:
    print("Books with hard covers can be more expensive!")




