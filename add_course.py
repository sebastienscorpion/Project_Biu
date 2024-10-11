import tkinter as tk
from tkinter import messagebox
from db import add_course

def add_course_frame():
    app = tk.Toplevel()
    app.title("Ajouter un Cours")
    app.geometry("300x200")

    tk.Label(app, text="Nom du Cours").pack(pady=10)
    entry_course_name = tk.Entry(app)
    entry_course_name.pack(pady=10)

    def submit():
        course_name = entry_course_name.get()
        add_course(course_name)
        messagebox.showinfo("Succès", "Cours ajouté avec succès.")
        app.destroy()

    tk.Button(app, text="Ajouter Cours", command=submit).pack(pady=20)

    app.mainloop()