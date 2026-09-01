from datetime import datetime as dt

def show_date():
	now = dt.now()
	current_date = now.strftime("%Y-%m-%d")
	print(current_date)
def show_time():
	now = dt.now()
	current_time = now.strftime("%I:%M:%S %p")
	print(current_time)