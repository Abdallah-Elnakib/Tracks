import tkinter as tk
from tkinter import messagebox
import json

DATA_PATH = "D:/Tracks/Python 1/Day 12/taskAnswre/data.json"

def load_data():
    with open(DATA_PATH, "r") as file:
        return json.load(file)

def save_data(new_data):
    with open(DATA_PATH, "w") as file:
        json.dump(new_data, file, indent=4)

data = load_data()
master = tk.Tk()
master.title("Product Info Editor")
master.geometry("400x250")
master.config(bg="#f0f0f0")


def refresh_labels():
    data.update(load_data())
    name_label.config(text=f"Name: {data['name']}")
    price_label.config(text=f"Price: {data['price']}")
    quantity_label.config(text=f"Quantity: {data['quantity']}")
    description_label.config(text=f"Description: {data['description']}")


def edit_field(field, prompt, cast_type=str):
    def change_data():
        new_value = entry.get()
        try:
            data[field] = cast_type(new_value)
            save_data(data)
            refresh_labels()
            top.destroy()
        except ValueError:
            messagebox.showerror("Error", f"Invalid input for {field}")

    top = tk.Toplevel(master)
    top.title(f"Edit {field}")
    top.geometry("300x100")
    tk.Label(top, text=prompt, font=("Arial", 10)).pack(pady=5)
    entry = tk.Entry(top, width=30)
    entry.pack(pady=5)
    tk.Button(top, text="Save", command=change_data, bg="#4CAF50", fg="white").pack(pady=5)

# الواجهة
frame = tk.Frame(master, bg="#ffffff", bd=2, relief="groove", padx=10, pady=10)
frame.pack(pady=20)

name_label = tk.Label(frame, text=f"Name: {data['name']}", font=("Arial", 12), bg="white")
price_label = tk.Label(frame, text=f"Price: {data['price']}", font=("Arial", 12), bg="white")
quantity_label = tk.Label(frame, text=f"Quantity: {data['quantity']}", font=("Arial", 12), bg="white")
description_label = tk.Label(frame, text=f"Description: {data['description']}", font=("Arial", 12), bg="white")

name_label.grid(row=0, column=0, sticky="w", pady=5)
price_label.grid(row=1, column=0, sticky="w", pady=5)
quantity_label.grid(row=2, column=0, sticky="w", pady=5)
description_label.grid(row=3, column=0, sticky="w", pady=5)

tk.Button(frame, text="Edit", command=lambda: edit_field('name', "Enter new product name"), bg="#2196F3", fg="white").grid(row=0, column=1, padx=10)
tk.Button(frame, text="Edit", command=lambda: edit_field('price', "Enter new product price", int), bg="#2196F3", fg="white").grid(row=1, column=1, padx=10)
tk.Button(frame, text="Edit", command=lambda: edit_field('quantity', "Enter new product quantity", int), bg="#2196F3", fg="white").grid(row=2, column=1, padx=10)
tk.Button(frame, text="Edit", command=lambda: edit_field('description', "Enter new product description"), bg="#2196F3", fg="white").grid(row=3, column=1, padx=10)

master.mainloop()
