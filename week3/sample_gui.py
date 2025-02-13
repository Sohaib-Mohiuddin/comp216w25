import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("User Input Form")
root.geometry("400x250")

# Define a function to handle the button click and show an alert with user input
def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    city = city_entry.get()
    
    if name and age and city:
        messagebox.showinfo("Form Submitted", f"Hello, {name}!\nAge: {age}\nCity: {city}")
    else:
        messagebox.showwarning("Incomplete Form", "Please fill out all fields.")

# Create labels and entry widgets for Name, Age, and City
tk.Label(root, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(root, width=30)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="City:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
city_entry = tk.Entry(root, width=30)
city_entry.grid(row=2, column=1, padx=10, pady=10)

# Add a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=1, pady=20)

# Run the application
root.mainloop()
