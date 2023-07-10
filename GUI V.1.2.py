import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()
    label['text'] = entry_text
    entry['state'] = 'disabeld'

def knapp():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

window = tk.Tk()
window.title('Getting and setting widgets')

label = ttk.Label(master=window, text = 'Jesus is king')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='Done', command=button_func)
button.pack()

knapp = ttk.Button(master=window, text="you done", command=knapp)
knapp.pack()


window.mainloop()