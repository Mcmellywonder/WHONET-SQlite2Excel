# gui.py

import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from converter import convert_sqlite_to_excel

def run_gui():
    ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

    app = ctk.CTk()
    app.title("WHONET SQLite to Excel Converter")
    app.geometry("500x300")

    file_path = ctk.StringVar()

    def upload_file():
        path = filedialog.askopenfilename(filetypes=[("SQLite files", "*.sqlite *.db")])
        file_path.set(path)

    def convert_file():
        path = file_path.get()
        if not path:
            messagebox.showerror("Error", "Please upload a .SQLite file first.")
            return
        output_folder = os.path.join(os.getcwd(), "output")
        os.makedirs(output_folder, exist_ok=True)
        convert_sqlite_to_excel(path, output_folder)
        messagebox.showinfo("Success", f"Files saved to {output_folder}")

    # UI Elements
    ctk.CTkLabel(app, text="Upload WHONET .SQLite File", font=("Arial", 16)).pack(pady=10)
    ctk.CTkEntry(app, textvariable=file_path, width=400).pack(pady=5)
    ctk.CTkButton(app, text="Browse", command=upload_file).pack(pady=5)
    ctk.CTkButton(app, text="Convert to Excel", command=convert_file).pack(pady=20)

    app.mainloop()
