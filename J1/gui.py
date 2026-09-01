import customtkinter as ctk
from system import gui_system_status
from task_notes import complete_existing_task,delete_existing_task,add_new_task, show_task,remember_notes, show_all_notes,show_all_tasks,addtaskgui, completetaskgui, deletetaskgui, addnotegui
from database import get_all_tasks,get_all_notes
from power import lock_system, do_restart, do_shutdown,cancel_power_action
from tkinter import messagebox as msg
from income_commands import add_gui_income,gui_profit

class JarvisApp(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.title("JARVIS")
		self.geometry("600x700")
		label = ctk.CTkLabel(self, text="Welcome to JARVIS") 
		label.pack(pady=(0,10))

	     # tabview
		self.tabview = ctk.CTkTabview(self, width=500, height=600)
		self.tabview.pack(pady=10)
		self.tabview.add("Tasks")
		self.tabview.add("Notes")
		self.tabview.add("System")
		self.tabview.add("Income")


		self.build_tasks_tab()
		self.build_notes_tab()
		self.build_system_tab()
		self.build_income_tab()
	def build_tasks_tab(self):
		tab = self.tabview.tab("Tasks")

	       # add task entry + button
		self.task_entry = ctk.CTkEntry(tab, placeholder_text="Enter task")
		self.task_entry.pack(pady=5)
		ctk.CTkButton(tab, text="Add Task", command=self.handle_add).pack(pady=5)

	       # complete task entry + button
		self.complete_entry = ctk.CTkEntry(tab, placeholder_text="Task ID to complete")
		self.complete_entry.pack(pady=5)
		ctk.CTkButton(tab, text="Complete Task",command=self.handle_complete).pack(pady=5)

	     # delete task entry + button
		self.delete_entry = ctk.CTkEntry(tab, 	placeholder_text="Task ID to delete")
		self.delete_entry.pack(pady=5)
		ctk.CTkButton(tab, text='Delete Task',command=self.handle_delete).pack(pady=5)
		
	     # task list frame
		self.task_list_frame = ctk.CTkScrollableFrame(tab, width=350, height=200)
		self.task_list_frame.pack(pady=10)
		self.refresh_tasks()

	def handle_add(self):
		addtaskgui(self.task_entry.get())
		self.task_entry.delete(0,'end')
		self.refresh_tasks()
	
	def handle_complete(self):
		completetaskgui(int(self.complete_entry.get()))
		self.complete_entry.delete(0,'end')
		self.refresh_tasks()
	def refresh_tasks(self):
		for widget in self.task_list_frame.winfo_children():
			widget.destroy()
		for task in get_all_tasks():
			text = f"{task[0]}. {task[1]} [{task[2]}]"
			ctk.CTkLabel(self.task_list_frame, text=text).pack(anchor='w')

	def handle_delete(self):
		deletetaskgui(int(self.delete_entry.get()))
		self.delete_entry.delete(0,'end')
		self.refresh_tasks()
	def build_notes_tab(self):
		tab = self.tabview.tab("Notes")
		
	    # note entry+button
		self.note_entry = ctk.CTkEntry(tab, placeholder_text="Enter note")
		self.note_entry.pack(pady=10)
		ctk.CTkButton(tab, text="Add Note", command=self.handle_note).pack(pady=5)

		self.notes_frame = ctk.CTkScrollableFrame(tab, width=350, height=150)
		self.notes_frame.pack(pady=10)
		self.refresh_notes()

	def handle_note(self):
		addnotegui(self.note_entry.get())
		self.note_entry.delete(0,'end')
		self.refresh_notes()

	def refresh_notes(self):
		for widget in self.notes_frame.winfo_children():
			widget.destroy()
		for note in get_all_notes():
			ctk.CTkLabel(self.notes_frame, text=f"{note[0]}. {note[1]}").pack(anchor='w')

	def build_system_tab(self):
		tab = self.tabview.tab("System")

		ctk.CTkButton(tab,text="Lock",command=lock_system).pack(pady=5)
		ctk.CTkButton(tab, text="Restart",command=self.handle_restart).pack(pady=5)
		ctk.CTkButton(tab,text="Shutdown", command=self.handle_shutdown).pack(pady=5)
		ctk.CTkButton(tab,text="Cancel Pending task",command=cancel_power_action).pack(pady=5)
		ctk.CTkButton(tab, text="Check Status",command=self.handle_status).pack(pady=5)
		
		self.status_label = ctk.CTkLabel(tab, text="")
		self.status_label.pack(pady=10)
	
	def handle_shutdown(self):
		answer = msg.askyesno("Confirm Shutdown", "Are you sure you want to shutdown?")
		if answer:
			do_shutdown()
			msg.showinfo("Shutdowning","System will shutdown in 240 seconds. YOu can cancelled shutdown from the system tab.")
		else:
			msg.showinfo("Cancelled", "Shutdown cancelled.")

	def handle_restart(self):
		answer = msg.askyesno("Confirm Restart", "Are you sure you want to restart?")
		if answer:
			do_restart()
			msg.showinfo("Restarting", "System will restart in 240 seconds. You can cancel from the System tab.")
		else:
			msg.showinfo("Cancelled", "restart cancelled.")
	def handle_status(self):
		self.status_label.configure(text=gui_system_status())

	def build_income_tab(self):
		tab = self.tabview.tab("Income")

		self.stamp_entry = ctk.CTkEntry(tab, placeholder_text="Stamp value (e.g. 100) ")
		self.stamp_entry.pack(pady=5)

		self.charged_entry = ctk.CTkEntry(tab, placeholder_text="Amount charged")
		self.charged_entry.pack(pady=5)

		ctk.CTkButton(tab, text="Add Income", command=self.handle_add_income).pack(pady=5)
		ctk.CTkButton(tab, text="Show Today's Profit", command=self.handle_show_profit).pack(pady=5)
		self.profit = ctk.CTkLabel(tab,text="")
		self.profit.pack(pady=4)
	

	def handle_add_income(self):
		stamp= self.stamp_entry.get().strip()
		charged = self.charged_entry.get().strip()
		try:	
			if stamp in ['',"",0] or charged in ["",'',0]:
				msg.showerror("Empty", "The value must be entered")
				return
			else:
				stampp = int(stamp)
				price = int(charged)
				add_gui_income(stampp,price)
				self.stamp_entry.delete(0, 'end')
				self.charged_entry.delete(0,'end')
				msg.showinfo("Success","Income added.")
		except ValueError:
			msg.showerror("Value error", "should be add some number")	
	def handle_show_profit(self):
		text = gui_profit()
		self.profit.configure(text=text)
if __name__=="__main__":
	app = JarvisApp()
	app.mainloop()