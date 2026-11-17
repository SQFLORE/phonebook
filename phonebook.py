import json


class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = {}
        self.load()

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = {}

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, ensure_ascii=False, indent=4)

    def find(self, name):
        return self.contacts.get(name)

    def add(self, name, number):
        self.contacts[name] = number
        self.save()

    def count(self):
        return len(self.contacts)

    def delete(self, name):
        try:
            del self.contacts[name]
            self.save()
        except KeyError:
            print('Такого контакта нету')

    def show_all(self):
        for key, value in self.contacts.items():
            print(f'{key} - {value}')

    def rename(self, old_name, new_name):
        if old_name not in self.contacts:
            print('Такого контакта нету')
        elif old_name == new_name:
            print('Имена совпадают')
        elif new_name in self.contacts:
            print('Имя уже занято')
        else:
            self.contacts[new_name] = self.contacts.pop(old_name)
            self.save()



book = PhoneBook("contacts.json")

while True:
    command = input("Команда (найти, добавить, удалить, переименовать, список, выход): ").strip().casefold()

    if command == "выход":
        break

    elif command == "найти":
        name = input("Имя: ").strip().capitalize()
        number = book.find(name)
        if number is not None:
            print(f"Номер: {number}")
        else:
            print("Не найден")

    elif command == "добавить":
        name = input("Имя: ").strip().capitalize()
        number = input("Номер: ").strip()
        book.add(name, number)
        print("Контакт добавлен")

    elif command == "удалить":
        person = input('Имя: ').strip().capitalize()
        book.delete(person)

    elif command == "переименовать":
        old = input('Введите кого хотите переименовать: ').strip().capitalize()
        new = input('Введите новое имя: ').strip().capitalize()
        book.rename(old, new)

    elif command == "список":
        book.show_all()

    else:
        print("Неизвестная команда")