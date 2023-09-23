# Представьте, что у вас есть список измерений топливной эффективности автомобилей в разных масштабах, таких
# как "миль на галлон" (MPG), "километров на литр" (KPL) и "миль на литр" (MPL). Ваша задача -
# создать функцию convert_to_L_per_100KM, которая принимает список измерений и конвертирует их в
# масштаб "литры на 100 километров" (L/100KM).


# Примечание: Для конвертации MPG в L/100KM используйте формулу: L/100KM = 235.214583 /
# MPG, для KPL в L/100KM: L/100KM = 100 / KPL, и для MPL в L/100KM: L/100KM = MPL * 2.35214583.

data = [
    {"масштаб": "MPG", "значение": 25.0},
    {"масштаб": "KPL", "значение": 10.0},
    {"масштаб": "MPL", "значение": 40.0},
    {"масштаб": "MPG", "значение": 30.0}
]
converted_data = []


def convert_fuel(data):
    litres_to_hundred = "L/100KM"
    for element in data:
        if element["масштаб"] == "MPG":
            l_hundred = 235.214583 / element["значение"]
            converted_data.append({"масштаб": litres_to_hundred, "значение": l_hundred})
        elif element["масштаб"] == "KPL":
            l_hundred = 100 / element["значение"]
            converted_data.append({"масштаб": litres_to_hundred, "значение": l_hundred})
        elif element["масштаб"] == "MPL":
            l_hundred = 2.35214583 * element["значение"]
            converted_data.append({"масштаб": litres_to_hundred, "значение": l_hundred})
        else:
            print("Значения не найдены")
    return converted_data


converted_data = convert_fuel(data)

for elem in data:
    print(elem)
print("--------------------------")
for elem in converted_data:
    print(elem)