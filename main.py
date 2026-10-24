
def main():
    tasks = []

    while True:
        print("======Welcome to To Do List App======")
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        confirmation = input("Do you wanna check your tasks. Enters (y/n): ")
        if confirmation == "n":
            print("Thank you for using To-Do-List App. Goodbye!")
            break
        elif confirmation == "y":
            print("\n=====Get started=====")
            try:
                choice = int(input("Enter your options above: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value: ")
                continue

            if choice == 1:
                if not tasks:
                    print("There are no tasks in your list.")
                else:
                    for index, task in enumerate(tasks):
                        stat = "✔" if task["completed"] else "✘"
                        print(f"{index + 1}. {task['name']} [{stat}]")

            elif choice == 2:
                task_name = input("Enter the name of your new task: ").strip()
                tasks.append({"name": task_name, "completed": False})

            elif choice == 3:
                try:
                    task_number = int(
                        input("Enter the number of the task you completed: ")) - 1
                    if 0 <= task_number < len(tasks):
                        tasks[task_number]["completed"] = True
                        print(
                            f"Task {tasks[task_number]['name']} marked as completed.")
                    else:
                        print("Invalid task number. Please try again.")

                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

            elif choice == 4:
                try:
                    task_number = int(
                        input("Enter the number of the task you wanna delete: ")) - 1
                    if 0 <= task_number < len(tasks):
                        deleted_task = tasks.pop(task_number)
                        print(f"Task '{deleted_task['name']}' deleted.")
                    else:
                        print("Invalid task number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            elif choice == 5:
                print("Thank you for using To-Do-List App. Goodbye!")

        else:
            print("invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
