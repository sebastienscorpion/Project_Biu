import tkinter as tk
from tkinter import messagebox
from db import delete_grade  # Assurez-vous d'importer votre fonction pour supprimer une note

def delete_grade_frame():
    app = tk.Toplevel()
    app.title("Supprimer une Note")
    app.geometry("400x200")

    tk.Label(app, text="Supprimer une Note", font=("Helvetica", 18)).pack(pady=20)

    tk.Label(app, text="ID de la Note à Supprimer :").pack(pady=5)
    grade_id_entry = tk.Entry(app)
    grade_id_entry.pack(pady=5)

    def submit_delete():
        grade_id = grade_id_entry.get()
        if grade_id:
            try:
                delete_grade(int(grade_id))  # Assurez-vous que delete_grade accepte un ID comme argument
                messagebox.showinfo("Succès", "Note supprimée avec succès.")
                app.destroy()  # Fermer la fenêtre après la suppression
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer un ID valide.")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    tk.Button(app, text="Supprimer Note", command=submit_delete).pack(pady=20)

    app.mainloop()