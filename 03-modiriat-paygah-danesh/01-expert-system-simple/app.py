def diagnose_car():
    print("Car Diagnosis Expert System\n")
    print("Please answer the following questions with 'yes' or 'no'.\n")

    # Questions and diagnosis rules
    if input("Does the car not start? ").strip().lower() == "yes":
        if input("Is the battery dead? ").strip().lower() == "yes":
            print("Problem: The battery is dead. Solution: Charge or replace the battery.")
        elif input("Is there a clicking sound? ").strip().lower() == "yes":
            print("Problem: The starter is faulty. Solution: Check or replace the starter.")
        else:
            print("Problem: Check the electrical system.")
    elif input("Does the car shake while driving? ").strip().lower() == "yes":
        if input("Are the tires damaged? ").strip().lower() == "yes":
            print("Problem: The tires are damaged. Solution: Replace the tires.")
        elif input("Is there an issue with the suspension? ").strip().lower() == "yes":
            print("Problem: Suspension issue. Solution: Check and repair the suspension system.")
        else:
            print("Problem: Check the alignment or suspension system.")
    elif input("Is the check engine light on? ").strip().lower() == "yes":
        if input("Is there enough fuel in the tank? ").strip().lower() == "no":
            print("Problem: Insufficient fuel. Solution: Fill the fuel tank.")
        else:
            print("Problem: Visit a mechanic to check the error code.")
    else:
        print("Problem not identified. It is recommended to visit a mechanic.")

# Run the expert system
diagnose_car()
