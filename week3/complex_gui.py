"""
This module provides a complex GUI for the application, allowing users to interact with the system in a more intuitive way.
This module will also use tkinter bootstrap for a more modern look and feel.

This module includes:
- A main window with a title and a menu bar.
- A menu bar with options for file operations, editing, and help.
- Entry and label widgets for user input name, age, and city
- Buttons for submitting the form and clearing the input fields.
- A tab with a scrolled text area for displaying submitted data
"""

import tkinter as tk
from tkinter import messagebox, ttk, simpledialog, font as tkfont, scrolledtext
from tkinter.filedialog import askopenfilename
from ttkbootstrap import Style as BootstrapStyle

class ComplexGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Complex GUI Application")
        self.style = BootstrapStyle(theme='flatly')

        # Create a menu bar
        self.create_menu()

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create input fields
        self.create_input_fields()

        # Create buttons
        self.create_buttons()

        # Create tabbed interface for displaying data
        self.create_tabs()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    def create_input_fields(self):
        ttk.Label(self.main_frame, text="Name:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(self.main_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.main_frame, text="Age:").grid(row=1, column=0, sticky=tk.W)
        self.age_entry = ttk.Entry(self.main_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.main_frame, text="City:").grid(row=2, column=0, sticky=tk.W)
        self.city_entry = ttk.Entry(self.main_frame)
        self.city_entry.grid(row=2, column=1, padx=5, pady=5)

    def create_buttons(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.submit_button = ttk.Button(button_frame, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=0, column=0, padx=5)
        
        self.clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=0, column=1, padx=5)
        
        self.quit_button = ttk.Button(button_frame, text="Quit", command=self.root.quit)
        self.quit_button.grid(row=0, column=2, padx=5)

        
    def create_tabs(self):
        self.tab_control = ttk.Notebook(self.main_frame)
        self.data_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.data_tab, text='Submitted Data')
        
        # Use grid instead of pack
        self.tab_control.grid(row=4, column=0, columnspan=2, sticky='nsew')

        self.data_display = scrolledtext.ScrolledText(self.data_tab, wrap=tk.WORD, width=50, height=10)
        self.data_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        # self.data_display.config(state='disabled')  # Make it read-only initially

        
    def submit_data(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        city = self.city_entry.get()

        if not name or not age or not city:
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return

        data = f"Name: {name}, Age: {age}, City: {city}\n"
        self.data_display.insert(tk.END, data)
        self.clear_fields()
        
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        
    def new_file(self):
        if messagebox.askyesno("New File", "Do you want to create a new file?"):
            self.clear_fields()
            self.data_display.delete(1.0, tk.END)

    def open_file(self):
        file_path = askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                data = file.read()
                self.data_display.delete(1.0, tk.END)
                self.data_display.insert(tk.END, data)
    
    def show_about(self):
        messagebox.showinfo("About", "Complex GUI Application\nVersion 1.0\nCreated with Tkinter and ttkbootstrap")

if __name__ == "__main__":
    root = tk.Tk()
    app = ComplexGUI(root)
    root.mainloop()
