import tkinter as tk
from tkinter import ttk
from math import factorial, exp, pi, sin, cos, tan, sqrt, log, log10, log2

# Global variables
calc_operator = ""

# Functions


def button_click(num):
    global calc_operator
    calc_operator += num
    text_input.set(calc_operator)


def button_equal():
    global calc_operator
    try:
        result = eval(calc_operator)
        text_input.set(result)
    except SyntaxError:
        pass
    calc_operator = ""


def clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set(calc_operator)


def delete_one():
    global calc_operator
    if len(calc_operator) > 0:
        calc_operator = calc_operator[:-1]
        text_input.set(calc_operator)

# Scientific functions


def factorial_button():
    try:
        result = factorial(int(calc_operator))
        text_input.set(result)
    except ValueError:
        pass


def trig_sin():
    try:
        result = sin(eval(calc_operator))
        text_input.set(result)
    except ValueError:
        pass


def trig_cos():
    try:
        result = cos(eval(calc_operator))
        text_input.set(result)
    except ValueError:
        pass


def trig_tan():
    try:
        result = tan(eval(calc_operator))
        text_input.set(result)
    except ValueError:
        pass


def trig_cot():
    try:
        result = 1 / tan(eval(calc_operator))
        text_input.set(result)
    except ValueError:
        pass


def square_root():
    try:
        result = sqrt(eval(calc_operator))
        text_input.set(result)
    except ValueError:
        pass


def log_base_10():
    try:
        result = log10(eval(calc_operator))
        text_input.set(result)
    except ValueError:
        pass


def log_base_2():
    try:
        result = log2(eval(calc_operator))
        text_input.set(result)
    except ValueError:
        pass


# Create the window
root = tk.Tk()
root.title("Fun Calculator")

# Set ttkthemes style
style = ttk.Style(root)
style.theme_use("clam")

# Set custom styles for themed buttons
style.configure("TButton",
                background="#4CAF50",  # Green background
                foreground="white",   # White text
                font=('Arial', 16),
                padding=10)

style.map("TButton",
          # Darker green when pressed or active
          background=[("pressed", "#45a049"), ("active", "#45a049")],
          foreground=[("pressed", "white"), ("active", "white")])

# Create the display
text_input = tk.StringVar()
display = ttk.Entry(root, textvariable=text_input, font=(
    'Arial', 20), justify='right', style='TEntry')
display.grid(row=0, column=0, columnspan=5, padx=10,
             pady=10, ipady=10, sticky='nsew')

# Create the buttons with custom styles
buttons = [
    ("7", lambda: button_click("7")),
    ("8", lambda: button_click("8")),
    ("9", lambda: button_click("9")),
    ("/", lambda: button_click("/")),
    ("AC", clear_all),

    ("4", lambda: button_click("4")),
    ("5", lambda: button_click("5")),
    ("6", lambda: button_click("6")),
    ("*", lambda: button_click("*")),
    ("DEL", delete_one),

    ("1", lambda: button_click("1")),
    ("2", lambda: button_click("2")),
    ("3", lambda: button_click("3")),
    ("-", lambda: button_click("-")),
    ("π", lambda: button_click(str(pi))),

    ("0", lambda: button_click("0")),
    (".", lambda: button_click(".")),
    ("EXP", lambda: button_click("EXP")),
    ("+", lambda: button_click("+")),
    ("=", button_equal),

    ("abs", lambda: button_click("abs(")),
    ("mod", lambda: button_click("%")),
    ("//", lambda: button_click("//")),
    ("x!", factorial_button),
    ("sin", trig_sin),
    ("cos", trig_cos),
    ("tan", trig_tan),
    ("cot", trig_cot),
    ("√", square_root),
    ("log10", log_base_10),
    ("log2", log_base_2),
]

# Configure row and column weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Create and place the buttons with ttk.Button
row_val = 1
col_val = 0
for (text, command) in buttons:
    ttk.Button(root, text=text, style='TButton', command=command).grid(
        row=row_val, column=col_val, sticky='nsew')
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

root.mainloop()
