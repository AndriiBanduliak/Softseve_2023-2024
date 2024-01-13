def convert_to_fahrenheit(celsius):

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def main():

    celsius = float(input("Enter the temperature in Celsius: "))

    # Check if the temperature is below absolute zero.
    if celsius < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
    else:
        fahrenheit = convert_to_fahrenheit(celsius)
        print("{}°C is equivalent to {}°F".format(celsius, fahrenheit))


main()
