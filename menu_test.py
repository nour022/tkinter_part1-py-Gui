import tkinter as tk

def do_something():
    print("Something was done.")

root = tk.Tk()

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a File menu with two options
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=do_something)
file_menu.add_command(label="Save", command=do_something)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an Edit menu with one option
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=do_something)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Attach the menu bar to the root window
root.config(menu=menu_bar)

root.mainloop()
