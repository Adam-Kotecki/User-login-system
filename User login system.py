import requests
import json
import tkinter as tk
from tkinter import ttk
from tkinter import Entry
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import datetime

root = tk.Tk()

root.geometry('500x400')
root.resizable(False, False)
root.title('User login system')

sign_in_btn = tk.Button(root, text="Sign in", command=lambda: login_page())
sign_in_btn.place(x=160, y=50)

create_account_btn = tk.Button(root, text="Create account", command=lambda: register_page())
create_account_btn.place(x=160, y=100)

def register_page():
    # button.place_forget()
    
    for widgets in root.winfo_children():
        widgets.destroy()
    
    sign_in_btn = tk.Button(root, text="Sign in", command=lambda: login_page())
    sign_in_btn.place(x=160, y=330)
    
    label0 = tk.Label(text="", fg = "red")
    label0.place(x=160 , y=30)
    
    label1 = tk.Label(text="Username:")
    label1.place(x=210 , y=80)
    username = tk.StringVar()
    textbox1 = tk.Entry(root, width = 30, textvariable = username)
    textbox1.place(x=160, y=100)
    
    label2 = tk.Label(text="Password:")
    label2.place(x=210 , y=130)
    password =  tk.StringVar()
    textbox2 = tk.Entry(root, width = 30, textvariable = password)
    textbox2.place(x=160, y=150)
    
    label3 = tk.Label(text="Repeat password:")
    label3.place(x=210 , y=180)
    password_again =  tk.StringVar()
    textbox3 = tk.Entry(root, width = 30, textvariable = password_again)
    textbox3.place(x=160, y=200)
    
    label4 = tk.Label(text="Email:")
    label4.place(x=210 , y=230)
    email =  tk.StringVar()
    textbox4 = tk.Entry(root, width = 30, textvariable = email)
    textbox4.place(x=160, y=250)
    
    def send_data():
        if username.get() == "":
            label0["text"] = "Please type username"
        elif (len(username.get()) < 5) or username.get()[0] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            label0["text"] = "Username should consists of at least 5 characters\n and should not starts with digit"
        elif password.get() == "":
            label0["text"] = "Please provide password"
        elif (len(password.get()) < 8) or (not any(letter in "!@#$%^&*()-+?_=,<>/" for letter in password.get())):
            label0["text"] = "Password should be at least 8 characters long and should consists of special character"
        elif password_again.get() == "":
            label0["text"] = "Please repeat password"
        elif password_again.get() != password.get():
            label0["text"] = "Repeated password does not match password"
        elif email.get() == "":
            label0["text"] = "Please type email"
            
    register_btn = tk.Button(root, text="Register", command=lambda: send_data())
    register_btn.place(x=160, y=290)
    
def login_page():
    
    for widgets in root.winfo_children():
      widgets.destroy()
    
    label1 = tk.Label(text="Username:")
    label1.place(x=210 , y=80)
    username = tk.StringVar()
    textbox1 = tk.Entry(root, width = 30, textvariable = username)
    textbox1.place(x=160, y=100)
    
    label2 = tk.Label(text="Password:")
    label2.place(x=210 , y=130)
    password =  tk.StringVar()
    textbox2 = tk.Entry(root, width = 30, textvariable = password)
    textbox2.place(x=160, y=150)
    
    def compare_data():
        pass
    
    login_btn = tk.Button(root, text="Log in", command=lambda: compare_data())
    login_btn.place(x=160, y=180)
    
    create_account_btn = tk.Button(root, text="Create account", command=lambda: register_page())
    create_account_btn.place(x=160, y=210)

root.mainloop()
