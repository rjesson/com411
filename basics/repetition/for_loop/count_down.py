# Display message
print("How far are we from the cave? (in steps)")

# Read user input
distance = int(input())

# Create blank line
print()

for count in range(distance,0,-1):
    print(f" {count} steps remaining...")
print("\nWe have reached the cave.")





