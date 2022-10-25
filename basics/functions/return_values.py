# Define sum of weight function
def sum_weights(bop_weight, beep_weight):
    total_weight = bop_weight + beep_weight
    return total_weight

# Define average weight function
def calc_avg_weight(bop_weight, beep_weight):
    avg_weight = sum_weights(bop_weight, beep_weight)/2
    return avg_weight

# Define run function
def run():

    # Ask user for required inputs
    print("Please enter Beep's weight. (kgs)")
    beep_weight = float(input())

    print("Please enter Bop's weight. (kgs)")
    bop_weight = float(input())

    print("What would you like to calculate? (sum or average?)")
    action = input()

    # Determine and carry out action
    if action == "sum":
        answer = sum_weights(bop_weight, beep_weight)
        print(f"The sum on Beep and Bop's weight is {answer}")
    elif action == "average":
        answer = calc_avg_weight(bop_weight, beep_weight)
        print(f"The average of Beep and Bop's weight is {answer}")
    else:
        print("I am not sure what you would like me to do")

# Call function
run()









