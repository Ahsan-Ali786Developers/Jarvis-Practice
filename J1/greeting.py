from datetime import datetime as dt

def greeting():
	now = dt.now()
	hour = now.hour
	if hour < 12:
		print("Good morning, Ahsan")
	elif hour >= 12 and hour < 17:
		print("Good afternoon, Ahsan")
	else:
		print("Good evening,Ahsan")