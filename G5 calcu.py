import tkinter as tk
from tkinter import messagebox

# Global history and memory
history = []
memory = 0

# Arithmetic functions
def subtract(a, b): return a - b
def add (a, b): return a + b
def def multiply(a, b): return a * b
def divide(a, b):
    if z == 0:
        messagebox.showerror("Error", "Undefined")
        return None
    return a / b
def modulus(a, b):
    if z == 0:
        messagebox.showerror("Error", "Cannot perform modulus by zero")
        return None
    return a % b

# Update history
def update_history(num1, op, num2, result):
    if result is not None:
        history.append(f"{num1} {op} {num2} = {result}")
    else:
        history.append(f"{num1} {op} {num2} = Error")

# Show history
def show_history():
    if not history:
        messagebox.showinfo("History", "No history yet.")
    else:
        messagebox.showinfo("History", "\n".join(history))

# Clear history
def clear_history():
    history.clear()
    messagebox.showinfo("History", "Calculation history cleared.")

# Perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        elif op == "%":
            result = modulus(num1, num2)
        else:
            result = "Invalid operation"

        if result is not None:
            result_label.config(text=f"Result: {result}")
        else:
            result_label.config(text="Result: Error")

        update_history(num1, op, num2, result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Memory functions
def memory_add():
    global memory
    try:
        value = float(result_label.cget("text").split(":")[1].strip())
        memory += value
        messagebox.showinfo("Memory", f"Added to memory: {memory}")
    except:
        messagebox.showerror("Memory Error", "No valid result to add.")

def memory_subtract():
    global memory
    try:
        value = float(result_label.cget("text").split(":")[1].strip())
        memory -= value
        messagebox.showinfo("Memory", f"Subtracted from memory: {memory}")
    except:
        messagebox.showerror("Memory Error", "No valid result to subtract.")

def memory_recall():
    entry1.delete(0, tk.END)
    entry1.insert(0, str(memory))
    messagebox.showinfo("Memory", f"Recalled memory: {memory}")

def memory_clear():
    global memory
    memory = 0
    messagebox.showinfo("Memory", "Memory cleared.")

# GUI setup
root = tk.Tk()
root.title("G5 Calculator")

tk.Label(root, text="First Number").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Operation").grid(row=2, column=0)
operation = tk.StringVar(root)
operation.set("+")
tk.OptionMenu(root, operation, "+", "-", "*", "/", "%").grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0)
tk.Button(root, text="Show History", command=show_history).grid(row=3, column=1)
tk.Button(root, text="Clear History", command=clear_history).grid(row=4, column=1)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0)

# Memory buttons
tk.Button(root, text="M+", command=memory_add).grid(row=5, column=0)
tk.Button(root, text="M-", command=memory_subtract).grid(row=5, column=1)
tk.Button(root, text="MR", command=memory_recall).grid(row=6, column=0)
tk.Button(root, text="MC", command=memory_clear).grid(row=6, column=1)

root.mainloop()
