import sqlite3 as sq

c = sq.connect("Jarvis.db")
cr = c.cursor()
cr.execute(""" Create Table if not exists tasks(id Integer primary key autoincrement, task Text not null, status text not null default 'pending')""")#not know to setting value by default
c.commit()
def add_task(task):
	cr.execute("Insert into tasks (task) VAlues (?)",(task,))
	c.commit()
def show_task():
	cr.execute("Select * from tasks")
	R = cr.fetchall()
	for row in R:
		print(f"{row[0]}. {row[1]} [{row[2]}]\n")
def complete_task(task_id):
	cr.execute("Update tasks set status =? where id=?",("done",task_id))# did not know
	c.commit()