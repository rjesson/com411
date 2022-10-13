# ask user to enter their name
print("what is your name human?")
name = input()
print(f"It is nice to meet you {name}")

# ask user how old they are
print("How old are you? (in years)")
age = int(input())

# ask user how tall they are
print("How tall are you?(in metres)")
height = float(input())

# ask user how much they weigh?
print("How much do you weigh? (in kilograms)")
weight = float(input())

# working out BMI which is weight (kg) divided by height squared
bmi = float(weight/(height**2))
print(f"Your BMI = {bmi:.2f}")
print(f"{name} you are {age} years old and your bmi is {bmi:.2f}.")


















