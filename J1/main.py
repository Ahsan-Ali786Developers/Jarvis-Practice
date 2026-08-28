from database import complete_task,add_task, show_task,delete_task,add_notes,show_notes
from files import organize_downloads,create_folder	
from datetime import datetime as dt
import os, psutil
from logger import log_command as log
from income import add_income, show_today_income, show_all_income,today_profit

print("JARVIS ready. Type 'help' for commands.")
while True:
	now = dt.now()
	cho = input("Enter your choice : ").lower()
	log(cho)
	if cho=="help":
		print('''1. complete task\t2. add_task\t3. show_task\t4. shutdown/turn off\t5. system/status\t6. search google\t7. greeting\t8. date\t9. time \t10. delete_task\t11. add_notes\t12. show_notes\t13. create_folder\t14. organ\rize_folder\t 15. lock \t16. restart\t17. open app\t18. add_income\t19. show_today_income \t20. show_all_income\t21. exit''')
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
			os.system("shutdown /r /t 240")
			conn = input("Do you want to cancel? ").lower()
			if conn == 'yes':
				os.system("shutdown /a")
			elif conn == 'no':
				print("Your pc is restarting...")	
		elif confirm=='no':
			print("You cancelled the restarting of your system.")
	elif cho in ["shutdown", 'shut down']:
		confirm = input("Are you sure you want to shut down? (yes/no) : ").lower()
		if confirm == 'yes':
			print("Shutting down. Good bye ,Ahsan.")
			os.system("shutdown /s /t 240")
			conn = input("Do you want to cancel? ").lower()
			if conn == 'yes':
				os.system("shutdown /a")
			elif conn == 'no':
				print("Your pc is shuting down...")	
		elif confirm=='no':
			print("You cancelled the shut down of your system.")
					
	elif cho in ['open']:
		app = input("Which app?")
		apps = {
			"notepad": "notepad",
			"calc": "calc",
			"calculator": "calc",
			"chrome" : "start chrome",
			"vscode": "code",
			"code":"code",
			"word": "start winword",
			"excel": "start excel",
			"powerpoint":"start powerpnt",
			"explorer": "explorer",
			"files":"explorer",
			"cmd":"start cmd",
			"terminal":"start cmd",
			"paint": "mspaint",
			"task manager": "taskmgr",
			"control panel":"control",
			"settings":"start ms-settings:",
			"whatsapp": "start https://web.whatsapp.com/",
			"camera":"start microsoft.windows.camera:",
			"wordpad":"write"
			}
		if app in apps:
			os.system(apps[app])
			print(f"{apps[app]} is opening...")
		else:
			print("App not found.")

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
	elif cho in ['add_income','income','new income','add income','add-income']:
		stamp = int(input("Enter the stamp price(e.g. 100) : "))
		price = int(input("Enter the charged price : "))
		add_income(stamp,price)
	elif cho in ['today_income','today']:
		show_today_income()
	elif cho in ['show_all_income','total_income','total income']:
		show_all_income()
	elif cho in ['profit','today profit','today-profit']:
		today_profit()
	else:
		print("unknow command. type 'help' for knowing the yet available commands.")