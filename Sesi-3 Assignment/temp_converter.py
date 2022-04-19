def convert(value, temp):
    if(temp == 'K'): # kelvin => celcius
        result = value - 273
    elif(temp == 'C'): # celcius => kelvin
        result = value + 273
    return round(result, 2)

def convert_to_fahrenheit(value, temp):
    if(temp == 'C'): # celcius => fahrenheit
        result = (9/5) * value + 32
    elif(temp == 'K'): # kelvin => fahrenheit
        result = convert_to_fahrenheit(convert(value, 'K'), 'C')
    return round(result, 2)

def convert_from_fahrenheit(value, temp):
    if(temp == 'C'): # fahrenheit => celcius
        result = (5/9) * (value - 32)
    elif(temp == 'K'): # fahrenheit => kelvin
        result = convert(convert_from_fahrenheit(value, 'C'), 'C')
    return round(result, 2)