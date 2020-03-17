import tkinter as tk
from tkinter import ttk
import dpiconfig
from PIL import ImageTk, Image
import os
pwd = __file__
print(pwd)

boolean = None
user_name_saved = None

def write_fl_name():
    # checking is needed if the /tmp folder is exists.
    is_path_exist = os.path.isdir('./tmp')  # True if yes, False if not
    if is_path_exist is False:
        create_tmp_folder = "tmp"
        try:
            os.mkdir(create_tmp_folder)
        except OSError:
            print ("Creation of the directory %s failed" % create_tmp_folder)
    f = open(r"tmp\user_name.txt", "w")
    f.write(user_name.get())
    f.close()
    root.destroy()

# If we know what is the user id, we should simple skip the login process.
def login_as_saved():
    root.destroy()


try:
    f = open(r"tmp\user_name.txt", "r")
    user_name_saved = f.read()
    print(user_name_saved)
    boolean = True
    f.close()
except:
    print("Something went wrong when writing to the file")
    boolean = False



#print(boolean)

# Declarring main window with size. Users cannot resize the window.
root = tk.Tk()
root.title("TEA Login")
root.geometry("800x600")
root.resizable(0, 0)

# Declaring the tea icon and pack it to the top
img = Image.open('./tea.png')
img = img.resize((250, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = tk.Label(root, image = img)
panel.pack(side = "left", fill = "x")
tea_label = ttk.Label(root, text="Túlóra Elszámóló Apllikáció")
tea_label.pack(side="top", padx=(20, 20), fill = "y")

if boolean is True:
    user_name = tk.StringVar()
    name_label = ttk.Label(root, text="WiW ID: " + user_name_saved)
    name_label.pack(side="top", padx=(20, 20), fill = "y")
    login_button = ttk.Button(root, text="Login as " + user_name_saved, command=login_as_saved)
    login_button.pack(side="top", fill = "x")
    login1_button = ttk.Button(root, text="Login as other:", command=write_fl_name)
    login1_button.pack(side="top", fill = "y")
    name_getter = ttk.Entry(root, width=15, textvariable=user_name)
    name_getter.pack(side="top", fill = "y")
    
else:
    user_name = tk.StringVar()
    name_label = ttk.Label(root, text="WiW ID: ")
    name_label.pack(side="left", padx=(20, 20))

    name_getter = ttk.Entry(root, width=15, textvariable=user_name)
    name_getter.pack(side="left")
    login_button = ttk.Button(root, text="Login", command=write_fl_name)
    login_button.pack(side="left")
# kampeco
root.mainloop()