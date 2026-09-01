from task_notes import (
complete_existing_task,
add_new_task, 
show_all_tasks,
delete_existing_task,
remember_notes,
show_all_notes
)
from datetime_tool import show_time, show_date
from system import system_status
from help import show_help
from files import organize_user_folder,create_new_folder	
from greeting import greeting
import os
from apps import open_app
from power import lock_system, restart_system, shutdown_system
from logger import log_command as log
from search import search_google
from income_commands import (
add_new_income, 
show_today, 
show_all,
show_profit
)

print("JARVIS ready. Type 'help' for commands.")

while True:
	command = input("\nYou: ").strip().lower()
	log(command)
	
	#HELP
	if command=="help":
		show_help()
	# system
	elif command in ['system','status']:
		system_status()

	# search
	elif command in ['search']:	
		search_google()
	# greeting
	elif command in ['hay','hey','greet','hello','hy']:
		greeting()
		
	#Exit
	elif command=="exit":
		print("Your are exitting from the jarvis.\nTake care of your self.")
		break
	elif command in ['date']:
		show_date()
	elif command in ['time']:
		show_time()
	elif command in ['create_folder','create-folder','make-folder','make_folder','make','create']:
		create_new_folder()
		
	elif command in ['organize-downloads','organize_downloads','organize']:
		organize_user_folder()

	elif command in ['lock']:
		lock_system()
	elif command in ['restart', 'refresh','re']:
		restart_system()
	elif command in ["shutdown", 'shut down']:
		shutdown_system()
					
	elif command in ['open']:
		open_app()

	elif command in ['add', 'add_task']:
		add_new_task()
	elif command in ['show', 'show_task']:
		show_all_tasks()
	elif command in ["complete_task", "task", 'complete']:
		complete_existing_task()
	elif command in ['delete', 'delete_task']:
		delete_existing_task()
	elif command in ['remember','add notes']:
		remember_notes()
	elif command in ['notes']:
		show_all_notes()
	elif command in ['add_income','income','new income','add income','add-income']:
		add_new_income()
	elif command in ['today_income','today']:
		show_today()
	elif command in ['show_all_income','total_income','total income']:
		show_all()
	elif command in ['profit','today profit','today-profit']:
		show_profit()
	else:
		print("unknow command. type 'help' for knowing the yet available commands.")

def handle_system_command(command):
	pass
def handle_search_command(command):
	pass
def handle_task_command(command):
	pass
def handle_income_command(command):
	pass
def handle_file_command(command):
	pass
'''
def greeting():
def system_status():
def search_google():
def open_app():
def show_date():
def show_time():
def restart_pc():
def shutdown_pc():
def lock_pc():
def main_loop():
'''