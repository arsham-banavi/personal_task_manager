from tasks import tasks_list, add_tasks

print("Welcome!")
name = input("Enter username: ")

add_tasks()

print("------")
print(f"{name}'s current tasks: ")
if tasks_list == []:
    print("no tasks")
else:
    for i in tasks_list:
        print(f" - {i}")