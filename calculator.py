# # Python program for simple calculator

# # Function to add two numbers
# def add(num1, num2):
# 	return num1 + num2

# # Function to subtract two numbers
# def subtract(num1, num2):
# 	return num1 - num2

# # Function to multiply two numbers
# def multiply(num1, num2):
# 	return num1 * num2

# # Function to divide two numbers
# def divide(num1, num2):
# 	return num1 / num2

# print("Please select operation -\n" \
# 		"1. Add\n" \
# 		"2. Subtract\n" \
# 		"3. Multiply\n" \
# 		"4. Divide\n")


# # Take input from the user
# select = int(input("Select operations form 1, 2, 3, 4 :\n"))

# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number: "))

# if select == 1:
# 	print(number_1, "+", number_2, "=",
# 					add(number_1, number_2))

# elif select == 2:
# 	print(number_1, "-", number_2, "=",
# 					subtract(number_1, number_2))

# elif select == 3:
# 	print(number_1, "*", number_2, "=",
# 					multiply(number_1, number_2))

# elif select == 4:
# 	print(number_1, "/", number_2, "=",
# 					divide(number_1, number_2))
# else:
# 	print("Invalid input")


import tkinter as tk
from tkinter import ttk

# Functions for operations
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input!")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input!")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input!")

def divide():
    try:
        if float(entry2.get()) == 0:
            label_result.config(text="Error! Division by zero.")
        else:
            result = float(entry1.get()) / float(entry2.get())
            label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input!")

# Create the main window
root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# Styles for widgets
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
style.configure("TEntry", font=("Helvetica", 12), padding=5)

# Frame for input fields and labels
frame_inputs = ttk.Frame(root, padding="10")
frame_inputs.pack(pady=20)

# Labels and entry widgets
label1 = ttk.Label(frame_inputs, text="Enter first number:")
label1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry1 = ttk.Entry(frame_inputs, width=20)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = ttk.Label(frame_inputs, text="Enter second number:")
label2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry2 = ttk.Entry(frame_inputs, width=20)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Frame for buttons
frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.pack()

# Buttons for operations
button_add = ttk.Button(frame_buttons, text="Add", command=add, style="TButton")
button_add.grid(row=0, column=0, padx=10, pady=5)

button_subtract = ttk.Button(frame_buttons, text="Subtract", command=subtract, style="TButton")
button_subtract.grid(row=0, column=1, padx=10, pady=5)

button_multiply = ttk.Button(frame_buttons, text="Multiply", command=multiply, style="TButton")
button_multiply.grid(row=0, column=2, padx=10, pady=5)

button_divide = ttk.Button(frame_buttons, text="Divide", command=divide, style="TButton")
button_divide.grid(row=0, column=3, padx=10, pady=5)

# Label to display the result
label_result = ttk.Label(root, text="Result:", font=("Helvetica", 14))
label_result.pack(pady=20)

# Run the application
root.mainloop()
