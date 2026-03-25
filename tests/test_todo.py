from app.todo import TodoList

def test_add_task():
    todo = TodoList()
    todo.add_task("Estudar CI/CD")
    assert "Estudar CI/CD" in todo.get_tasks()

def test_remove_task():
    todo = TodoList()
    todo.add_task("Tarefa")
    todo.remove_task("Tarefa")
    assert "Tarefa" not in todo.get_tasks()


def test_fail(): #o erro está aqui
    todo = TodoList()
    todo.add_task("Erro")
    assert "Outra coisa" in todo.get_tasks()