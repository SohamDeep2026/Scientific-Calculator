from tkinter import Tk, END, Entry, SUNKEN, Button, INSERT
from math import (
    sin,
    cos,
    tan,
    asin,
    acos,
    atan,
    degrees,
    radians,
    sqrt,
    pi,
    e,
    log,
    log10,
)


def click(value, test_check_list):
    try:
        text = str(entry_field.get())

        if value == "C":
            text = text[: len(text) - 1]
            entry_field.delete(0, END)
            entry_field.insert(0, text)
        elif value == "CE":
            entry_field.delete(0, END)
        elif value == "π":
            entry_field.insert(INSERT, "π")
        elif value == "e":
            entry_field.insert(INSERT, "e")
        elif value == "(":
            entry_field.insert(INSERT, "(")
        elif value == ")":
            entry_field.insert(INSERT, ")")
        elif value == "sin":
            entry_field.insert(INSERT, "sin()")
        elif value == "cos":
            entry_field.insert(INSERT, "cos()")
        elif value == "tan":
            entry_field.insert(INSERT, "tan()")
        elif value == "asin":
            entry_field.insert(INSERT, "asin()")
        elif value == "acos":
            entry_field.insert(INSERT, "acos()")
        elif value == "atan":
            entry_field.insert(INSERT, "atan()")
        elif value == "x^2":
            entry_field.insert(INSERT, "^2")
        elif value == "x^y":
            entry_field.insert(INSERT, "^")
        elif value == "log10":
            entry_field.insert(INSERT, "log10()")
        elif value == "ln":
            entry_field.insert(INSERT, "ln")
        elif value == "√x":
            entry_field.insert(INSERT, "√()")
        elif value == "x!":
            entry_field.insert(INSERT, "!")
        elif value == "%":
            entry_field.delete(0, END)
            a = (
                eval(
                    text.replace("deg", "degrees")
                    .replace("rad", "radians")
                    .replace("^", "**")
                    .replace("ln", "log")
                    .replace("√", "sqrt")
                    .replace("ln10", "log10")
                    .replace("x", "*")
                    .replace("π", "pi")
                )
                * 100
            )
            if a < 0.001:
                output = "{:.3g}".format(a)
            else:
                output = "{:.5f}".format(a)
            entry_field.insert(END, output)
        elif value == "+":
            entry_field.insert(INSERT, "+")
        elif value == "-":
            entry_field.insert(INSERT, "-")
        elif value == "x":
            entry_field.insert(INSERT, "x")
        elif value == "/":
            entry_field.insert(INSERT, "/")
        elif value == "deg":
            entry_field.insert(INSERT, "deg()")
        elif value == "rad":
            entry_field.insert(INSERT, "rad()")
        elif value == "=":
            test_check = text
            for j in test_check_list:
                test_check = test_check.replace(j, "")
            if test_check != "":
                a = int("a")
            entry_field.delete(0, END)
            a = eval(
                text.replace("deg", "degrees")
                .replace("rad", "radians")
                .replace("^", "**")
                .replace("ln", "log")
                .replace("√", "sqrt")
                .replace("ln10", "log10")
                .replace("x", "*")
                .replace("π", "pi")
            )
            if a < 0.001:
                output = str(round(a, 10))
            else:
                output = "{:.5f}".format(a)
            entry_field.insert(END, output)
        else:
            entry_field.insert(INSERT, value)
    except ValueError:
        entry_field.delete(0, END)
        entry_field.insert(INSERT, "Invalid input")
    except SyntaxError:
        entry_field.delete(0, END)
        entry_field.insert(INSERT, "Invalid input")
    except NameError:
        entry_field.delete(0, END)
        entry_field.insert(INSERT, "Invalid input")
    except TypeError:
        entry_field.delete(0, END)
        entry_field.insert(INSERT, "Invalid input")


root = Tk()
root.title("Calculator")
root.config(bg="#222222")
root.geometry("452x350+150+125")

entry_field = Entry(
    root, font=("calibri", 20, "bold"), bg="#E6E6E6", fg="#040404", bd=14, relief=SUNKEN
)
entry_field.grid(row=0, column=0, columnspan=5)

