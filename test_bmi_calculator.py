"""
Deepa Naik
Class: CS 521 - Fall 1
Date: 17/10/2023
Term_project BMI (Body Mass Index) calculator
This is a testing file to test two public methods of our program to ascertain if they function as expected
 """

import unittest
from bmi_calculator import BMICalculator

class TestBMICalculator(unittest.TestCase): #user defined class
    def test_get_bmi_category(self):
        """
        This function defines a test case  for the get_bmi_category method, which categorizes BMI values.

        """

        age = 20 # Age must be 20 or above for certain categories

        bmi_calculator = BMICalculator(age)# Create an instance of the BMICalculator with the specified age.

        # Test "Underweight" category
        underweight_bmi = 17
        underweight_category = bmi_calculator.get_bmi_category(underweight_bmi)
        self.assertEqual(underweight_category, "Underweight: Please focus on consuming a nutritious diet and "
                                               "consult your health provider")

        # Test "Normal Weight" category
        normal_bmi = 22
        normal_category = bmi_calculator.get_bmi_category(normal_bmi)
        self.assertEqual(normal_category, "Normal weight: Congratulations! Your BMI is normal")

        # Test "Overweight" category
        overweight_bmi = 27
        overweight_category = bmi_calculator.get_bmi_category(overweight_bmi)
        self.assertEqual(overweight_category, "Overweight: Please exercise and eat healthy food. "
                                              "You may consult a nutritionist for further advice")

        # Test "Obesity" category
        obesity_bmi = 32
        obesity_category = bmi_calculator.get_bmi_category(obesity_bmi)
        self.assertEqual(obesity_category, "Obesity: Please consult your health provider for further advice")

    def test_calculate_bmi_metric(self): #user defined class
        """
        This function defines  test case  for the calculate_bmi method using metric units (height in cm, weight in kg).

        """
        # Test for metric units
        age = 20 # Age must be 20 or above
        # Set the units for height and weight
        height_unit = 'cm'
        weight_unit = 'kg'
        # Height and weight values in metric units
        height = 170
        weight = 70

        bmi_calculator = BMICalculator(age)# Create an instance of the BMICalculator with the specified age.
        bmi_calculator.set_units(height_unit, weight_unit)# Set the units and values for height and weight.
        bmi_calculator.height = height
        bmi_calculator.weight = weight

        # Calculate the BMI and check if it's approximately equal to the expected result.
        result = bmi_calculator.calculate_bmi()
        self.assertAlmostEqual(result, 24.22, places=2)


if __name__ == '__main__':
    unittest.main() # Run the unit tests defined in this script.




