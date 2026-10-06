print("Welcome!")
name = input("Enter username: ")

tasks_list = []
new_tasks = True
while new_tasks:
    task = input("Enter a task (`q` to stop): ")
    if task.lower() == "q":
        new_tasks = False
        break
    tasks_list.append(task)
    continue

print("------")
print(f"{name}'s current tasks: ")
if tasks_list == []:
    print("no tasks")
else:
    for i in tasks_list:
        print(f" - {i}")