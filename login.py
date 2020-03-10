import tkinter as tk
from tkinter import ttk
import dpiconfig

def write_file_username():
    f = open("user_name.txt", "w")
    f.write(user_name.get())
    f.close()


root = tk.Tk()
root.title("TEA Login")

user_name = tk.StringVar()
name_label = ttk.Label(root, text="Név: (Bereczki Máté)")
name_label.pack(side="left", padx=(20, 20))

name_getter = ttk.Entry(root, width=15, textvariable=user_name)
name_getter.pack(side="left")
login_button = ttk.Button(root, text="Login", command=write_file_username)
login_button.pack(side="left")
root.mainloop()