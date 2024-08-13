import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

#* What to do when convert button is clicked
def convert_temperature():
    fahrenheit_input = entry_int.get()
    celsius_output = (fahrenheit_input - 32) * 5/9
    output_string.set(f"{celsius_output:.2f} °C")
    
    
#  window
window = ttk.Window(themename = "journal")
window.title("Degree converter")
window.geometry("400x200")

#title
title_label = ttk.Label(master = window, text = "Fahrenheit to Celsius", font = "Calibri 24 bold")
title_label.pack()

#input
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
convert_button = ttk.Button(master = input_frame, 
                            text = "Convert", 
                            command = convert_temperature
                            )
entry.pack(side = "left", padx = 10)
convert_button.pack(side = "left")
input_frame.pack(pady = 20)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, 
                         text = "Celsius", 
                         font = "Calibri 28 bold", 
                         textvariable = output_string
                         )
output_label.pack()


#run
window.mainloop()
 