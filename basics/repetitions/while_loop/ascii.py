# Display message
print("How many bars should be charged?")

# Read response
bars_to_charge = int(input())

# Declare control variable
bars_charged = 0

# Display bars
print()

while bars_charged < bars_to_charge:
    print("Charging:", end="")
    bars_charged = bars_charged +1
    print(bars_charged * "🁢")

print("\nThe battery is fully charged")









