import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math
import sys

root = tk.Tk()
root["bg"] = "#000"
root.title("ЕВРЕЙСКИЙ КАЛЬКУЛЯТОР")
root.geometry("400x350")
root.minsize(300, 300)
root.maxsize(600, 600)

bttn_list = [
"7", "8", "9", "+", "*", 
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
"0", ".", "±",  "C",
"Exit", "π", "sin", "cos",
"(", ")","n!","√2", "Я ДОЛЖЕН", "ТЫ ДОЛЖЕН"]

a = 1
b = 0
for i in bttn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    tk.Button(root, text=i, bg = "#000", fg = "#b7f731", font = "arial 13", command = cmd).grid(row=a, column=b, sticky="nsew")
    b += 1
    if b > 4:
        b = 0
        a += 1

call_entry = Entry(root, width = 50)
call_entry.grid(row=0, column=0, columnspan=5)

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_columnconfigure(2, weight = 1)
root.grid_columnconfigure(3, weight = 1)
root.grid_columnconfigure(4, weight = 1)

root.grid_rowconfigure(0, weight = 0)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)
root.grid_rowconfigure(4, weight = 1)
root.grid_rowconfigure(5, weight = 1)
root.grid_rowconfigure(6, weight = 1)

def calc(key):
    if key == "=":
        strdop = "0123456789-+.*/()"
        if call_entry.get()[0] not in strdop:
            call_entry.insert(END, "Ошибка!")
            messagebox.showerror("Это недопустимый символ!")

        try:
            result = eval(call_entry.get())
            call_entry.insert(END, "=" + str(result))
        except:
            call_entry.insert(END, "Ошибка!")
            messagebox.showerror("Проверь корректность данных!")

    elif key == "C":
        call_entry.delete(0, END)

    elif key == "±":
        if "=" in call_entry.get():
            call_entry.delete(0, END)

        try:
            if call_entry.get()[0] == "-":
                call_entry.delete(0)
            else:
                call_entry.insert(0, "-")

        except IndexError:
            pass

    elif key == "Exit":
        root.after(0, root.destroy)
        sys.exit

    elif key == "√2":
        call_entry.insert(END, "=" + str(math.sqrt(int(call_entry.get()))))

    elif key == "n!":
        call_entry.insert(END, "=" + str(math.factorial(int(call_entry.get()))))

    elif key == "sin":
        call_entry.insert(END, "=" + str(math.sin(int(call_entry.get()))))

    elif key == "cos":
        call_entry.insert(END, "=" + str(math.cos(int(call_entry.get()))))

    elif key == "π":
        call_entry.insert(END, math.pi)

    elif key == "xⁿ":
        call_entry.insert(END, "**")

    elif key == "(":
        call_entry.insert(END, "(")

    elif key == ")":
        call_entry.insert(END, ")")

    elif key == "Я ДОЛЖЕН":
        call_entry.insert(END, "/10")

    elif key == "ТЫ ДОЛЖЕН":
        call_entry.insert(END, "*10")

    else:
        if "=" in call_entry.get():
            call_entry.delete(0, END)
        call_entry.insert(END, key)

root.mainloop()