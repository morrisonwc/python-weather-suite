# temperatureconvert.py

def fahrenheitToCelsius(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) * 5 / 9
    return celsius_temp

def celsiusToFahrenheit(celsius_temp):
    fahrenheit_temp = 9 / 5 * celsius_temp + 32
    return fahrenheit_temp


def main():
    while (True):
        print("\n*****************************************************")
        print("Please choose a conversion:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Exit")
        print("*****************************************************")
        
        user_choice = int(input("Enter number: "))
        if user_choice == 1:
            user_fahrenheit = float(input("Enter Fahrenheit temperature: "))
            print(f"The Celsius temperature is: {fahrenheitToCelsius(user_fahrenheit)}\n")
            continue
        elif user_choice == 2:
            user_celsius = float(input("Enter Celsius temperature: "))
            print(f"The Fahrenheit temperature is: {celsiusToFahrenheit(user_celsius)}\n")
            continue
        elif user_choice == 3:
            print("Thank you for using this conversion program!\n")
            break
        else:
            print("That value is invalid, please enter integers 1 to 3.")

main()