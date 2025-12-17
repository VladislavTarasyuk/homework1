import csv


def load_csv(filepath: str) -> list[dict]:
    """Загружает CSV-файл"""
    with open(filepath, encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return [normalize_row(row) for row in reader]


def normalize_row(row: dict) -> dict:
    """Очищает значения от пробелов"""
    return {key.strip(): value.strip() for key, value in row.items()}


def normalize_gender(sex: str) -> tuple[str, str]:
    """Возвращает текст пола и корректный глагол"""
    if sex.lower() == "female":
        return "женского пола", "совершила"
    return "мужского пола", "совершил"


def normalize_device(device: str) -> str:
    """Преобразует тип устройства"""
    device_map = {
        "mobile": "мобильного",
        "desktop": "десктопного",
        "tablet": "планшетного"
    }
    return device_map.get(device.lower(), device)


def build_description(client: dict) -> str:
    gender_text, verb = normalize_gender(client["sex"])

    return (
        f"Пользователь {client['name']} {gender_text}, {client['age']} лет "
        f"{verb} покупку на {client['bill']} у.е. "
        f"с {normalize_device(client['device_type'])} браузера {client['browser']}. "
        f"Регион, из которого совершалась покупка: {client['region']}."
    )


def generate_descriptions(clients: list[dict]) -> list[str]:
    """Генерирует описания пользователей"""
    return [build_description(client) for client in clients]


def save_to_txt(descriptions: list[str], filepath: str) -> None:
    """Сохраняет результат в TXT-файл"""
    with open(filepath, "w", encoding="utf-8") as file:
        file.write("\n\n".join(descriptions))


def main(input_csv: str, output_txt: str) -> None:
    clients = load_csv(input_csv)
    descriptions = generate_descriptions(clients)
    save_to_txt(descriptions, output_txt)


if __name__ == "__main__":
    main("web_clients_correct.csv", "clients_description.txt")