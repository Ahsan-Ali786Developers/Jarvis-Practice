from database import complete_task,add_task, show_task
from files import organize_downloads as org
org(r"C:\Users\as\Desktop\New")

print("JARVIS ready. Type 'help' for commands.")
while True:
	
	cho = input("Enter your choice : ").lower()
	if cho=="help":
		print('''complete task\nadd_task\nshow_task\nexit''')
	elif cho=="exit":
		print("Your are exitting from the jarvis.\nTake care of your self.")
		break
	elif cho in ['add', 'add_task']:
		t=input("Enter your task : ")
		add_task(t)
	elif cho in ['show', 'show_task']:
		show_task()
	elif cho in ["complete_task", "Task", 'complete']:
		id = int(input("Enter id of task : "))
		complete_task(id)
	else:
		print("unknow command. type 'help' for knowing the yet available commands.")