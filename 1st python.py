# bmi_calculator.py

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).
    :param weight_kg: Weight in kilograms
    :param height_m: Height in meters
    :return: BMI value
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight_kg / (height_m ** 2)

def bmi_category(bmi: float) -> str:
    """
    Determine BMI category.
    :param bmi: BMI value
    :return: Category as string
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "OBESITY GO TO THE GYM"

def main():
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
