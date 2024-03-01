def calculate_bmi(weight, height):
    """Calculates the Body Mass Index (BMI) for a given weight and height.

    Args:
        weight (float): Weight in kilograms. Must be positive.
        height (float): Height in meters. Must be positive.

    Returns:
        float: The calculated BMI.

    Raises:
        ValueError: If weight or height is not a positive value.
    """

    if weight <= 0 or height <= 0:
        raise ValueError("Both weight and height must be positive values.")

    return weight / height ** 2


def categorize_bmi(bmi):
    """Categorizes the BMI based on standard ranges.

    Args:
        bmi (float): The calculated BMI.

    Returns:
        str: The BMI category (e.g., "Underweight", "Normal weight", etc.).
    """

    categories = {
        "Underweight": 18.5,
        "Normal weight": 25,
        "Overweight": 30,
        "Obese": float("inf"),
    }

    for category, upper_bound in categories.items():
        if bmi < upper_bound:
            return category


def get_user_input(prompt):
    """Prompts the user for input, ensuring it's a valid positive number.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        float: The valid input from the user.
    """

    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Please enter a positive value.")
            return value
        except ValueError:
            print("Invalid input format. Please enter a positive number only.")


def main():
    try:
        weight = get_user_input("Enter your weight in kilograms (e.g. 70): ")
        height = get_user_input("Enter your height in meters (e.g. 1.75): ")

        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        print(f"Your BMI is {bmi:.2f}. You are classified as {category}.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
