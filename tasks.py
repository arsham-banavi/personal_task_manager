tasks_list = []

def add_tasks():
    new_tasks = True
    while new_tasks:
        task = input("Enter a task (`q` to stop): ")
        if task.lower() == "q":
            new_tasks = False
            break
        tasks_list.append(task)
        continue