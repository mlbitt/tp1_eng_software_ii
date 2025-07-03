from todo import TodoList

def print_tasks(tasks):
    if not tasks:
        print("Nenhuma tarefa na lista.")
    else:
        for task in tasks:
            status = "[x]" if task["completed"] else "[ ]"
            print(f"ID: {task['id']} - {status} {task['description']}")

def main():
    """
    Função principal que executa o loop interativo do sistema de tarefas.
    """
    todo = TodoList()
    print("Sistema de Lista de Tarefas Interativo.")
    print("Comandos disponíveis: add, list, complete, remove, search, exit")

    while True:
        try:
            command_input = input("> ").strip()
            if not command_input:
                continue

            parts = command_input.split(" ", 1)
            command = parts[0].lower()
            args_str = parts[1] if len(parts) > 1 else ""

            if command == "exit":
                print("Saindo do sistema...")
                break

            elif command == "add":
                if not args_str:
                    print("Erro: A descrição da tarefa não pode ser vazia.")
                    continue
                task = todo.add_task(args_str)
                print(f"Tarefa adicionada: \"{task['description']}\"")

            elif command == "list":
                tasks = todo.list_tasks()
                print_tasks(tasks)

            elif command == "complete":
                if not args_str.isdigit():
                    print("Erro: O ID da tarefa deve ser um número.")
                    continue
                task = todo.complete_task(int(args_str))
                print(f"Tarefa concluída: \"{task['description']}\"")

            elif command == "remove":
                if not args_str.isdigit():
                    print("Erro: O ID da tarefa deve ser um número.")
                    continue
                task = todo.remove_task(int(args_str))
                print(f"Tarefa removida: \"{task['description']}\"")

            elif command == "search":
                if not args_str:
                    print("Erro: A palavra-chave da busca não pode ser vazia.")
                    continue
                tasks = todo.search_tasks(args_str)
                if not tasks:
                    print(f"Nenhuma tarefa encontrada com a palavra-chave: \"{args_str}\"")
                else:
                    print_tasks(tasks)
            
            else:
                print(f"Comando desconhecido: '{command}'")

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
