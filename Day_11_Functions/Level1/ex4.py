# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, # convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(temp_cel):
    temp_fer = (temp_cel* (9/5)) + 32
    return temp_fer


print(convert_celsius_to_fahrenheit(14))