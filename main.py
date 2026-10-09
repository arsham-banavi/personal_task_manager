import os
from dotenv import load_dotenv
from tasks import tasks_list, add_tasks, priority_list

# admin mode
load_dotenv()
admin_pass = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
admin_mode_confirmation = input("Open admin mode? (yes/no): ")
if admin_mode_confirmation.lower() == "yes":
    user_pass = input("Enter admin password: ")
    if user_pass == admin_pass:
        print("Welcome admin!")
    else:
        print("Wrong password!")

print("Welcome!")
name = input("Enter username: ")

add_tasks()

print("------")
print(f"{name}'s current tasks: ")
if tasks_list == []:
    print("no tasks")
else:
    a = 0
    for i in tasks_list:
        print(f" - {i} - {priority_list[a]} priority")
        a += 1

with open("tasks.txt", "a") as file:
    file.write(f"{name} - {tasks_list}\n")