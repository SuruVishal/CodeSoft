tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Done")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nYour list is empty.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            status = "[✓]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task['name']}")

def add_task():
    name = input("Enter the task: ")
    tasks.append({"name": name, "done": False})
    print("Task added.")

def mark_done():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to mark done: ")) - 1
            tasks[index]["done"] = True
            print("Task updated.")
        except (ValueError, IndexError):
            print("Invalid number.")

def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            tasks.pop(index)
            print("Task removed.")
        except (ValueError, IndexError):
            print("Invalid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()