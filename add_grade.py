import tkinter as tk
from tkinter import messagebox
from db import add_grade  # Assurez-vous d'importer votre fonction pour ajouter une note

def add_grade_frame():
    app = tk.Toplevel()
    app.title("Ajouter une Note")
    app.geometry("400x300")

    tk.Label(app, text="Ajouter une Note", font=("Helvetica", 18)).pack(pady=20)

    tk.Label(app, text="Numéro d'Inscription de l'Étudiant :").pack(pady=5)
    enrollment_number_entry = tk.Entry(app)
    enrollment_number_entry.pack(pady=5)

    tk.Label(app, text="Nom du Cours :").pack(pady=5)
    course_name_entry = tk.Entry(app)
    course_name_entry.pack(pady=5)

    tk.Label(app, text="Note :").pack(pady=5)
    grade_entry = tk.Entry(app)
    grade_entry.pack(pady=5)

    def submit_grade():
        enrollment_number = enrollment_number_entry.get()
        course_name = course_name_entry.get()
        grade = grade_entry.get()

        if enrollment_number and course_name and grade:
            try:
                add_grade(enrollment_number, course_name, float(grade))
                messagebox.showinfo("Succès", "Note ajoutée avec succès.")
                app.destroy()  # Fermer la fenêtre après l'ajout
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    tk.Button(app, text="Ajouter Note", command=submit_grade).pack(pady=20)

    app.mainloop()