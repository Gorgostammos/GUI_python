import tkinter as tk
from tkinter import ttk

def Knapp():
    print(string_var.get())
    string_var.set('OK')


# window
window = tk.Tk()
window.title('Tkinter variables')

#Tkinter variables
string_var = tk.StringVar()


# Widgets
label = ttk.Label(master=window, text='label', textvariable= string_var)
label.pack()

# Entry
entry = ttk.Entry(master=window, textvariable= string_var)
entry.pack()

button = ttk.Button(master=window, text='Done', command= Knapp)
button.pack()
# RUN
window.mainloop()