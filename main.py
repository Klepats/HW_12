from name import Name
from phone import Phone
from record import Record
from address_book import AddressBook

def main():
    address_book = AddressBook()

    try:
        address_book.load_from_file('address_book.pickle')
    except:
        print("Помилка при завантаженні даних з файлу.")

    while True:
        print("1. Додати запис")
        print("2. Пошук запису")
        print("3. Зберегти та вийти")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            name = Name(first_name, last_name)
            number = input("Введіть номер телефону: ")
            phone = Phone(number)
            record = Record(name, phone)
            address_book.add_record(record)
        elif choice == '2':
            query = input("Введіть ім'я або номер телефону для пошуку: ")
            results = address_book.search_records(query)
            if results:
                print("Результати пошуку:")
                for result in results:
                    print(f"Ім'я та Прізвище: {result.name.first_name} {result.name.last_name}, Телефон: {result.phone.number}")
            else:
                print("Немає збігів.")
        elif choice == '3':
            address_book.save_to_file('address_book.pickle')
            break

if __name__ == '__main__':
    main()
