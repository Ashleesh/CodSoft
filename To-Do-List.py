import os
todo_list = []
def clear(): os.system('cls' if os.name == 'nt' else 'clear')
def add(): 
    todo_list.append(input("Enter a new task: "))
    print("Task added.")
def view():
    print("To-Do List:" if todo_list else "List is empty.")
    [print(f"{i+1}. {task}") for i, task in enumerate(todo_list)]
def remove():
    view()
    if todo_list:
        try:
            del todo_list[int(input("Task number to remove: ")) - 1]
            print("Task removed.")
        except (ValueError, IndexError):
            print("Invalid input.")
def main():
    actions = {'1': add, '2': view, '3': remove}
    while True:
        clear()
        print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Quit")

        choice = input("Choose (1-4): ")
        if choice == '4':
            print("Goodbye!")
            break
        actions.get(choice, lambda: print("Invalid choice"))()
        input("Press Enter to continue...")
if __name__ == "__main__":
    main()
