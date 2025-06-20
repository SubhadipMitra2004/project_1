# Simple To-Do List in Python

todo_list = []

def show_menu():
    print("\n------ TO-DO-LIST ------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list):
            status = "👍 Done" if task['done'] else "❌ Not Done"
            print(f"{i+1}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    todo_list.append({'title': title, 'done': False})
    print("Task added successfully!")

def mark_task_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]['done'] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed = todo_list.pop(task_num)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_task_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
