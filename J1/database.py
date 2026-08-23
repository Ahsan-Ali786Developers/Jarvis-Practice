import sqlite3 as sq

c = sq.connect("Jarvis.db")
cr = c.cursor()
cr.execute(""" Create Table if not exists tasks(id Integer primary key autoincrement, task Text not null, status text not null default 'pending')""")#not know to setting value by default
cr.execute("""Create table if not exists notes(id integer primary key autoincrement, content text)""")
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
def delete_task(task_id):
	cr.execute("Delete from tasks where id = ?",(task_id,))
	c.commit()
def add_notes(text):
	cr.execute('insert into notes (content) values (?)',(text,))
	c.commit()
def show_notes():
	text = cr.execute("Select * from notes")
	tex = text.fetchall()
	for te in tex:
		print(te[0],te[1])