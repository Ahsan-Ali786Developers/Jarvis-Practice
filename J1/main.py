from database import complete_task,add_task, show_task,delete_task,add_notes,show_notes
from files import organize_downloads,create_folder	
from datetime import datetime as dt
import os
import psutil


print("JARVIS ready. Type 'help' for commands.")
while True:
	now = dt.now()
	cho = input("Enter your choice : ").lower()
	if cho=="help":
		print('''complete task\tadd_task\tshow_task\tshut\texit''')
	elif cho in ['system','status']:
		disk = psutil.disk_usage('/')
		print(f"Disk usage: {disk.percent}\n total:{disk.total}\nfree {disk.free}\n")
		memory = psutil.virtual_memory()
		print(f"Ram usage : {memory.percent}\ntotal : {memory.total}\nFree : {memory.free}")
	elif cho in ['search']:	
		sear = input("What do you want to search? ")
		cmd = f"https://www.google.com/search?q={sear}"
		print(f"{sear} is searching..")
		os.system(f"start {cmd}")
	elif cho in ['hay','hey','greet','hello','hy']:
		hour = now.hour
		if hour < 12:
			print("Good morning, Ahsan")
		elif hour >= 12 and hour < 17:
			print("Good afternoon, Ahsan")
		else:
			print("Good evening,Ahsan")
		
	elif cho=="exit":
		print("Your are exitting from the jarvis.\nTake care of your self.")
		break
	elif cho in ['date']:
		current_date = now.strftime("%Y-%m-%d")
		print(current_date)
	elif cho in ['time']:
		current_time = now.strftime("%I-%M-%S %p")
		print(current_time)
	elif cho in ['create_folder','create-folder','make-folder','make_folder']:
		flna = input("Enter your folder name : ")
		create_folder(flna)
		print(f"The {flna} folder is created successfully!")
	elif cho in ['organize-downloads','organize_downloads','organize']:
		fldna = input("Enter your folder address whose you want to organize : ")
		organize_downloads(fldna)
	elif cho in ['lock']:
		print("Your system is locking..")
		os.system("rundll32.exe user32.dll,LockWorkStation")

	elif cho in ['restart', 'refresh','re']:
		confirm = input("Are you sure you want to restart? (yes/no) : ").lower()	
		if confirm == 'yes':
			print("Your pc is restarting...")
			os.system("shutdown /r /t 5")
			break
		if confirm=='no':
			print("You cancelled the restarting of your system.")
			
	elif cho in ["shutdown", 'shut down']:
		confirm = input("Are you sure you want to shut down? (yes/no) : ").lower()
		if confirm == 'yes':
			print("Shutting down. Good bye ,Ahsan.")
			os.system("shutdown /s /t 5")
			break 
		else:
			print("Shutdown Cancelled.")
	elif cho in ['open']:
		app = input("Which app?")
		if app in ['notepad']:
			print("Notepad is opening...")
			os.system('notepad')
		elif app in ['calc','calculator']:
			print("Calculator is opening...")
			os.system("calc")
	
		elif app in ['chrome']:
			print("Chrome is opening...")
			os.system('start chrome')
	elif cho in ['add', 'add_task']:
		t=input("Enter your task : ")
		add_task(t)
	elif cho in ['show', 'show_task']:
		show_task()
	elif cho in ["complete_task", "Task", 'complete']:
		id = int(input("Enter id of task : "))
		complete_task(id)
	elif cho in ['delete', 'delete_task']:
		id = int(input("Enter id of task : "))
		delete_task(id)
	elif cho in ['remember']:
		text = input("Enter your text for notes : ")
		add_notes(text)
	elif cho in ['notes']:
		show_notes()		
	else:
		print("unknow command. type 'help' for knowing the yet available commands.")