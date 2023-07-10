import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Button')
window.geometry('600x400')

# button
def button_func():
    print('A basic button')

button_string = tk.StringVar(value='A button with string var')
button = ttk.Button(window, text='Smiple button', command=button_func)
button.pack()






# Run
window.mainloop()