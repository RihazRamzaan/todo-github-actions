tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})

def list_tasks():
    if not tasks:
        return "No tasks yet."
    return "\n".join(
        f"  {'✓  ' if t['done'] else '○  '} {i+1}. {t['title']}"
        for i, t in enumerate(tasks)
    )

def mark_done(n):
    if 1 <= n <= len(tasks):
        tasks[n - 1]["done"] = True
        return True
    return False

if __name__ == "__main__":
    while True:
        cmd = input("\n[a]dd  [l]ist  [d]one  [q]uit :").strip().lower()
        if cmd == "a":
            add_task(input("Task: "))
        elif cmd == "l":
            print(list_tasks())
        elif cmd == "d":
            n = input("Mark done #: ")
            if n.isdigit():
                mark_done(int(n))
        elif cmd == "q":
            break