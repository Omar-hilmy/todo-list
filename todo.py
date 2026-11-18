# To-Do List by Omar Hilmy

tasks = []

while True:
    print("\n=== My To-Do List ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose 1/2/3/4: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("✅ Task added!")
    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    elif choice == "3":
        num = int(input("Task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Deleted: {removed}")
        else:
            print("Wrong number!")
    elif choice == "4":
        print("Bye! 👋")
        break
    else:
        print("Wrong choice!")
