import os

def lock_system():
	print("Your system is locking...")
	os.system("rundll32.exe user32.dll,LockWorkStation")

def restart_system():
	confirm = input("Are you sure to restart? (yes/no) : ").strip().lower()
	if confirm == 'yes':
		print("Your system is restarting...")
		os.system("shutdown /r /t 240")
		
		cancel = input("Do you want to cancel? (yes/no) : ").strip().lower()
		if cancel =='yes':
			os.system("shutdown /a")
			print("Restart cancelled.")
		elif cancel == 'no':
			print("Restart will  continue.")
	elif confirm == 'no':
		print("You cancelled the restart.")
def shutdown_system():
	confirm = input("Are you sure you want to shut down? (yes/no) : ").strip().lower()
	if confirm == 'yes':
		print("Shutting down. Goodbye, Ahsan.")
		os.system("shutdown /s /t 240")
		
		cancel = input("Do you want to cancel? (yes/no) : ").strip().lower()
		if cancel == 'yes':
			os.system("shutdown /a")
			print("Shutdown cancelled.")
		if cancel == 'no':
			print("Shutdown will continue.")
	elif confirm == 'no':
		print('You canelled the shutdown.')
def do_restart():
	os.system("shutdown /r /t 240")
def do_shutdown():
	os.system("shutdown /s /t 240")
def cancel_power_action():
	os.system("shutdown /a")