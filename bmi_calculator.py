"""
Deepa Naik
Class: CS 521 - Fall 1
Date: 17/10/2023
Term_project BMI (Body Mass Index) calculator
This program is a BMI calculator class with the following class attributes and methods
 """
class BMICalculator: #user defined class
    def __init__(self,age):
        """
        Constructor method for the class. It is called when an object of the class is created
        Initialize the constructor with age parameter
        Age is a parameter that the caller must provide when creating an object of this class.

        """
        self.__age=age #Private Class Attribute
        self.weight=0 #Public Attribute
        self.height=0 #Public Attribute
        self.height_unit="" #Public Attribute
        self.weight_unit="" #Public Attribute

    # tuple to store valid units
    VALID_UNIT=('metric','imperial')

    def set_units(self,height_unit,weight_unit): #public method
        """
        Set the units for height and weight.Raises ValueError If invalid units are provided.
        """

        # Define valid units for height and weight
        # using sets to ensure unique input for units
        valid_height_units={'cm','feet-inches'}
        valid_weight_units={'kg','pounds'}

        # Check if the provided height_unit is valid
        if height_unit not in valid_height_units:
            raise ValueError("Invalid height unit. Please choose 'cm" or 'feet-inches')

        if weight_unit not in valid_weight_units:# Check if the provided weight_unit is valid
            raise ValueError("Invalid weight unit. Please choose 'kg' or 'pounds'.")

# Set the height and weight units if they are valid
        self.height_unit=height_unit
        self.weight_unit=weight_unit

    def __calculate_bmi_metric(self): #private method
        """
        Calculate BMI using the metric system (centimeters and kilograms).returns calculated BMI

        """
        if self.height==0 or self.weight==0: # Check if height or weight is equals to 0
            raise ValueError("Height and Weight must not be zero. ")
        return self.weight/((self.height/100)**2)# Calculate BMI using the formula


    def __calculate_bmi_imperial(self, weight,height): #private method
        """
        Calculate BMI using the imperial system (centimeters and kilograms).returns calculated BMI

        """
        if height==0 or weight==0: # Check if height or weight is equals to 0
            raise ValueError("Height and Weight must not be zero. ")
        return (weight/(height * height)) * 703 #Calculate BMI using the formula

    def calculate_bmi(self): #public method
        """
        Calculate BMI based on the provided height, weight, and units.Returns the calculated BMI.checks for validity
        of inputs
        """
        if self.__age < 20:  # Check if the age is less than 20
            raise ValueError("Age must be 20 or above. ")
        if self.height==0 or self.weight==0: # Check if height or weight is equals to 0
            raise ValueError("Height and Weight must not be zero. ")
        # Check the units for height and weight and calculate BMI accordingly
        if self.height_unit=='cm' and self.weight_unit=='kg':
            return self.__calculate_bmi_metric()
        elif self.height_unit=='feet-inches' and self.weight_unit=='pounds':
            return self.__calculate_bmi_imperial(self.weight,self.height)
        else: #handle exception if invalid input
            raise ValueError("Invalid units. Please choose 'metric' or 'imperial'.")


    def get_bmi_category(self, bmi_value, age=None): #public method
        """
        Get the BMI category based on the BMI value. Returns The BMI category and advice.

        """
        if age is not None and age < 20: #if age is provided but is less than 20
            raise ValueError("Age must be 20 or above.")

        # Determine the BMI category based on the BMI value
        if bmi_value < 18.5:
            return "Underweight: Please focus on consuming a nutritious diet and consult your health provider"
        elif 18.5 <= bmi_value < 24.9:
            return "Normal weight: Congratulations! Your BMI is normal"
        elif 25 <= bmi_value < 29.9:
            return "Overweight: Please exercise and eat healthy food. You may consult a nutritionist for further advice"
        else:
            return "Obesity: Please consult your health provider for further advice"


    def __str__(self):
        """
        Return a string with contact information
        """

        return "For more information, please contact at abc@abc.com and 808-123456"


    def __repr__(self):
        """
        Return a string describing the source of BMI recommendations.
        """
        return "The bmi calculator is based on The Centers for Disease Control and Prevention agency recommendations"

    def __eq__(self, other):
        """
         Magic method to compare two objects by their values
        """
        return self.__age == other.__age




