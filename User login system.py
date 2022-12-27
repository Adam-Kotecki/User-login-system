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

root.geometry('400x400')
root.resizable(False, False)
root.title('User login system')


def register_page():
    
    for widgets in root.winfo_children():
        widgets.destroy()
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=3)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=2)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=2)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=2)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=2)
    root.rowconfigure(9, weight=3)
    root.rowconfigure(10, weight=3)
    
    label1 = tk.Label(root, text="", fg = "red")
    label1.grid(column=0, row = 0)
    
    label2 = ttk.Label(root, text="Username:")
    label2.grid(column=0, row = 1)
    
    username = ttk.Entry(root)
    username.grid(column=0, row = 2,sticky = "N")
    
    label3 = ttk.Label(root, text="Password:")
    label3.grid(column=0, row =  3)
    
    password = ttk.Entry(root)
    password.grid(column=0, row = 4,sticky = "N")
    
    label4 = ttk.Label(root, text="Confirm password:")
    label4.grid(column=0, row =  5)
    
    confirm_password = ttk.Entry(root)
    confirm_password.grid(column=0, row = 6,sticky = "N")
    
    label5 = ttk.Label(root, text="Email:")
    label5.grid(column=0, row = 7)
    
    email = ttk.Entry(root)
    email.grid(column=0, row = 8,sticky = "N")
    
    login_button = ttk.Button(root, text="Sign in", command=lambda: login_page())
    login_button.grid(column=0, row =  10, sticky = "N")
    
    register_button = ttk.Button(root, text="Register", command=lambda: send_data())
    register_button.grid(column=0, row = 9)
    
    def send_data():
        if username.get() == "":
            label1["text"] = "Please type username"
        elif (len(username.get()) < 5) or username.get()[0] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            label1["text"] = "Username should consists of at least 5 characters\n and should not starts with digit"
        elif password.get() == "":
            label1["text"] = "Please provide password"
        elif (len(password.get()) < 8) or (not any(letter in "!@#$%^&*()-+?_=,<>/" for letter in password.get())):
            label1["text"] = "Password should be at least 8 characters long and should consists of special character"
        elif confirm_password.get() == "":
            label1["text"] = "Please repeat password"
        elif confirm_password.get() != password.get():
            label1["text"] = "Repeated password does not match password"
        elif email.get() == "":
            label1["text"] = "Please type email"
    
register_page()
    

def compare_data():
    pass

def login_page():
    
    for widgets in root.winfo_children():
      widgets.destroy()
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=3)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=2)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=2)
    root.rowconfigure(5, weight=6)
    root.rowconfigure(6, weight=2)
    root.rowconfigure(7, weight=2)
    
    label1 = tk.Label(root, text="", fg = "red")
    label1.grid(column=0, row = 0)
    
    label2 = ttk.Label(root, text="Username:")
    label2.grid(column=0, row = 1)
    
    username = ttk.Entry(root)
    username.grid(column=0, row = 2,sticky = "N")
    
    label3 = ttk.Label(root, text="Password:")
    label3.grid(column=0, row =  3)
    
    password = ttk.Entry(root)
    password.grid(column=0, row = 4,sticky = "N")
    
    label4 = ttk.Label(root, text="")
    label4.grid(column=0, row =  5)
    
    login_button = ttk.Button(root, text="Sign in", command=lambda: compare_data())
    login_button.grid(column=0, row = 6, sticky = "N")
    
    register_button = ttk.Button(root, text="Don't have an account? Register", command=lambda: register_page())
    register_button.grid(column=0, row =  7, sticky = "N")
    

root.mainloop()
