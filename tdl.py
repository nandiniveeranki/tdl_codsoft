class TodoList:
    def __init__(se):
        se.tasks = []

    def add_task(se, task):
        se.tasks.append(task)

    def remove_task(se, index):
        if 0 <= index < len(se.tasks):
            del se.tasks[index]
            print("Task removed successfully!")
        else:
            print("Invalid task index. Please try again.")

    def display_tasks(se):
        if se.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(se.tasks):
                print(f"{i+1}. {task}")
        else:
            print("Your To-Do List is empty")

    def update_task(se, index, new_task):
        if 0 <= index < len(se.tasks):
            se.tasks[index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task index. Please try again.")

def main():
    todo_list = TodoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter task index to be removed: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter task index to be  updated: ")) - 1
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()