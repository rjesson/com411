# Display message
print("Program started...")

# Ask user for a single character
print("Please enter an ASCII code")

# Read user's input
ascii_code = int(input())

# Determine if single character entered
if ascii_code >= 32 and ascii_code <= 126:
    print(f"The character for {ascii_code} is {chr(ascii_code)}")
else:
    print("A single character was expected!")
print("\nProgram ended.")

