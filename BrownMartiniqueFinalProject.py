#stopped at https://youtu.be/VnwDPa9biwc?si=_iAyNUEWgGTqYGKg&t=181 for line 20 (images)

# M08-AssnFinal -  Creating a To Do List
# author: myb
# created: 2025-05-3
# IDE: visual studio code
# program of creating a to do list
# CODING ASSISTANCE was used in this program


# Display the program's name
print("M08-AssnFinal (myb): Creating a To Do List")
print("")


# import tkinter

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTK

root = tk.Tk()

#Create an empty list
tasks = []

#Create functions for buttons

def update_listbox():
    clear_listbox()
    for items in tasks:
        task_list_box.insert("end", items)

def clear_listbox():
    task_list_box.delete(0, "end")

def add_task():
    task = task_input.get()
    tasks.append(task)
    update_listbox()
    #Deletes task after text has been inputted 
    task_input.delete(0, "end")

  
def delete():
    # learn this from this https://youtu.be/K7jOtVpEFLk?si=SRJEOedLd85M-_ur 
    #whatever the user clicks on is cosidered "active"
    task = task_list_box.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

# learned more about global function https://youtu.be/v2oLM6tDj04?si=lDMVP-h7QX0oA_M2 
# used AI to learn how to write code for messagebox
def delete_all():
    confirmed = messagebox.askyesno("Confirmation", "Do you really want to delete all tasks?")
    if confirmed:
        global tasks
        tasks = []
        update_listbox()

def save():
    pass

def exit():
    pass

# root window title and dimension
root.title("My To Do List")
# Set geometry (widthxheight)
root.geometry("350x500")

todays_date = input("What is today's date?")
cmd = tk.Label(text = f"{todays_date} Tasks")
cmd.pack()



# Learned how to code entry command https://www.simplilearn.com/tutorials/python-tutorial/python-graphical-user-interface-gui
task_input = tk.Entry(width = 350)
task_input.pack()

blank_field = tk.Label(text = "")
blank_field.pack()






# Learned how to code buttons https://youtu.be/OAHLwtmdqUk?si=mAC5-rIof-w5TZ-0 
btn_add_task = tk.Button(root, text = "Add Task", command = add_task)
btn_add_task.pack()


btn_del = tk.Button(root, text = "Delete", command = delete)
btn_del.pack()

btn_del_all = tk.Button(root, text = "Delete All", command = delete_all)
btn_del_all.pack()

btn_save = tk.Button(root, text = "Save", command = save)
btn_save.pack()


btn_exit = tk.Button(root, text = "Exit", command = exit)
btn_exit.pack()

task_list_box = tk.Listbox(root)
task_list_box.pack()



# all widgets will be here
# Execute Tkinter
root.mainloop()
