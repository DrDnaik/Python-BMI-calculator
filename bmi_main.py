"""
Deepa Naik
Class: CS 521 - Fall 1
Date: 17/10/2023
Term_project BMI (Body Mass Index) calculator
This is the driver program. It drives the execution of our codes
 """

from bmi_calculator import BMICalculator #importing BMICalculator class

def get_user_input():
    """
     Collects user data including age, units (metric/imperial), weight, and height.Returns list of dictionaries
     containing user data.Each dictionary represents a user record.
    """
    # List used to store user data records
    user_data = [] # Create an empty list to store user data records

    while True: # Use a while loop to repeatedly ask for the user's age until a valid input is received
        try:
            age = int(input("Enter Your Age: ")) # Prompt the user to enter their age as an integer
            if age < 0:  # Check if the entered age is negative
                print("Age cannot be negative. Please enter a non-negative age.")
            elif age < 20: # Check if the entered age is less than 20
                print("Age must be 20 years or above.")
            else:
                # if valid age, age is stored in a dictionary, and the dictionary is added to the list
                user_data.append({"age": age})
                break

        except ValueError: # Handle exception if the user enters invalid input
            print("Invalid Input. Please enter a valid age.")

    while True: # Use a while loop to ask for the units (metric or imperial)until user enters a valid input
        units = input("Choose units (metric/imperial): ").lower()

        # Check if the entered units are valid
        if units not in BMICalculator.VALID_UNIT:
            print("Invalid units. Please choose 'metric' or 'imperial'.")
        else:
            # Dictionary used to store user data for the last record in the list
            user_data[-1]['height_unit'] = units
            user_data[-1]['weight_unit'] = units

            # Set specific unit  based on the choice (e.g., 'cm' and 'kg' for metric)
            if units == 'metric':
                user_data[-1]["height_unit"] = "cm"
                user_data[-1]["weight_unit"] = "kg"
            else:
                user_data[-1]["height_unit"] = "feet-inches"
                user_data[-1]["weight_unit"] = "pounds"
            break

    # Prompt the user to enter their weight and store it in the user data
    user_data[-1]["weight"] = get_weight(user_data[-1]['weight_unit'])
    user_data[-1]["height"] = get_height(user_data[-1]['height_unit'])

    # Return the list of user data records
    return user_data

def get_weight(weight_unit):# Use a while loop to repeatedly ask for the user's weight until a valid input is received
    """
    Collects user weight in the specified unit (kg or pounds)

    """
    while True:
        try:
            weight = float(input(f"Enter your weight in {weight_unit}: "))# Prompt the user to enter their weight
            if weight < 0: # Check if the entered weight is negative
                print("Weight cannot be negative. Please enter a non-negative weight.")
            else:
                return weight # Return the valid weight value
        except ValueError:  # Handle exception if the user enters invalid input
            print("Invalid Input. Please enter a valid weight.")

def get_height(height_unit):
    """
     Collects user height in the specified unit (cm or feet-inches).
    """
    while True: # Use a while loop to repeatedly ask for the user's height until a valid input is received
        try:
            if height_unit == 'cm': # Check the specified unit for height
                height = float(input(f"Enter your height in {height_unit}: "))
            else: # Prompt the user to enter their height in feet and remaining inches
                feet = float(input(f"Enter your height in feet: "))
                inches = float(input("Enter your remaining inches: "))
                height = (feet * 12) + inches

            if height < 0: # Check if the entered height is negative
                print("Height cannot be negative. Please enter a non-negative height.")
            else:
                return height # Return the valid height value
        except ValueError:# Handle exception if the user enters invalid input
            print("Invalid Input. Please enter a valid height.")



if __name__ == "__main__": #main function
    print("BMI Calculator\n")
    user_data = get_user_input()  #  collect user data
    for data in user_data:  # Process each user data record
        age = data.get('age')
        weight_unit = data.get('weight_unit')
        height_unit = data.get('height_unit')
        weight = data.get('weight')
        height = data.get('height')

        bmi_calculator = BMICalculator(age)  # Create an object of the BMICalculator class with the user's age

        bmi_calculator.set_units(height_unit, weight_unit)  # Set the units  for the BMI calculator
        bmi_calculator.weight = weight
        bmi_calculator.height = height

        try:
            bmi = bmi_calculator.calculate_bmi()  # Calls method calculate_bmi() with object of the class

            # Display user information and BMI result
            print(f"Age: {age}")
            print(f"Units: {weight_unit} / {height_unit}")
            print(f"Weight: {weight} {weight_unit}")
            print(f"Height: {height} {height_unit}")
            print(f"Your BMI: {bmi:.2f}")

            # Pass the BMI value and age to the get_bmi_category method
            category = bmi_calculator.get_bmi_category(bmi, age)
            print(f"BMI Category: {category}")
            # print(f"{bmi_calculator}\n")
            print(repr(bmi_calculator))
            print(f"{bmi_calculator}\n")

            # Create two BMICalculator instances
            bmi_calculator1 = BMICalculator(20)
            bmi_calculator2 = BMICalculator(20)
            print("Are these two values equal :", bmi_calculator1 == bmi_calculator2)#check if equal

            # Define BMI categories and their corresponding ranges
            bmi_categories = {
                "Underweight": "< 18.5",
                "Normal Weight": "18.5 - 24.9",
                "Overweight": "25.0 - 29.9",
                "Obesity": ">=30"
            }
            # Display weight categories
            print("-" * 25)
            print("Weight Categories")
            print("-" * 25)

            # Print each category and its corresponding BMI range
            for category, range_str in bmi_categories.items():
                print(f"{category}: {range_str}")

            print("-" * 25)  # seperator line

        except ValueError as e:  # exception handling for any errors apart from ones specified
            print(f"Error: {e}")



