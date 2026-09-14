deals = [
    ("Олексій", 50, "clean"),
    ("Остап", 550.5, "suspicious"),
    ("Олена", 1200, "fraud"),
    ("Пазігор", "bb100000", "clean"),
    ("Сергій", 1500, "unknown"),
    ("Яна", 999, "clean"),
]

for deal in deals:
    name, amount, status = deal

    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        print(f"{name}: Фальшиві дані")
        continue

    if amount < 100:
        amount_category = "Дрібнота"
    elif amount <= 999:
        amount_category = "Середнячок"
    else:
        amount_category = "Великий клієнт"

    match status:
        case "clean":
            status_decision = "Працювати без питань"
        case "suspicious":
            status_decision = "Перевірити документи"
        case "fraud":
            status_decision = "У чорний список"
        case _:
            status_decision = "Невідомий статус"


    print(f"{name}: {amount_category}, {status_decision}")