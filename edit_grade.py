import tkinter as tk
from tkinter import messagebox
from db import update_grade  # Assurez-vous d'importer votre fonction pour mettre à jour une note

def edit_grade_frame():
    app = tk.Toplevel()
    app.title("Modifier une Note")
    app.geometry("400x300")

    tk.Label(app, text="Modifier une Note", font=("Helvetica", 18)).pack(pady=20)

    tk.Label(app, text="ID de la Note à Modifier :").pack(pady=5)
    grade_id_entry = tk.Entry(app)
    grade_id_entry.pack(pady=5)

    tk.Label(app, text="Nouvelle Note :").pack(pady=5)
    new_grade_entry = tk.Entry(app)
    new_grade_entry.pack(pady=5)

    def submit_edit():
        grade_id = grade_id_entry.get()
        new_grade = new_grade_entry.get()

        if grade_id and new_grade:
            try:
                update_grade(int(grade_id), float(new_grade))  # Assurez-vous que update_grade prend ces arguments
                messagebox.showinfo("Succès", "Note modifiée avec succès.")
                app.destroy()  # Fermer la fenêtre après la modification
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    tk.Button(app, text="Modifier Note", command=submit_edit).pack(pady=20)

    app.mainloop()