import tkinter as tk
from tkinter import ttk
from db import view_students  # Assurez-vous que cette fonction existe

def view_students_frame():
    app = tk.Toplevel()  # Ouvrir une nouvelle fenêtre
    app.title("Liste des Étudiants")
    app.geometry("600x400")  # Taille de la fenêtre

    # Titre de la fenêtre
    tk.Label(app, text="Liste des Étudiants", font=("Helvetica", 18)).pack(pady=20)

    # Création d'un tableau pour afficher les étudiants
    columns = ("ID", "Nom", "Âge", "Numéro d'inscription", "Cours")
    tree = ttk.Treeview(app, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)

    tree.pack(expand=True, fill='both')

    # Récupération des étudiants depuis la base de données
    students = view_students()  # Cette fonction doit renvoyer une liste de tuples (id, nom, âge, numéro, cours)

    # Remplissage du tableau avec les données des étudiants
    for student in students:
        tree.insert("", "end", values=student)

    app.mainloop()  # Démarrer la boucle principale de la nouvelle fenêtre