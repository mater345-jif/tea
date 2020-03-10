import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def hello():
    print(f"I deceivied You, {entered_name.get() or '!'}")



root = tk.Tk()
root.title("Hello")

entered_name = tk.StringVar()

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))

name_getter = ttk.Entry(root, width=15, textvariable=entered_name)
name_getter.pack(side="left")
hello_button = ttk.Button(root, text="I'm not doing anything", command=hello)
hello_button.pack(side="left")

exit_button = ttk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(side="right")

root.mainloop()