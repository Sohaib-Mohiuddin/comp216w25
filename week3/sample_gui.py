import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Tkinter App")
root.geometry("300x150")  # Set window size (width x height)

# Add a label
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)  # Add some padding

# Add a button to close the window
close_button = tk.Button(root, text="Close", command=root.destroy)
close_button.pack(pady=10)

# Run the application
root.mainloop()
