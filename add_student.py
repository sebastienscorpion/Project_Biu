import tkinter as tk
from tkinter import messagebox, ttk
from db import add_student, view_courses

def add_student_frame():
    app = tk.Toplevel()
    app.title("Ajouter un Étudiant")

    # Pour ouvrir en plein écran
    app.attributes('-fullscreen', True)

    # Pour quitter le mode plein écran avec la touche "Escape"
    def toggle_fullscreen(event=None):
        app.attributes('-fullscreen', not app.attributes('-fullscreen'))

    app.bind('<Escape>', toggle_fullscreen)

    tk.Label(app, text="Nom").pack(pady=5)
    entry_name = tk.Entry(app)
    entry_name.pack(pady=5)

    tk.Label(app, text="Âge").pack(pady=5)
    entry_age = tk.Entry(app)
    entry_age.pack(pady=5)

    tk.Label(app, text="Numéro d'inscription").pack(pady=5)
    entry_enrollment_number = tk.Entry(app)
    entry_enrollment_number.pack(pady=5)

    tk.Label(app, text="Sélectionner un Cours").pack(pady=5)

    course_combobox = ttk.Combobox(app)
    courses = view_courses()
    course_combobox['values'] = [course[1] for course in courses]
    course_combobox.pack(pady=5)

    def submit():
        name = entry_name.get()
        age = entry_age.get()
        enrollment_number = entry_enrollment_number.get()
        course_name = course_combobox.get()

        # Vérifications de validité
        if not name or not age or not enrollment_number or not course_name:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        try:
            age = int(age)  # Conversion de l'âge en entier
        except ValueError:
            messagebox.showerror("Erreur", "L'âge doit être un nombre.")
            return

        # Trouver l'ID du cours sélectionné
        course_id = next((course[0] for course in courses if course[1] == course_name), None)

        add_student(name, age, enrollment_number, course_id)
        messagebox.showinfo("Succès", "Étudiant ajouté avec succès.")
        app.destroy()

    # Ajout du bouton d'insertion
    tk.Button(app, text="Ajouter Étudiant", command=submit).pack(pady=20)

    app.mainloop()