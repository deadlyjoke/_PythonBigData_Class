def cauculate_bmi(h:int, w:int)->float:
    return w / ((h / 100) ** 2)
# BMI Calculator
# This program calculates the Body Mass Index (BMI) based on user input for height and weight.
def get_state(b:float)->str:
    if b < 18.5:
        return "Underweight"
    elif b < 24:
        return "Normal weight"
    elif b < 27:
        return "Overweight"
    elif b < 30:
        return "Obesity I"
    elif b < 35:
        return "Obesity II"
    else:
        return "Obesity III"
height:int = int(input("Enter your height in cm: "))
weight:int = int(input("Enter your weight in kg: "))

bmi = cauculate_bmi(height, weight)
print(bmi)
print(get_state(bmi))
# BMI Categories
if __name__ == "__main__":
     main()