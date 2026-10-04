class JunkItem:
    def __init__(self, name: str, quantity: int, value: float):
        self.name = name
        self.quantity = quantity
        self.value = value

    def __repr__(self):
        return f"JunkItem('{self.name}', {self.quantity}, {self.value})"

class StorageBackend:
    def save(self, items: list[JunkItem]) -> None:
        raise NotImplementedError("Цей метод треба реалізувати у дочірньому класі")

    def load(self) -> list[JunkItem]:
        raise NotImplementedError("Цей метод треба реалізувати у дочірньому класі")

class FileJunkStorage(StorageBackend):
    def __init__(self, filename: str):
        self.filename = filename

    def save(self, items: list[JunkItem]) -> None:
        with open(self.filename, 'w', encoding='utf-8') as f:
            for item in items:
                val_str = str(item.value).replace('.', ',')
                f.write(f"{item.name}|{item.quantity}|{val_str}\n")

    def load(self) -> list[JunkItem]:
        items = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    
                    parts = line.split('|')
                    
                    if len(parts) != 3:
                        print(f"[Увага] Рядок {line_num} не має 3 полів: '{line}'. Пропускаємо.")
                        continue
                    
                    name, qty_str, val_str = parts
                    
                    try:
                        quantity = int(qty_str)
                        value = float(val_str.replace(',', '.'))
                        items.append(JunkItem(name, quantity, value))
                    except ValueError:
                        print(f"[Увага] Рядок {line_num} має неправильний тип даних (не число). Пропускаємо.")
        except FileNotFoundError:
            print("Сховище порожнє або файл ще не створено.")
            
        return items

def warehouse_manager(storage: StorageBackend):
    my_junk = [
        JunkItem("Бляшанка", 5, 2.5),
        JunkItem("Стара плата", 3, 7.8),
        JunkItem("Купка дротів", 10, 1.2)
    ]
    
    print("--- Зберігаємо барахло ---")
    storage.save(my_junk)
    print("Збережено успішно.\n")

    with open("warehouse.txt", "a", encoding="utf-8") as f:
        f.write("Просто якийсь текст без роздільників\n")
        f.write("Зламана деталь|багато|дорого\n")

    print("--- Зчитуємо барахло назад ---")
    restored_junk = storage.load()
    for item in restored_junk:
        print(item)


if __name__ == "__main__":

    current_storage = FileJunkStorage("warehouse.txt")
    

    warehouse_manager(current_storage)