# Ask user for input
print("What level of brightness is required?")

# Read user input
brightness_required = int(input())

# Adjust brightness
print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_required + 1, 2):
    print(f"Beep's brightness level: {'*' * brightness}")
    print(f"Bop's brightness level: {'*' * brightness}")

print("Adjustments complete!")



