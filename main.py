import tkinter as tk
from tkinter import ttk


def button_fuck():
    print('Fuck you')


window = tk.Tk()
window.title('widow and widgets')
window.geometry('800x500')


label = ttk.Label(master=window, text='text is a test')
label.pack()

text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='Done', command=button_fuck)
button.pack()

window.mainloop()
