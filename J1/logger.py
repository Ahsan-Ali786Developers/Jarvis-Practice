import csv
from datetime import datetime as dt

def log_command(cho):
	now = dt.now().strftime("%I-%M-%S %p  %y-%m-%d")
	with open("logs.csv","a",newline="") as f:
		writer = csv.writer(f)
		writer.writerow([now, cho])