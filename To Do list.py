from tkinter import *
from tkinter.ttk import*
from tkinter import messagebox
import pickle


window=Tk()
window.geometry("600x500")
window.resizable(False,False)
window.title("TO DO LIST")
style=Style()

def addtask():
    get_task=task_entry.get()
    if get_task!="":
        tasks_list.insert(END,get_task)
        task_entry.delete(0,END)
    else:
        messagebox.showerror("error!","enter a task")    


def delete_task():
    try:
         task_index=tasks_list.curselection()[0]
         tasks_list.delete(task_index)
    except:
        messagebox.showerror("warning","select a task")

def load_task():
    try:
        taskloaded=pickle.load(open("task.data",'rb'))
        tasks_list.delete(0,END)
        for task in taskloaded:
               tasks_list.insert(END,task)
    except:
        messagebox.showerror("warning","cannot find data")

def save_task():
    tasks=tasks_list.get(0,tasks_list.size())
    pickle.dump(tasks,open("task.data",'wb'))
    
style.configure("Header.TFrame",background="light blue")
header_frame=Frame(window, style='Header.TFrame')
header_frame.pack(fill=X)

style.configure("Header.TLabel",background="light blue" ,font=('cursive',30),color="white")
header=Label(header_frame,text="TO DO LIST" ,style='Header.TLabel')
header.pack()

task_frame=Frame(window)
task_frame.pack()

tasks_list=Listbox(task_frame, height=15, width=80)
tasks_list.pack(side=LEFT)

scrollbar = Scrollbar(task_frame)
scrollbar.pack(side=RIGHT ,fill=Y)

tasks_list.config (yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_list.yview)


task_entry=Entry(window, width=80)
task_entry.pack()

add_task_button=Button(window,text="ADD TASK",width=80, command=addtask)
add_task_button.pack()

delete_task_button=Button(window,text="Delete Task", width=80, command=delete_task)
delete_task_button.pack()

load_task_button=Button(window,text="Load Task",width=80,command=load_task)
load_task_button.pack()

save_task_button=Button(window,text="Save Task",width=80,command=save_task)
save_task_button.pack()


window.mainloop()