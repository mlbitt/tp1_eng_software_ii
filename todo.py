class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        if not description.strip():
            raise ValueError("Descrição não pode ser vazia")
        task = {"id": self.next_id, "description": description, "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return self.tasks.copy()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return task
        raise ValueError("Tarefa não encontrada")

    def remove_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                return self.tasks.pop(i)
        raise ValueError("Tarefa não encontrada")

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task["description"].lower()]