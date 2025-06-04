def print_header(title: str):
    print("=" * len(title))
    print(title)
    print("=" * len(title))


def print_tasks(tasks: list[dict]):
    if not tasks:
        print("Список задач пуст.")
    else:
        print_header("Список задач")
        for task in tasks:
            print(f"[{task['id']}] {task['description']}")
