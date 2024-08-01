import tkinter as tk
from tkinter import messagebox
import string
import random

class Window:

    MAX_CHARS = 15
    MIN_CHARS = 3
    CHARS_OPTIONS = ["Alphanumeric", "Numeric", "Alpha"]
    GRID_PADY = (10, 10)

    def __init__(self):
        self.initUI()

    def initUI(self):
        self.master = tk.Tk()
        self.master.title("Password Generator")
        self.master.geometry("600x300")
        self.master.resizable(False, False)

        self.ptype = tk.StringVar(self.master, value=Window.CHARS_OPTIONS[0])
        self.n_chars = tk.IntVar(self.master, value=Window.MIN_CHARS)

        # Character type selection
        self.label_chars = tk.Label(self.master, text="Select Character Type: ")
        self.option_menu_chars = tk.OptionMenu(self.master, self.ptype, *Window.CHARS_OPTIONS)
        self.option_menu_chars.config(width=15)

        # Password length selection
        self.label_num_chars = tk.Label(self.master, text="Select Password Length: ")
        self.option_menu_n_chars = tk.OptionMenu(self.master, self.n_chars, *range(Window.MIN_CHARS, Window.MAX_CHARS + 1))
        self.option_menu_n_chars.config(width=5)

        # Generated password display
        self.label_password_out = tk.Label(self.master, text="Generated Password:")
        self.text_password_out = tk.Entry(self.master, border=2, width=30, font=('Arial', 14))

        # Buttons
        self.button_generate = tk.Button(self.master, text="Generate", width=10, command=self.set_password)
        self.button_copy = tk.Button(self.master, text="Copy", width=10, command=self.copy_to_clipboard)
        self.button_close = tk.Button(self.master, text="Close", command=self.master.quit, width=10)

        # Layout
        self.label_chars.grid(row=0, column=0, pady=Window.GRID_PADY, padx=10, sticky='e')
        self.option_menu_chars.grid(row=0, column=1, pady=Window.GRID_PADY, padx=10, sticky='w')
        self.label_num_chars.grid(row=1, column=0, pady=Window.GRID_PADY, padx=10, sticky='e')
        self.option_menu_n_chars.grid(row=1, column=1, pady=Window.GRID_PADY, padx=10, sticky='w')
        self.label_password_out.grid(row=2, column=0, pady=Window.GRID_PADY, padx=10, sticky='e')
        self.text_password_out.grid(row=2, column=1, pady=Window.GRID_PADY, padx=10, sticky='w')

        self.button_generate.grid(row=3, column=0, pady=Window.GRID_PADY, padx=10)
        self.button_copy.grid(row=3, column=1, pady=Window.GRID_PADY, padx=10, sticky='w')
        self.button_close.grid(row=4, column=1, pady=Window.GRID_PADY, padx=10, sticky='e')

        self.text_password_out.focus()

        self.master.mainloop()

    def set_password(self):
        ptype = self.ptype.get().lower()
        if ptype == "numeric":
            chars = string.digits
        elif ptype == "alpha":
            chars = string.ascii_letters
        else:
            chars = string.digits + string.ascii_letters

        password = "".join(random.choices(chars, k=self.n_chars.get()))

        self.text_password_out.delete(0, tk.END)
        self.text_password_out.insert(0, password)

    def copy_to_clipboard(self):
        password = self.text_password_out.get()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("No Password", "Please generate a password first!")

if __name__ == "__main__":
    Window()
