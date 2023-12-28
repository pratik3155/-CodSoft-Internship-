'''
Task 1
A To-Do List application is a useful project that helps users manage and organize their tasks efficiently.
This project aims to create a command-line or GUI-based application using Python, allowing users to create,
update, and track their to-do lists
'''

import tkinter
import tkinter.messagebox
import pickle

class ToDoListApp:
    def __init__(self, window):
        self.window = window
        self.window.title("TO DO LIST")

        self.list_frame = tkinter.Frame(window)
        self.list_frame.pack()

        self.todo_box = tkinter.Listbox(self.list_frame, height=20, width=50)
        self.todo_box.pack(side=tkinter.LEFT)

        self.scroller = tkinter.Scrollbar(self.list_frame)
        self.scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.todo_box.config(yscrollcommand=self.scroller.set)
        self.scroller.config(command=self.todo_box.yview)

        self.task_add = tkinter.Entry(window, width=70)
        self.task_add.pack()

        self.add_task_button = tkinter.Button(window, text="Click to Add Task", font=("arial", 20, "bold"),
                                              background="red", width=20, command=self.task_adding)
        self.add_task_button.pack()

        self.remove_task_button = tkinter.Button(window, text="Click to Delete Task", font=("arial", 20, "bold"),
                                                 background="yellow", width=20, command=self.task_removing)
        self.remove_task_button.pack(side=tkinter.LEFT)

        self.load_task_button = tkinter.Button(window, text="Click to Load Task", font=("arial", 20, "bold"),
                                               background="blue", width=20, command=self.task_load)
        self.load_task_button.pack(side=tkinter.LEFT)

        self.update_task_button = tkinter.Button(window, text="Click to Update Task", font=("arial", 20, "bold"),
                                                 background="green", width=20, command=self.task_update)
        self.update_task_button.pack(side=tkinter.LEFT)

        self.save_task_button = tkinter.Button(window, text="Click to Save Task", font=("arial", 20, "bold"),
                                               background="brown", width=20, command=self.task_save)
        self.save_task_button.pack(side=tkinter.LEFT)

    def task_adding(self):
        todo = self.task_add.get()
        if todo != "":
            self.todo_box.insert(tkinter.END, todo)
            self.task_add.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="Attention !!", message="To add a task, please enter the task")

    def task_removing(self):
        try:
            index_todo = self.todo_box.curselection()[0]
            self.todo_box.delete(index_todo)
        except IndexError:
            tkinter.messagebox.showwarning(title="Attention !!", message="To delete a task, you must select a task !!")

    def task_load(self):
        try:
            tasks = pickle.load(open("tasks.dat", "rb"))
            self.todo_box.delete(0, tkinter.END)
            for todo in tasks:
                self.todo_box.insert(tkinter.END, todo)
        except FileNotFoundError:
            tkinter.messagebox.showwarning(title="Attention !!", message="Cannot find tasks.dat")

    def task_update(self):
        try:
            index_todo = self.todo_box.curselection()[0]
            updated_task = self.task_add.get()
            if updated_task != "":
                self.todo_box.delete(index_todo)
                self.todo_box.insert(index_todo, updated_task)
                self.task_add.delete(0, tkinter.END)
            else:
                tkinter.messagebox.showwarning(title="Attention !!", message="To update a task, please enter the task")
        except IndexError:
            tkinter.messagebox.showwarning(title="Attention !!", message="To update a task, you must select a task !!")

    def task_save(self):
        todo_list = self.todo_box.get(0, self.todo_box.size())
        pickle.dump(todo_list, open("tasks.dat", "wb"))

if __name__ == "__main__":
    window = tkinter.Tk()
    todo_app = ToDoListApp(window)
    window.mainloop()
