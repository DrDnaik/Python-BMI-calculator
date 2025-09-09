The program is a BMI calculator for adults 20 years and above that displays BMI, its categories and
health advice to users. It also displays customer support information to the users.
We run the project from bmi_main.py file. BMICalculator class is imported from bmi_calcualtor.py to bmi_main
bmi_main is the driver program for this project.codes are executed from here.
on running the main.py it will print the header BMI calculator followed by prompts for user to enter their data
User has to enter age,if age is 20 or more the user will be prompted to select system -metric or imperial system
once system is selected, user is prompted to enter weight and height as specified
once user enters valid weight and height following things are displayed:
for example
Enter Your Age: 34
Choose units (metric/imperial): metric
Enter your weight in kg: 45
Enter your height in cm: 152Enter Your Age: 34
Choose units (metric/imperial): metric
Enter your weight in kg: 45
Enter your height in cm: 152
Age: 34
Units: kg / cm
Weight: 45.0 kg
Height: 152.0 cm
Your BMI: 19.48
BMI Category: Normal weight: Congratulations! Your BMI is normal:
The bmi calculator is based on The Centers for Disease Control and Prevention agency recommendations
For more information, please contact at abc@abc.com and 808-123456

You can replace these values with ones of your choice.

if user enters invalid inputs like negative weight and height , incorrect name for BMI system, non numeric value for
weight and height, incorrect age,  error messages will be displayed

There is testing module to check validity of 2 public methods from the BMI calculator class
using assert command we are checking if the methods work as expected

This calculator is based on The Centers for Disease Control and Prevention, national public health agency of USA
This is the link to CDC website for deriving the calculations and various categories of BMI
https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#InterpretedAdults