test_check_list = [
    "π",
    "e",
    "(",
    ")",
    "+",
    "sin",
    "cos",
    "tan",
    "7",
    "8",
    "9",
    "-",
    "asin",
    "acos",
    "atan",
    "4",
    "5",
    "6",
    "x",
    "^",
    "log10",
    "1",
    "2",
    "3",
    "/",
    "√",
    "!",
    "ln",
    "0",
    ".",
]

button = Button(
    root,
    width=5,
    height=2,
    bd=4,
    relief=SUNKEN,
    text="deg",
    bg="#404040",
    fg="#FFFFFF",
    font=("arial", 13, "bold"),
    activebackground="#adadad",
    activeforeground="#FFFFFF",
    command=lambda button="deg": click(button, test_check_list),
)
button.grid(row=0, column=5)
button = Button(
    root,
    width=5,
    height=2,
    bd=4,
    relief=SUNKEN,
    text="rad",
    bg="#404040",
    fg="#FFFFFF",
    font=("arial", 13, "bold"),
    activebackground="#adadad",
    activeforeground="#FFFFFF",
    command=lambda button="rad": click(button, test_check_list),
)
button.grid(row=0, column=6)
button_list = [
    "C",
    "CE",
    "π",
    "e",
    "(",
    ")",
    "+",
    "sin",
    "cos",
    "tan",
    "7",
    "8",
    "9",
    "-",
    "asin",
    "acos",
    "atan",
    "4",
    "5",
    "6",
    "x",
    "x^2",
    "x^y",
    "log10",
    "1",
    "2",
    "3",
    "/",
    "√x",
    "x!",
    "ln",
    "%",
    "0",
    ".",
    "=",
]
row_val = 1
col_val = 0
for i in button_list:
    if col_val < 2 and row_val == 1:
        button = Button(
            root,
            width=5,
            height=2,
            bd=4,
            relief=SUNKEN,
            text=i,
            bg="#C55A11",
            fg="#FFFFFF",
            font=("arial", 13, "bold"),
            activebackground="#F2A36E",
            activeforeground="#FFFFFF",
            command=lambda button=i: click(button, test_check_list),
        )
        button.grid(row=row_val, column=col_val)
    elif (
        (col_val == 3 or col_val == 4 or col_val == 5)
        and (row_val == 2 or row_val == 3 or row_val == 4)
    ) or (col_val == 4 and row_val == 5):
        button = Button(
            root,
            width=5,
            height=2,
            bd=4,
            relief=SUNKEN,
            text=i,
            bg="#737373",
            fg="#FFFFFF",
            font=("arial", 13, "bold"),
            activebackground="#adadad",
            activeforeground="#FFFFFF",
            command=lambda button=i: click(button, test_check_list),
        )
        button.grid(row=row_val, column=col_val)
    elif col_val == 6 and row_val == 5:
        button = Button(
            root,
            width=5,
            height=2,
            bd=4,
            relief=SUNKEN,
            text=i,
            bg="#D6A300",
            fg="#FFFFFF",
            font=("arial", 13, "bold"),
            activebackground="#FFDA65",
            activeforeground="#FFFFFF",
            command=lambda button=i: click(button, test_check_list),
        )
        button.grid(row=row_val, column=col_val)
    elif col_val == 6 and row_val > 0:
        button = Button(
            root,
            width=5,
            height=2,
            bd=4,
            relief=SUNKEN,
            text=i,
            bg="#4472C4",
            fg="#FFFFFF",
            font=("arial", 13, "bold"),
            activebackground="#96B0DE",
            activeforeground="#FFFFFF",
            command=lambda button=i: click(button, test_check_list),
        )
        button.grid(row=row_val, column=col_val)
    else:
        button = Button(
            root,
            width=5,
            height=2,
            bd=4,
            relief=SUNKEN,
            text=i,
            bg="#404040",
            fg="#FFFFFF",
            font=("arial", 13, "bold"),
            activebackground="#adadad",
            activeforeground="#FFFFFF",
            command=lambda button=i: click(button, test_check_list),
        )
        button.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val == 7:
        col_val = 0
        row_val += 1

root.mainloop()