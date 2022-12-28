import sqlite3
from tkinter.messagebox import showinfo
import tkinter as tk

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("create table users (username text, password text, email text)")

tk.messagebox.showinfo(message="SQLite table created")

connection.close