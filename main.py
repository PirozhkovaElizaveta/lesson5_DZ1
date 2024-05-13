class Task:
    def __init__(self, description, deadline, is_completed=False):
        self.description = description
        self.deadline = deadline
        self.is_completed = is_completed

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        return f"Описание: {self.description}, Срок: {self.deadline}, {'Выполнено' if self.is_completed else 'Не выполнено'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append(Task(description, deadline))

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Задача с таким индексом не найдена.")

    def show_current_tasks(self):
        print("Актуальные задачи:")
        for task in self.tasks:
            if not task.is_completed:
                print(task)

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2024-05-11")
task_manager.add_task("Позвонить другу", "2024-05-15")
task_manager.mark_task_completed(2)
task_manager.show_current_tasks()