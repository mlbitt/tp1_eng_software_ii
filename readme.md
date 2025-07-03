# Sistema de Lista de Tarefas

## Autor
Marcos Aguilar

## Explicação do Sistema
Sistema de gerenciamento de tarefas com as seguintes operações:
- Adicionar novas tarefas com descrição
- Listar todas as tarefas
- Marcar tarefas como completas
- Remover tarefas
- Buscar tarefas por palavra-chave
- Validação de dados e tratamento de erros
- Persistência de dados em arquivo JSON

## Como Usar

O sistema é utilizado de forma interativa através da linha de comando. Para iniciar, execute o seguinte comando:

```bash
python3 main.py

```

Após iniciar, você pode usar os seguintes comandos diretamente no terminal. Para sair, digite `exit`.

### Adicionar uma Tarefa

Use o comando `add` seguido da descrição da tarefa.

```
> add Comprar pão
```

### Listar todas as Tarefas

Use o comando `list` para ver todas as tarefas, seus IDs e status.

```
> list
```

**Exemplo de saída:**
```
ID: 1 - [ ] Comprar pão
ID: 2 - [ ] Fazer exercícios
```

### Marcar uma Tarefa como Concluída

Use o comando `complete` seguido do ID da tarefa.

```
> complete 1
```

### Remover uma Tarefa

Use o comando `remove` seguido do ID da tarefa.

```
> remove 2
```

### Buscar Tarefas

Use o comando `search` seguido de uma palavra-chave para encontrar tarefas.

```
> search pão
```

## Tecnologias Utilizadas
- **Linguagem**: Python 3.9
- **Testes**: Unittest (framework nativo do Python)
- **CI/CD**: GitHub Actions
- **Sistemas Operacionais Testados**: Windows, Linux e macOS