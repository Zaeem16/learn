import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    #setting the value of the variable when the button is clicked
    string_var.set("button clicked")

#window setup
window = tk.Tk()
window.title("Tkinter Variables")

#tkinter variable
string_var = tk.StringVar(value = "0")
exercise_string_var = tk.StringVar(value = "test")
#exercise_string_var.set("test")


#widgets
label = ttk.Label(master = window, text = "label", textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

#entry2 = ttk.Entry(master = window, textvariable = string_var)
#entry2.pack()

button = ttk.Button(master = window, text = "button", command = button_func)
button.pack()

#exercise label
exercise_label = ttk.Label(master = window, 
                           textvariable = exercise_string_var)
exercise_label.pack()

#exercise entry1
exercise_entry1 = ttk.Entry(master = window, textvariable = exercise_string_var)
exercise_entry1.pack()

#exercise entry2
exercise_entry2 = ttk.Entry(master = window, textvariable = exercise_string_var)
exercise_entry2.pack()


#run
window.mainloop()