'''
	Python GUI

	___________________________
	|STUDENT INFORMATION       |
	---------------------------|
	|[    ENTRY     ]  [SEARCH]|
	|IDNO                      |
	|[              ]          |
	|LASTNAME                  |
	|[              ]          |
	|FIRSTNAME                 |
	|[              ]          |
	|COURSE                    |
	|[  COMBO BOX   ]       [V]|
	|LEVEL                     |
	|[  COMBO BOX   ][V] [SAVE]|
	|                  [CANCEL]|
	----------------------------

'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from os import system
import student_database as db

system("cls")

#Main container setup
root = tk.Tk()
root.title("Student Information")
root.geometry("400x350")
root.eval("tk::PlaceWindow  .  center")
root.resizable(False,False)



#
frame =tk.Frame(root)
frame.pack(padx=10,pady=10)

def save_data()->None:
	idno:str = txt_idno.get()
	lastname:str = txt_lastname.get()
	firstname:str = txt_firstname.get()
	course:str = cbo_course.get()
	level:str = cbo_level.get()

	if db.verification(idno,lastname,firstname,course,level):
		out:list=db.sql_query("insert",[idno,lastname,firstname,course,level])
		messagebox.showinfo(title="Message",message=str(out))
	else:
		messagebox.showinfo(title="Message",message="Fill all fields")









# the widget
#txt_search = tk.Entry(frame,text = "Search...",width=50)
#txt_search.pack(side="left")
#btn_search = tk.Button(frame,text="Search")
#btn_search.pack(side="right")

label_idno = ttk.Label(frame,text="IDNO")
label_idno.pack(fill="x",padx=3,pady=3)
txt_idno = ttk.Entry(frame,width=50,show="*")
txt_idno.pack(fill="x",padx=3,pady=3)

label_lastname = ttk.Label(frame,text="LASTNAME")
label_lastname.pack(fill="x",padx=3,pady=3)
txt_lastname = ttk.Entry(frame,width=50)
txt_lastname.pack(fill="x",padx=3,pady=3)

label_firstname = ttk.Label(frame,text="FIRSTNAME")
label_firstname.pack(fill="x",padx=3,pady=3)
txt_firstname = ttk.Entry(frame,width=50)
txt_firstname.pack(fill="x",padx=3,pady=3)

label_course = ttk.Label(frame,text="COURSE")
label_course.pack(fill="x",padx=3,pady=3)

selected_course=tk.StringVar()
cbo_course = ttk.Combobox(frame,width=50,textvariable=selected_course)
cbo_course['values']=['BSCPE','BSCS','BSIT','BSIS','ACT']
cbo_course.pack(fill="x",padx=3,pady=3)


label_level = ttk.Label(frame,text="LEVEL")
label_level.pack(fill="x",padx=3,pady=3)

selected_level=tk.StringVar()
cbo_level = ttk.Combobox(frame,width=50,textvariable=selected_level)
cbo_level['values']=['1','2','3','4']
cbo_level.pack(fill="x",padx=3,pady=3)

btn_save =tk.Button(frame,text="SAVE",width=20,command=save_data)
btn_save.pack(side="left")
btn_cancel = tk.Button(frame,text="CANCEL",width=20)
btn_cancel.pack(side="right")

root.mainloop()