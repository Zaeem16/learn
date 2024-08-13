import tkinter as tk
from tkinter import ttk

#window setup
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

#ttk label
label = ttk.Label(master = window, text = "This is a test")
label.pack()

#ttk textbox
textbox = tk.Text(master = window)
textbox.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#my label
my_label = ttk.Label(master = window, text = "My Label")
my_label.pack()

#ttk button
button = ttk.Button(master = window, text = "A button", 
                    command = lambda: print("A button was pressed"))
button.pack()

#my button
my_button = ttk.Button(master = window, text = "Click me", 
                       command = lambda: print("hello"))
my_button.pack()

#run window
window.mainloop()

