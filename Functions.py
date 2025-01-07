

def convert_temperature(temperature, scale):
    """Converts temperature between Celsius and Fahrenheit."""
    if scale == "C":
        return (temperature * 9/5) + 32  # Celsius to Fahrenheit
    elif scale == "F":
        return (temperature - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid scale"

# Example
print(convert_temperature(0, "C"))  # Celsius to Fahrenheit
print(convert_temperature(32, "F"))  # Fahrenheit to Celsius