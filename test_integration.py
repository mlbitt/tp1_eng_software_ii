import unittest
import os
import json
from todo import TodoList

class TestTodoIntegration(unittest.TestCase):

    def setUp(self):
        """
        Cria um arquivo de tarefas de teste antes de cada teste.
        """
        self.test_filename = "test_tasks.json"
        # Garante que o arquivo de teste não existe antes de cada teste
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        self.todo = TodoList(filename=self.test_filename)

    def tearDown(self):
        """
        Remove o arquivo de tarefas de teste após cada teste.
        """
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_1_add_and_load_persistence(self):
        """
        Testa se uma tarefa adicionada persiste e é carregada por uma nova instância.
        """
        # Adiciona uma tarefa
        self.todo.add_task("Tarefa Persistente")

        # Cria uma nova instância da TodoList para carregar do arquivo
        new_todo = TodoList(filename=self.test_filename)
        tasks = new_todo.list_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Tarefa Persistente")
        self.assertFalse(tasks[0]["completed"])

    def test_2_complete_task_persistence(self):
        """
        Testa se o estado 'completed' de uma tarefa persiste.
        """
        task = self.todo.add_task("Tarefa para completar")
        self.todo.complete_task(task["id"])

        # Cria uma nova instância para verificar a persistência
        new_todo = TodoList(filename=self.test_filename)
        tasks = new_todo.list_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertTrue(tasks[0]["completed"])

    def test_3_remove_task_persistence(self):
        """
        Testa se a remoção de uma tarefa persiste.
        """
        task = self.todo.add_task("Tarefa para remover")
        self.todo.remove_task(task["id"])

        # Cria uma nova instância para verificar a persistência
        new_todo = TodoList(filename=self.test_filename)
        tasks = new_todo.list_tasks()

        self.assertEqual(len(tasks), 0)

    def test_4_e2e_user_workflow(self):
        """
        Testa um fluxo de trabalho completo do usuário: adicionar, listar, completar e remover.
        """
        # 1. Adicionar duas tarefas
        task1 = self.todo.add_task("Comprar pão")
        task2 = self.todo.add_task("Comprar queijo")

        # 2. Verificar se as tarefas foram adicionadas
        new_todo1 = TodoList(filename=self.test_filename)
        self.assertEqual(len(new_todo1.list_tasks()), 2)

        # 3. Completar a primeira tarefa
        new_todo1.complete_task(task1["id"])

        # 4. Verificar se a primeira tarefa foi completada
        new_todo2 = TodoList(filename=self.test_filename)
        completed_task = new_todo2.search_tasks("pão")[0]
        self.assertTrue(completed_task["completed"])

        # 5. Remover a segunda tarefa
        new_todo2.remove_task(task2["id"])

        # 6. Verificar se a segunda tarefa foi removida
        new_todo3 = TodoList(filename=self.test_filename)
        tasks = new_todo3.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Comprar pão")

    def test_5_data_integrity_after_multiple_operations(self):
        """
        Testa a integridade dos dados após várias operações, verificando o JSON diretamente.
        """
        self.todo.add_task("Primeira Tarefa")
        task2 = self.todo.add_task("Segunda Tarefa")
        self.todo.add_task("Terceira Tarefa")
        self.todo.remove_task(task2["id"])

        with open(self.test_filename, 'r') as f:
            data = json.load(f)

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["description"], "Primeira Tarefa")
        self.assertEqual(data[1]["description"], "Terceira Tarefa")
        # Verifica se os IDs estão corretos (1 e 3)
        self.assertEqual(data[0]["id"], 1)
        self.assertEqual(data[1]["id"], 3)

if __name__ == "__main__":
    unittest.main()
