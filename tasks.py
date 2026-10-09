tasks_list = []
priority_list = []

def add_tasks():
    new_tasks = True
    while new_tasks:
        task = input("Enter a task (`q` to stop): ")
        if task.lower() == "q":
            new_tasks = False
            break
        priority = input("Enter task priority (low / medium / high): ")
        tasks_list.append(task)
        priority_list.append(priority)
        continue