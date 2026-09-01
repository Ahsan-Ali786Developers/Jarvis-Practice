import os

APPS = {
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
def open_app():
	app = input("Which app do you want to open? ").strip().lower()
	if app in APPS:
		os.system(APPS[app])
		print(f"Opening {app}...")
	else:
		print("App not found.")
