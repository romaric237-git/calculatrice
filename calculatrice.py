#!/usr/bin/env python3
import tkinter as tk
import numpy as np
from tkinter import font

HEIGHT = 700
WIDTH = 500

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

myFont = font.Font(family='Helvetica', size=40)
font.families()

frame = tk.Frame(root, bg='blue')
frame.place(relx=0.1, rely=0.18, relwidth=0.8, relheight=0.75)

field = tk.Text(root, bg='#5481C4', font=myFont)
field.place(relx=0.1, rely=0.04, relwidth=0.8, relheight=0.09)

exp = ""
last_result = False

def add_to_exp(sth):
    global exp, last_result
    if last_result:
        exp = ""
        last_result = False
    exp = exp + str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", exp)

def calc():
    global exp, last_result
    try:
        result = str(eval(exp))
        field.delete("1.0", "end")
        field.insert("1.0", result)
        exp = result
        last_result = True
    except:
        field.delete("1.0", "end")
        field.insert("1.0", "Erreur")

def clear():
    global exp
    exp = ""
    field.delete("1.0", "end")

def b_s():
    global exp
    exp = exp[:-1]
    field.delete("1.0", "end")
    field.insert("1.0", exp)

def clear_field(event):
    """Efface le champ de texte lorsque n'importe quelle touche est pressée."""
    clear()

# Lier l'événement de pression de touche à la fonction clear_field
root.bind("<Key>", clear_field)

# Boutons numériques
button_1 = tk.Button(frame, text='1', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(1))
button_1.place(relx=0, rely=0, relwidth=0.25, relheight=0.2)

button_2 = tk.Button(frame, text='2', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(2))
button_2.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.2)

button_3 = tk.Button(frame, text='3', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(3))
button_3.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.2)

button_4 = tk.Button(frame, text='4', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(4))
button_4.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.2)

button_5 = tk.Button(frame, text='5', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(5))
button_5.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.2)

button_6 = tk.Button(frame, text='6', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(6))
button_6.place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.2)

button_7 = tk.Button(frame, text='7', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(7))
button_7.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.2)

button_8 = tk.Button(frame, text='8', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(8))
button_8.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.2)

button_9 = tk.Button(frame, text='9', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(9))
button_9.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2)

button_0 = tk.Button(frame, text='0', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(0))
button_0.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.2)

button_decimal = tk.Button(frame, text='.', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp("."))
button_decimal.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.2)

button_clear = tk.Button(frame, text='C', bg='gray', fg='red', font=myFont, command=lambda: clear())
button_clear.place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.2)

button_open_paren = tk.Button(frame, text='(', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp("("))
button_open_paren.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

button_close_paren = tk.Button(frame, text=')', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp(")"))
button_close_paren.place(relx=0.25, rely=0.8, relwidth=0.25, relheight=0.2)

button_bs = tk.Button(frame, text='BS', bg='gray', fg='red', font=myFont, command=lambda: b_s())
button_bs.place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.2)

######### math symbols buttons 
button_p = tk.Button(frame, text='+', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp("+"))
button_p.place(relx=0.75, rely=0.0, relwidth=0.25, relheight=0.2)

button_m = tk.Button(frame, text='-', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp("-"))
button_m.place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.2)

button_d = tk.Button(frame, text='/', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp("/"))
button_d.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.2)

button_c = tk.Button(frame, text='x', bg='gray', fg='red', font=myFont, command=lambda: add_to_exp("*"))
button_c.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.2)

button_eq = tk.Button(frame, text='=', bg='gray', fg='red', font=myFont, command=lambda: calc())
button_eq.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

root.mainloop()
