import json


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def generate_unique_id(self):
        if not self.tasks:
            return 1
        else:
            return max(task["id"] for task in self.tasks) + 1

    def add_task(self):
        title = input("Podaj tytuł zadania: ")
        description = input("Podaj opis zadania: ")
        due_date = input("Podaj termin wykonania (RRRR-MM-DD): ")

        task = {
            "id": self.generate_unique_id(),
            "title": title,
            "description": description,
            "due_date": due_date
        }

        self.tasks.append(task)
        self.save_tasks()

        print("Zadanie zostało dodane.")

    def display_task(self, task, show_description=False):
        print(f"ID: {task['id']}")
        print(f"Tytuł: {task['title']}")
        print(f"Termin wykonania: {task['due_date']}")
        if show_description:
            print(f"Opis: {task['description']}")

    def display_tasks(self):
        if self.tasks:
            for task in self.tasks:
                self.display_task(task)
                print()  # Pusta linia dla czytelności
        else:
            print("Brak zapisanych zadań.")

    def remove_task(self):
        task_id = self.get_valid_task_id("Podaj ID zadania do usunięcia: ")

        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Zadanie zostało usunięte.")
                self.update_ids()  # Aktualizacja ID po usunięciu
                return

        print("Nie znaleziono zadania o podanym ID.")

    def update_task(self):
        task_id = self.get_valid_task_id("Podaj ID zadania do aktualizacji: ")

        for task in self.tasks:
            if task["id"] == task_id:
                title = input("Podaj nowy tytuł zadania (naciśnij Enter, aby pominąć): ")
                description = input("Podaj nowy opis zadania (naciśnij Enter, aby pominąć): ")
                due_date = input("Podaj nowy termin wykonania (naciśnij Enter, aby pominąć): ")

                if title:
                    task["title"] = title
                if description:
                    task["description"] = description
                if due_date:
                    task["due_date"] = due_date

                self.save_tasks()
                print("Zadanie zostało zaktualizowane.")
                return

        print("Nie znaleziono zadania o podanym ID.")

    def manual_save_tasks(self):
        self.save_tasks()
        print("Zadania zostały zapisane do pliku.")

    def display_task_description(self):
        task_id = self.get_valid_task_id("Podaj ID zadania, którego opis chcesz wyświetlić: ")

        for task in self.tasks:
            if task["id"] == task_id:
                self.display_task(task, show_description=True)
                return

        print("Nie znaleziono zadania o podanym ID.")

    def start(self):
        self.display_tasks()  # Wyświetlanie bieżących zadań od razu po uruchomieniu

        while True:
            print("===== ToDo Lista =====")
            print("1. Dodaj nowe zadanie")
            print("2. Wyświetl zadania")
            print("3. Usuń zadanie")
            print("4. Aktualizuj zadanie")
            print("5. Wyświetl opis zadania")
            print("6. Zapisz zadania do pliku")
            print("7. Wyjście")

            choice = input("Wybierz opcję: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.display_tasks()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                self.update_task()
            elif choice == "5":
                self.display_task_description()
            elif choice == "6":
                self.manual_save_tasks()
            elif choice == "7":
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

        print("Dziękujemy za skorzystanie z ToDo Listy.")

    def get_valid_task_id(self, prompt):
        while True:
            try:
                task_id = int(input(prompt))
                if self.is_valid_task_id(task_id):
                    return task_id
                else:
                    print("Nieprawidłowe ID zadania. Spróbuj ponownie.")
            except ValueError:
                print("Nieprawidłowe ID zadania. Spróbuj ponownie.")

    def is_valid_task_id(self, task_id):
        return any(task["id"] == task_id for task in self.tasks)

    def update_ids(self):
        for i, task in enumerate(self.tasks):
            task["id"] = i + 1


# Uruchomienie programu
todo_list = ToDoList()
todo_list.start()
