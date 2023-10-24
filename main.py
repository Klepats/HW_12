import pickle

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query in contact.name or query in contact.phone:
                results.append(contact)
        return results

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = []

def main():
    address_book = AddressBook()

    try:
        address_book.load_from_file('address_book.pickle')
    except:
        print("Помилка при завантаженні даних з файлу.")

    while True:
        print("1. Додати контакт")
        print("2. Пошук контакту")
        print("3. Зберегти та вийти")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            contact = Contact(name, phone)
            address_book.add_contact(contact)
        elif choice == '2':
            query = input("Введіть ім'я або номер телефону для пошуку: ")
            results = address_book.search_contacts(query)
            if results:
                print("Результати пошуку:")
                for result in results:
                    print(f"Ім'я: {result.name}, Телефон: {result.phone}")
            else:
                print("Немає збігів.")
        elif choice == '3':
            address_book.save_to_file('address_book.pickle')
            break

if __name__ == '__main__':
    main()
