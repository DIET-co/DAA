def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate the BMI based on the input weight and height.
    
    Arguments:
    weight (float): The weight in kilograms.
    height (float): The height in meters.
    
    Returns:
    float: The calculated BMI as a float.
    """
    return weight / (height ** 2)

# Example usage:
weight = 85.0  # in kilograms
height = 1.8  # in meters

bmi = calculate_bmi(weight, height)

print(f'BMI: {bmi:.2f}')