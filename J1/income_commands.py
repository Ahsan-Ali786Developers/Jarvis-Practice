import sqlite3 as sq
from datetime import datetime as dt

c = sq.connect("Jarvis.db")
cr = c.cursor()
cr.execute("""Create table if not exists income(Id Integer primary key autoincrement,date Text not null,time text not null, charged_price Integer,govt_fee int, other_charges int, profit int)""")
c.commit()

def add_new_income():
	try:
		stamp = int(input("Enter the Stamp price : "))
		price = int(input("Enter the charged price : "))
		
		govt_fee = int(stamp)+15
		profit=int(price) - govt_fee - 40
		now = dt.now()
		cr.execute("Insert into income (date, charged_price, govt_fee, other_charges, profit, time) values (?, ?, ?, 40, ?, ?) ",(now.strftime("%Y-%m-%d"), price,govt_fee, profit, now.strftime("%I-%M-%S %p")))
		c.commit()
	except ValueError:
		print("Please enter valid number")

def show_today():
	now = dt.now()
	data = cr.execute("Select * from income where date=?",(str(now.strftime("%Y-%m-%d")),))
	for row in data:
		print(row)

def show_all():
	data = cr.execute("Select * from income")
	for row  in data:
		print(row)
def show_profit():
	now = dt.now()
	data = cr.execute("Select * from income where date = ?",(str(now.strftime("%Y-%m-%d")),))
	total_charged = 0
	total_cost = 0
	total_profit = 0
	total_deducted = 0
	for row in data:
		total_charged+=row[3]
		total_deducted+=row[4]
		total_cost+=(row[4]+row[5])
		total_profit+=row[6]
	print(f'''Total cost : {total_cost}\nTotal Charged : {total_charged}\nTotal Deducted : {total_deducted}\nTotal Profit : {total_profit}''')

def add_gui_income(stamp,price):
	try:
		govt_fee = int(stamp)+15
		profit=int(price) - govt_fee - 40
		now = dt.now()
		cr.execute("Insert into income (date, charged_price, govt_fee, other_charges, profit, time) values (?, ?, ?, 40, ?, ?) ",(now.strftime("%Y-%m-%d"), price,govt_fee, profit, now.strftime("%I-%M-%S %p")))
		c.commit()
	except ValueError:
		print("Please enter valid number")

def gui_profit():
	now = dt.now()
	data = cr.execute("Select * from income where date = ?",(str(now.strftime("%Y-%m-%d")),))
	total_charged = 0
	total_cost = 0
	total_profit = 0
	total_deducted = 0
	for row in data:
		total_charged+=row[3]
		total_deducted+=row[4]
		total_cost+=(row[4]+row[5])
		total_profit+=row[6]
	return f'''Total cost : {total_cost}\nTotal Charged : {total_charged}\nTotal Deducted : {total_deducted}\nTotal Profit : {total_profit}'''
