import json
from typing import List, Dict


class Task:
    """Klasa reprezentująca pojedyncze zadanie."""

    def __init__(self, task_id: int, title: str, description: str, deadline: str) -> None:
        self._id = task_id
        self._title = title
        self._description = description
        self._deadline = deadline

    def get_id(self) -> int:
        """Zwraca ID zadania."""
        return self._id

    def get_title(self) -> str:
        """Zwraca tytuł zadania."""
        return self._title

    def get_description(self) -> str:
        """Zwraca opis zadania."""
        return self._description

    def get_deadline(self) -> str:
        """Zwraca termin wykonania zadania."""
        return self._deadline

    def __str__(self) -> str:
        """Zwraca reprezentację tekstową zadania."""
        return f"ID: {self._id}, Tytuł: {self._title}, Termin: {self._deadline}"


class TaskManager:
    """Klasa zarządzająca zadaniami."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._load_tasks_from_file()

    def _load_tasks_from_file(self) -> None:
        """Wczytuje zadania z pliku tasks.json."""
        try:
            with open('tasks.json', 'r') as file:
                tasks_data = json.load(file)
                self._tasks = [Task(task['id'], task['title'], task['description'], task['deadline'])
                               for task in tasks_data]
        except FileNotFoundError:
            self._tasks = []

    def _save_tasks_to_file(self) -> None:
        """Zapisuje zadania do pliku tasks.json."""
        tasks_data = [{'id': task.get_id(), 'title': task.get_title(),
                       'description': task.get_description(), 'deadline': task.get_deadline()}
                      for task in self._tasks]
        with open('tasks.json', 'w') as file:
            json.dump(tasks_data, file)

    def add_task(self) -> None:
        """Dodaje nowe zadanie."""
        title = input("Podaj tytuł zadania: ")
        description = input("Podaj opis zadania: ")
        deadline = input("Podaj termin wykonania zadania (YYYY-MM-DD): ")
        task_id = len(self._tasks) + 1
        task = Task(task_id, title, description, deadline)
        self._tasks.append(task)
        self._save_tasks_to_file()
        print('Zadanie dodane.')

    def delete_task(self) -> None:
        """Usuwa zadanie o podanym ID."""
        task_id = int(input("Podaj ID zadania do usunięcia: "))
        self._tasks = [task for task in self._tasks if task.get_id() != task_id]
        self._save_tasks_to_file()
        print('Zadanie usunięte.')

    def update_task(self) -> None:
        """Aktualizuje zadanie o podanym ID."""
        task_id = int(input("Podaj ID zadania do aktualizacji: "))
        for task in self._tasks:
            if task.get_id() == task_id:
                title = input("Nowy tytuł zadania: ")
                description = input("Nowy opis zadania: ")
                deadline = input("Nowy termin wykonania zadania (YYYY-MM-DD): ")
                task._title = title
                task._description = description
                task._deadline = deadline
                self._save_tasks_to_file()
                print('Zadanie zaktualizowane.')
                return
        print('Zadanie o podanym ID nie istnieje.')

    def display_tasks(self) -> None:
        """Wyświetla zadania dla danego dnia tygodnia."""
        day_of_week = input("Podaj dzień tygodnia, dla którego chcesz wyświetlić zadania: ")
        matching_tasks = [task for task in self._tasks if task.get_deadline().lower() == day_of_week.lower()]
        if not matching_tasks:
            print("Brak zadań dla podanego dnia tygodnia.")
        else:
            for task in matching_tasks:
                print(task)
                show_description = input("Czy wyświetlić opis zadania? (T/N): ")
                if show_description.lower() == 't':
                    print(f"Opis: {task.get_description()}")
                print()

    def run(self) -> None:
        """Uruchamia interfejs zarządzania zadaniami."""
        self._load_tasks_from_file()
        while True:
            print("1. Dodaj nowe zadanie")
            print("2. Usuń zadanie")
            print("3. Aktualizuj zadanie")
            print("4. Wyświetl zadania dla danego dnia tygodnia")
            print("5. Wyjście")
            choice = input("Wybierz opcję (1-5): ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.delete_task()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.display_tasks()
            elif choice == '5':
                break
            else:
                print('Nieprawidłowa opcja. Wybierz ponownie.')


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
