"""
	tbl_user
	id     username    password
	1       admin       user
	2       sample      hello
	3       foxtrot     golf
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

database = mysql.connect(
		host="127.0.0.1",
		user="root",
		password="",
		database="pythontth"
	)

def login_sql(user:str,password:str)->None:
	sql = f"SELECT * FROM `tbl_student` WHERE username='{user}'"
	cursor = database.cursor()
	cursor.execute(sql)
	data:list = cursor.fetchall()

	if len(data)>0:
		d:tuple = data[0]
		if password == d[2]:
			messagebox.showinfo(title="LOGIN",message=f"Hello {user}")
		else:
			messagebox.showinfo(title="LOGIN",message=f"Wrong password {user}!")

	else:
		messagebox.showinfo(title="LOGIN",message="Account not found")

def login()->None:
	username:str = text_user.get()
	password:str = text_password.get()
	
	login_sql(username,password)

root = tk.Tk()
root.title("USER LOGIN")
root.geometry("400x200")
root.eval("tk::PlaceWindow  .  center")
root.resizable(False,False)


frame =tk.Frame(root)
frame.pack(padx=10,pady=10)


label_user=ttk.Label(frame,text="USERNAME")
label_user.pack(fill="x",padx=3,pady=3)

text_user=ttk.Entry(frame,width=50)
text_user.pack(fill="x",padx=3,pady=3)

label_password=ttk.Label(frame,text="PASSWORD")
label_password.pack(fill="x",padx=3,pady=3)

text_password=ttk.Entry(frame,width=50,show="*")
text_password.pack(fill="x",padx=3,pady=3)

btn_save =tk.Button(frame,text="LOGIN",width=20,command=login)
btn_save.pack(fill="x",padx=3,pady=3)

root.mainloop()
