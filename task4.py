def celsius_to_kelvin(c):
    return c + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def celsius_to_fahrenheit(c):
    return (c * 1.8) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8


def fahrenheit_to_kelvin(f):
    return (f + 459.67) / 1.8


def kelvin_to_fahrenheit(k):
    return (k * 1.8) - 459.67


temperature_data = [("Фаренгейт", 98.6), ("Кельвин", 310.15), ("Цельсий", 37.0)]

for scale, temp in temperature_data:
    if scale == "Фаренгейт":
        print(f"Кельвин: {fahrenheit_to_kelvin(temp)}, Цельсий: {fahrenheit_to_celsius(temp)}")
    elif scale == "Кельвин":
        print(f"Фаренгейт: {kelvin_to_fahrenheit(temp)}, Цельсий: {kelvin_to_celsius(temp)}")
    elif scale == "Цельсий":
        print(f"Фаренгейт: {celsius_to_fahrenheit(temp)}, Кельвин: {celsius_to_kelvin(temp)}")

temperature_converted = []


def convert_temperature_to_celsius(temp_data):
    temperature_converted = []
    for unit, value in temp_data:
        if unit == "Фаренгейт":
            celsius = (value - 32) * 5 / 9
            temperature_converted.append(("Цельсий", celsius))
        elif unit == "Кельвин":
            celsius = value - 273.15
            temperature_converted.append(("Цельсий", celsius))
        elif unit == "Цельсий":
            temperature_converted.append(("Цельсий", value))
    return temperature_converted


converted_temperatures = convert_temperature_to_celsius(temperature_data)
print(converted_temperatures)
