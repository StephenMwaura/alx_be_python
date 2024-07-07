FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
    
def convert_to_celsius(fahrenheit):
    return(fahrenheit -32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius  * CELSIUS_TO_FAHRENHEIT_FACTOR + 32 

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F)")

        if unit == 'C':
           converted_temperature = convert_to_fahrenheit
           print(f"{temperature} is converted to, {converted_temperature}")
        elif unit == 'f':
           converted_temperature = convert_to_celsius
           print(f"{temperature} is converted to {converted_temperature}")
        else:
          print("Invalid unit")
    except ValueError:
        print("Invalid temperature.") 


if __name__ == "__main__":
    main()
