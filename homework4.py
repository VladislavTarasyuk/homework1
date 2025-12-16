documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_owner_by_doc_number(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return None

# Функция для поиска полки по номеру документа
def get_shelf_by_doc_number(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return None

def main():
    print("Добро пожаловать!")
    print("Команды:")
    print("p - узнать владельца документа по номеру")
    print("s - узнать полку хранения документа по номеру")
    print("q - выход из программы")
    
    while True:
        command = input("Введите команду: ").strip().lower()
        
        if command == 'p':
            doc_number = input("Введите номер документа: ").strip()
            owner = get_owner_by_doc_number(doc_number)
            
            if owner:
                print(f"Владелец документа: {owner}")
            else:
                print(f"Документ с номером '{doc_number}' не найден.")


        elif command == 'q':
            print("Завершение работы программы. До свидания!")
            break
        

        elif command == 's':
            doc_number = input("Введите номер документа: ").strip()
            shelf = get_shelf_by_doc_number(doc_number)
            
            if shelf:
                print(f"Документ хранится на полке: {shelf}")
            else:
                print(f"Документ с номером '{doc_number}' не найден на полках.")


        
        else:
            print("Неизвестная команда. Пожалуйста, используйте p, s или q.")

if __name__ == "__main__":
    main()