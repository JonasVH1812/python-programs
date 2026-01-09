import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Test")
root.geometry("300x200")
def say_hello():
    combo = ttk.Combobox(root, values=["Red", "Green", "Blue"])
    combo.pack()
    combo.current(0)
tk.Button(root, text="Click Me", command=say_hello).pack()
root.mainloop()


