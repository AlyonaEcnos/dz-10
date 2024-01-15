from collections import UserDict

class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError(f"Invalid {self.__class__.__name__.lower()} value")
        self.value = value

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        return True

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def is_valid(self, value):
        return isinstance(value, str) and len(value) == 10 and value.isdigit()

    def validate(self):
        if not self.is_valid(self.value):
            raise ValueError(f"Invalid {self.__class__.__name__.lower()} format")

    def __str__(self):
        return str(self.value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        initial_len = len(self.phones)
        self.phones = [p for p in self.phones if p.value != phone]
        if len(self.phones) == initial_len:
            raise ValueError(f"Phone number '{phone}' not found")

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                p.validate()
                return
        raise ValueError(f"Phone number '{old_phone}' not found")

    def find_phone(self, phone):
        found_numbers = [p for p in self.phones if p.value == phone]
        return found_numbers[0] if found_numbers else None

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
