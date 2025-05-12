#stopped at https://youtu.be/VnwDPa9biwc?si=3kark5FbxbMeVAYp&t=333 for line 27 (images)

# M08-AssnFinal -  Creating a To Do List
# author: myb
# created: 2025-05-3
# IDE: visual studio code
# program of creating a to do list
# CODING ASSISTANCE was used in this program

# Display the program's name
# Get user input of task
# Initialize variables


print("M08-AssnFinal (myb): Creating a To Do List") # Display the program's name
print("")

# CodeAssist-Internet: Lines 16-60 learned how to code to create functions for buttons from https://youtu.be/OAHLwtmdqUk?si=mAC5-rIof-w5TZ-0 

import tkinter as tk                # import tkinter
from tkinter import messagebox      # import messagebox

root = tk.Tk() # Assign the tk.TK() function to variable root to create an instance of the tkinter frame 

tasks = [] #Create an empty list

#Create functions for buttons

def update_listbox(): # Defined update_listbox() to ensure items are addded to the listbox
    clear_listbox()
    for items in tasks:
        task_list_box.insert("end", items)

def clear_listbox():  # Defined clear_listbox() to ensure the listbox is empty and to delete all of the tasks from index 0 to the end of the list
    task_list_box.delete(0, "end")

# CodeAssist-AI: Used Google Lens AI to learn how to write code using an if-else statement with a messagebox 
def add_task():
    task = task_input.get()  # Assign the task_input value to variable task and updates the listbox when a task is added.
    if task:                    # If-else statement used to determine if error messagebox will display if a task has not been inputted before clicking on add task button
        tasks.append(task)
        update_listbox()
        task_input.delete(0, "end")
    else:
        messagebox.showinfo("Error", "A task must be entered")

# CodeAssist-Internet: Used code from https://youtu.be/K7jOtVpEFLk?si=SRJEOedLd85M-_ur to delete tasks
def delete():
    task = task_list_box.get("active") # Assign the task_list_box value to variable task and to only delete tasks that have been added to the listbox
    if task in tasks:
        tasks.remove(task)
    update_listbox()

# CodeAssist-Internet: Learned how to write code using the global function from https://youtu.be/v2oLM6tDj04?si=lDMVP-h7QX0oA_M2 
# CodeAssist-AI: Used Google AI Overviews to learn how to write code using a messagebox 
def delete_all():
    confirmed = messagebox.askyesno("Confirmation", "Do you really want to delete all tasks?") # Assign the messagebox to variable confirmed to require confirmation of deleting all of task
    if confirmed:
        global tasks  
        tasks = []
        update_listbox()


# CodeAssist-Internet: Learned how to write code to exit GUI https://www.geeksforgeeks.org/how-to-close-a-tkinter-window-with-a-button/
def exit():
    confirmed = messagebox.askyesno("Warning", "Are you sure you want to exit?")  # Assign the messagebox to variable confirmed to require confirmation of exiting the GUI. If Yes is selected it will close GUI
    if confirmed:
        root.destroy()
  

# CodeAssist-Internet: Learned how to set up GUI from https://youtu.be/OAHLwtmdqUk?si=mAC5-rIof-w5TZ-0 
root.title("My To Do List") # root window title and dimension
root.geometry("350x500") # Set geometry (widthxheight) of GUI


# Label widgets: Header provides name of GUI and statements of encouragement when working on tasks

header = tk.Label(text = "Today's Tasks", pady = 5) 
header.pack()

encouragement1 = tk.Label(text = "You Got This!", pady = 20, padx = 10) # Assign the label widget to variable encouragement1 to give words of encouragement and provide text padding 
encouragement1.pack()

# CodeAssist-AI: Used Google AI Overviews to code text alignment at the bottom
encouragement2 = tk.Label(text = "All You Can Do is One Task at a Time!") # Assign the label widget to variable encouragement2 to give words of encouragement
encouragement2.pack(side = "bottom") # pack() layout manager used to place text at bottom of GUI



# CodeAssist-Internet: Learned how to code entry command and blank field from https://www.simplilearn.com/tutorials/python-tutorial/python-graphical-user-interface-gui
task_input = tk.Entry(width = 50) # Assign the entry widget to variable task_input to allow users to enter single-line text
task_input.pack()

# CodeAssist-Internet: Learned how to code blank field from https://youtu.be/OAHLwtmdqUk?si=mAC5-rIof-w5TZ-0 
blank_field = tk.Label(text = "") # Assign the label widget to variable blank_field to have white space between entry field and first button
blank_field.pack() 



# Button widgets: Creating clickable buttons for user interaction with GUI

# CodeAssist-Internet: Learned how to code buttons from https://youtu.be/OAHLwtmdqUk?si=mAC5-rIof-w5TZ-0 
btn_add_task = tk.Button(root, text = "Add Task", command = add_task)  # button handlers 
btn_add_task.pack()


btn_del = tk.Button(root, text = "Delete", command = delete)
btn_del.pack()

btn_del_all = tk.Button(root, text = "Delete All", command = delete_all)
btn_del_all.pack()

btn_exit = tk.Button(root, text = "Exit", command = exit)
btn_exit.pack()


task_list_box = tk.Listbox(root)
task_list_box.pack()


# CodeAssist-Internet: Learned how setup code for working GUI from https://youtu.be/OAHLwtmdqUk?si=mAC5-rIof-w5TZ-0 
root.mainloop()  # Executes Tkinter


