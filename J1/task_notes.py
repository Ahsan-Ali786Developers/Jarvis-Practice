from database import (
complete_task, show_task, delete_task, add_task, show_notes, add_notes)

def add_new_task():
	task = input("Enter your task : ").strip()

	if task:
		add_task(task)
	else:
		print("Task cannot be empty.")

def show_all_tasks():
	show_task()

def complete_existing_task():
	try:
		task_id  = int(input("Enter ID of task: "))
		complete_task(task_id)
	except ValueError:
		print("Please enter a valid task ID.")
def delete_existing_task():
	try:
		task_id = int(input("Enter ID of task : "))
		delete_task(task_id)
	except ValueError:
		print("Please enter a valid task ID.")
def remember_notes():
	text = input("Enter your note : ").strip()
	if text:
		add_notes(text)
	else:
		print("Note cannot be empty.")
def show_all_notes():
	show_notes()
def addtaskgui(text):
	add_task(text)
def completetaskgui(taskid):
	complete_task(taskid)
def deletetaskgui(taskid):
	delete_task(taskid)
def addnotegui(text):
	add_notes(text)
