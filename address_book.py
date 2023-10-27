import pickle

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def search_records(self, query):
        results = []
        for record in self.records:
            if query in record.name.first_name or query in record.name.last_name or query in record.phone.number:
                results.append(record)
        return results

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.records, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.records = pickle.load(file)
        except FileNotFoundError:
            self.records = []
