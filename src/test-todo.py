import todo

def setup_function():
    todo.tasks.clear()

def test_add_task():
    todo.add_task("Buy milk")
    assert len(todo.tasks) == 1
    assert todo.tasks[0]["title"] == "Buy milk"
    assert todo.tasks[0]["done"] is False

def test_list_empty():
    assert todo.list_tasks() == "No tasks yet."

def test_list_tasks():
    todo.add_task("Task A")
    todo.add_task("Task B")
    result = todo.list_tasks()
    assert "Task A" in result
    assert "Task B" in result

def test_mark_done():
    todo.add_task("Finish report")
    todo.mark_done(1)
    assert todo.tasks[0]["done"] is True

def test_mark_done_invalid():
    assert todo.mark_done(99) is False