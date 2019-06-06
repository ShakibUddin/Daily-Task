from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import os
import os.path

button_height=1
button_width=10
bg_color="lawn green"
active_bg="grey"

def add_task_input():
	tasks=task_entry.get()+"\n"
	f=open("task_file.txt","a")
	f.write(tasks)
	f.close()
	task_entry.delete('0', END)

def delete_task():
	with open("task_file.txt","r+") as f:
		file_lines= f.readlines()
	f.close()	
	with open("task_file.txt","w") as f:
	    for line in file_lines:
	        if (line.strip("\n") != delete_task_entry.get()):
	           f.write(line)
	f.close() 
	delete_task_entry.delete('0', END)          	

def my_task_display():
		if os.path.isfile("task_file.txt"):
			with open("task_file.txt") as f:
				lines=f.read().splitlines()
			f.close()	
			output.delete(0.0,END)
			for line in lines:
			    output.insert(END,line+"\n")	

		else:
		    messagebox.showinfo("Error","There is no task yet !!!")

def refresh_task():
        os.remove("task_file.txt")
        output.delete(0.0,END)  
def exit_gui():
    window.destroy()
    exit()        

window=Tk()

window.geometry("500x800")
window.resizable(0,0)
window.title("Task Manager")
window.configure(background=bg_color)

myfont=Font(family="Helvetica",size=12)
labelfont=Font(family="Helvetica",size=18)

headerphoto=Label(window,text="Daily Task",width=100,height=5,font=labelfont,bg=bg_color,borderwidth=2,relief="flat")
headerphoto.config(anchor=CENTER)
headerphoto.pack()

task_entry=Entry(window,width=50,bd=5,relief="sunken")
task_entry.pack()

button1=Button(window,text="Add Task",font=myfont,width=button_width,height=button_height,relief="raised",background="lime green",activebackground=active_bg,command=add_task_input)
button1.config(anchor=CENTER)
button1.pack()

delete_task_entry=Entry(window,width=50,bd=5,relief="sunken")
delete_task_entry.pack()

button2=Button(window,text="Delete Task",font=myfont,width=button_width,height=button_height,relief="raised",background="green2",activebackground=active_bg,command=delete_task)
button2.config(anchor=CENTER)
button2.pack()

button3=Button(window,text="My Tasks",font=myfont,width=button_width,height=button_height,relief="raised",background="green3",activebackground=active_bg,command=my_task_display)
button3.config(anchor=CENTER)
button3.pack()

output=Text(window,wrap=WORD,width=40,height=20,background="white",bd=5,relief="sunken")
output.pack()

button4=Button(window,text="Refresh",font=myfont,width=button_width,height=button_height,relief="raised",background="green4",activebackground=active_bg,command=refresh_task)
button4.config(anchor=CENTER)
button4.pack()

button5=Button(window,text="Exit",font=myfont,width=button_width,height=button_height,relief="raised",background="dark green",activebackground=active_bg,command=exit_gui)
button5.config(anchor=CENTER)
button5.pack()

window.mainloop()