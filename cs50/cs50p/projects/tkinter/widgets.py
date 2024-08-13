import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()
    
    label["text"] = entry_text
    entry["state"] = "disabled"
    

def exercise_button_func():
    label["text"] = "some text"
    entry["state"] = "enabled"
    
    

#window setup
window = tk.Tk()
window.title("Getting and Setting Widgets")
window.geometry("800x500")

#creating a label widget
label = ttk.Label(master = window, text = "Some text")
label.pack()

#entry widget
entry = ttk.Entry(master = window)
entry.pack()

#creating a button widget
button = ttk.Button(master = window, text = "Click me", command = button_func)
button.pack()

#another label widget
exercise_button = ttk.Button(master = window, text = "Enable", command = exercise_button_func)
exercise_button.pack()

#run
window.mainloop()