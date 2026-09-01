import psutil

def system_status():
	disk = psutil.disk_usage('/')

	print(f"\nDisk usage: {disk.percent}%\nTotal : {disk.total}\nFree: {disk.free}\n")

	memory  = psutil.virtual_memory()

	print(f"RAM usage : {memory.percent}%\nTotal : {memory.total}\nFree : {memory.free}")

def gui_system_status():	
	disk = psutil.disk_usage('/')
	memory = psutil.virtual_memory()

	return  f"\nDisk usage: {disk.percent}%\nTotal : {disk.total}\nFree: {disk.free}\n RAM usage : {memory.percent}%\nTotal : {memory.total}\nFree : {memory.free}" 