import tkinter as tk
from tkinter import ttk

#window setup
window = tk.Tk()
window.title("buttons")
window.geometry("600x400")

#basic button
def button_func():
    print("A basic button ")

button_string = tk.StringVar(value = "A button with string var")
button = ttk.Button(master = window, 
                    text = "A simple button", 
                    textvariable = button_string, 
                    command = button_func)
button.pack()

#checkbutton
check_var = tk.IntVar(value = 10)
check1 = ttk.Checkbutton(master = window, text = "checkbox 1",
                        command = lambda: print(check_var.get()),
                        variable = check_var,
                        onvalue = 10, offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(master = window, text = "checkbox 2",
                         command = lambda: print("testing"))
                         
check2.pack()

#radio button(s)
radio_var = tk.IntVar()
radio1 = ttk.Radiobutton(master = window, 
                         text = "Radiobutton 1", 
                         value = 1,
                         variable = radio_var,
                         command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(master = window, 
                         text = "Radiobutton 2", 
                         value = 2,
                         variable = radio_var,
                         command = lambda: print(radio_var.get()))
radio2.pack()

#exercise buttons
def click_check3():
    print(radio_var3.get())
check_var = tk.BooleanVar(value = False)
checkbutton3 = ttk.Checkbutton(master = window, 
                               text = "Checkbutton 3",
                               variable = check_var,
                               command = click_check3)
checkbutton3.pack()

#radios
def click_radio():
    print(check_var.get())
    check_var.set(value = False)
    

radio_var3 = tk.StringVar()

radio3 = ttk.Radiobutton(master = window, text = "Radiobutton 3",
                         value = "A",
                         variable = radio_var3,
                         command = click_radio)
radio3.pack()

radio4 = ttk.Radiobutton(master = window, text = "Radiobutton 4",
                         value = "B",
                         variable = radio_var3,
                         command = click_radio)
radio4.pack()




#run
window.mainloop()