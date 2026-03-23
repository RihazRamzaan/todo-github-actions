tasks = []

while True:
    cmd = input("\n[a]dd  [l]ist  [d]one  [q]uit: ").strip().lower()

    if cmd == "a":
        tasks.append({"title": input("Task: "), "done": False})
    elif cmd == "l":
        print("\n" + ("\n".join(f"  {'✓  ' if t['done'] else '○  '} {i+1}. {t['title']}"
                                for i, t in enumerate(tasks)) or "  No tasks yet."))
    elif cmd == "d":
        n = input("Mark done #: ")
        if n.isdigit() and 1 <= int(n) <= len(tasks):
            tasks[int(n)-1]["done"] = True
    elif cmd == "q":
        break