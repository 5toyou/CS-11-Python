medicines = [
    ("Амоксицилін", 100, "antibiotic", 18.5),
    ("Вітамін C", 50, "vitamin", 3.0),
    ("Вакцина від грипу", 20, "vaccine", 28.0),
    ("Анальгін", "10", "unknown", 32.0),
    ("Крутий анальгін", 10, "unknown", "322")
]

for item in medicines:
    name, quantity, category, temperature = item

    if type(quantity) is not int or not isinstance(temperature, float):
        print(f"{name}: Помилка даних")
        continue

    if temperature < 5:
        temp_status = "Надто холодно"
    elif temperature > 25:
        temp_status = "Надто жарко"
    else:
        temp_status = "Норма"

    match category:
        case "antibiotic":
            category_status = "Рецептурний препарат"
        case "vitamin":
            category_status = "Вільний продаж"
        case "vaccine":
            category_status = "Потребує спецзберігання"
        case _:
            category_status = "Невідома категорія"


    print(f"{name}: {category_status}, {temp_status}")