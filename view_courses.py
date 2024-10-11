import tkinter as tk
from tkinter import ttk
from db import view_courses  # Assurez-vous que cette fonction existe dans db.py

def view_courses_frame():
    app = tk.Toplevel()
    app.title("Liste des Cours")
    app.geometry("600x400")

    tk.Label(app, text="Liste des Cours", font=("Helvetica", 18)).pack(pady=20)

    tree = ttk.Treeview(app, columns=("ID", "Nom du Cours"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nom du Cours", text="Nom du Cours")
    tree.pack(expand=True, fill='both')

    courses = view_courses()  # Récupérer les cours de la base de données

    for course in courses:
        tree.insert("", "end", values=(course[0], course[1]))  # Ajustez les indices selon votre structure de données

    app.mainloop()