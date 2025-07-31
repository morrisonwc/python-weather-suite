# windchillcalculator.py

# The formula only applies for wind speeds in excess of 3 miles per hour
def windchillIndexCalculator(fahrenheit_temp, windspeed):
    windchill_index = 35.74 + (0.6215 * fahrenheit_temp) - 35.75 * (windspeed ** 0.16) + 0.4275 * fahrenheit_temp * (windspeed ** 0.16)
    return windchill_index

