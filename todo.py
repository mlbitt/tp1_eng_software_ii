import json


class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self._load_tasks()
        if self.tasks:
            self.next_id = max(task["id"] for task in self.tasks) + 1
        else:
            self.next_id = 1

    def _load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description):
        if not description.strip():
            raise ValueError("Descrição não pode ser vazia")
        task = {"id": self.next_id, "description": description, "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        self._save_tasks()
        return task

    def list_tasks(self):
        return self.tasks.copy()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self._save_tasks()
                return task
        raise ValueError("Tarefa não encontrada")

    def remove_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed_task = self.tasks.pop(i)
                self._save_tasks()
                return removed_task
        raise ValueError("Tarefa não encontrada")

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task["description"].lower()]