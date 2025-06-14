import unittest
from todo import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList()
        self.task1 = self.todo.add_task("Estudar Python")
        self.task2 = self.todo.add_task("Fazer exercícios")

    # Testes básicos
    def test_add_task(self):
        task = self.todo.add_task("Nova tarefa")
        self.assertEqual(task["description"], "Nova tarefa")
        self.assertFalse(task["completed"])
    
    def test_list_tasks(self):
        tasks = self.todo.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["description"], "Estudar Python")
    
    def test_complete_task(self):
        completed_task = self.todo.complete_task(self.task1["id"])
        self.assertTrue(completed_task["completed"])
    
    # Testes de erro
    def test_complete_invalid_id(self):
        with self.assertRaises(ValueError):
            self.todo.complete_task(999)
    
    def test_remove_task(self):
        removed = self.todo.remove_task(self.task1["id"])
        self.assertEqual(removed["id"], self.task1["id"])
        self.assertEqual(len(self.todo.list_tasks()), 1)
    
    def test_remove_invalid_id(self):
        with self.assertRaises(ValueError):
            self.todo.remove_task(999)
    
    # Testes de validação
    def test_empty_description(self):
        with self.assertRaises(ValueError):
            self.todo.add_task("")
    
    def test_search_tasks(self):
        self.todo.add_task("Comprar leite")
        results = self.todo.search_tasks("leite")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["description"], "Comprar leite")
    
    # Testes de estado
    def test_task_id_increment(self):
        task3 = self.todo.add_task("Terceira tarefa")
        self.assertEqual(task3["id"], 3)
        task4 = self.todo.add_task("Quarta tarefa")
        self.assertEqual(task4["id"], 4)
    
    def test_complete_removed_task(self):
        task_id = self.task1["id"]
        self.todo.remove_task(task_id)
        with self.assertRaises(ValueError):
            self.todo.complete_task(task_id)
    
    # Testes de integridade
    def test_list_after_remove(self):
        self.todo.remove_task(self.task1["id"])
        tasks = self.todo.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["id"], self.task2["id"])
    
    def test_search_case_insensitive(self):
        results = self.todo.search_tasks("pYtHoN")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], self.task1["id"])
    
    def test_complete_already_completed(self):
        self.todo.complete_task(self.task1["id"])
        task = self.todo.complete_task(self.task1["id"])
        self.assertTrue(task["completed"])
    
    def test_add_whitespace_task(self):
        with self.assertRaises(ValueError):
            self.todo.add_task("   ")
    
    def test_search_empty(self):
        results = self.todo.search_tasks("inexistente")
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()