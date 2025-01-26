from tkinter import *
from tkinter import messagebox
root = Tk()

root.option_add('*background', 'black')
root.title('My Calculator')

i = 0

#Data entry

entry = Entry(root, font=('Curier 20'), foreground='white', background='black')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

def click(val):
    global i
    entry.insert(i, val)
    i += 1

def delete():
    entry.delete(0, END)
    i = 0

def operatioon():
    ope = entry.get()
    try:
        res = eval(ope)
        delete()
        entry.insert(0, res)
    except SyntaxError:
        messagebox.showerror("Error de Sintaxis", "La expresión ingresada no es válida.")
        delete()
    except Exception as e: # Capturamos otros tipos de errores generales
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")
        delete()

#Buttons

button1 = Button(root, text='1', width=8, height=2, command=lambda:click(1), foreground='white', background='black', font=('Curier 12'))
button2 = Button(root, text='2', width=8, height=2, command=lambda:click(2), font=('Curier 12'), foreground='white', background='black')
button3 = Button(root, text='3', width=8, height=2, command=lambda:click(3),  font=('Curier 12'), foreground='white', background='black')
button4 = Button(root, text='4', width=8, height=2, command=lambda:click(4), font=('Curier 12'), foreground='white', background='black')
button5 = Button(root, text='5', width=8, height=2, command=lambda:click(5), font=('Curier 12'), foreground='white', background='black')
button6 = Button(root, text='6', width=8, height=2, command=lambda:click(6),  font=('Curier 12'), foreground='white', background='black')
button7 = Button(root, text='7', width=8, height=2, command=lambda:click(7), font=('Curier 12'), foreground='white', background='black')
button8 = Button(root, text='8', width=8, height=2, command=lambda:click(8), font=('Curier 12'), foreground='white', background='black')
button9 = Button(root, text='9', width=8, height=2, command=lambda:click(9), font=('Curier 12'), foreground='white', background='black')
button0 = Button(root, text='0', width=13, height=2, command=lambda:click(0), font=('Curier 14'), foreground='white', background='black')

button_delete = Button(root, text='DEL', width=5, height=2, command=lambda:delete(), font=('Curier 12'), foreground='white', background='black')
button_leftparenth = Button(root, text='(', width=5, height=2, command=lambda:click('('),  font=('Curier 12'), foreground='white', background='black')
button_rightparenth = Button(root, text=')', width=5, height=2, command=lambda:click(')'),  font=('Curier 12'), foreground='white', background='black')
button_point = Button(root, text='.', width=5, height=2, font=('Curier 14'), command=lambda:click('.'), foreground='white', background='black')

#Operations

button_addition = Button(root, text='+', width=5, height=2, command=lambda:click('+'), font=('Curier 14'), foreground='white', background='black')
button_substraction = Button(root, text='-', width=5, height=2, command=lambda:click('--'), font=('Curier 14'), foreground='white', background='black')
button_multiplicatiion = Button(root, text='*', width=5, height=2,  font=('Curier 14'), command=lambda:click('*'), foreground='white', background='black')
button_division = Button(root, text='/', width=5, height=2, font=('Curier 12'), command=lambda:click('/'),foreground='white', background='black')
button_equal = Button(root, text='=', width=5, height=2, command=lambda:operatioon(), font=('Curier 14'), foreground='white', background='black')

button_delete.grid(row=1, column=0, padx=5, pady=5)
button_leftparenth.grid(row=1, column=1, padx=5, pady=5)
button_rightparenth.grid(row=1, column=2, padx=5, pady=5)
button_division.grid(row=1, column=3, padx=5, pady=5)

button7.grid(row=2, column=0, padx=5, pady=5)
button8.grid(row=2, column=1, padx=5, pady=5)
button9.grid(row=2, column=2, padx=5, pady=5)
button_multiplicatiion.grid(row=2, column=3, padx=5, pady=5)

button4.grid(row=3, column=0, padx=5, pady=5)
button5.grid(row=3, column=1, padx=5, pady=5)
button6.grid(row=3, column=2, padx=5, pady=5)
button_addition.grid(row=3, column=3, padx=5, pady=5)

button1.grid(row=4, column=0, padx=5, pady=5)
button2.grid(row=4, column=1, padx=5, pady=5)
button3.grid(row=4, column=2, padx=5, pady=5)
button_substraction.grid(row=4, column=3, padx=5, pady=5)

button0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
button_point.grid(row=5, column=2, padx=5, pady=5)
button_equal.grid(row=5, column=3, padx=5, pady=5)

root.mainloop()
