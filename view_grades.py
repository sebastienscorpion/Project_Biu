import tkinter as tk
from tkinter import ttk, messagebox
from db import get_student_grades  # Assurez-vous d'importer votre fonction pour récupérer les notes

def view_grades_frame():
    app = tk.Toplevel()
    app.title("Afficher les Notes")
    app.geometry("400x300")

    tk.Label(app, text="Afficher les Notes", font=("Helvetica", 18)).pack(pady=20)

    tk.Label(app, text="Numéro d'Inscription de l'Étudiant :").pack(pady=5)
    enrollment_number_entry = tk.Entry(app)
    enrollment_number_entry.pack(pady=5)

    def display_grades():
        enrollment_number = enrollment_number_entry.get()
        if enrollment_number:
            grades = get_student_grades(enrollment_number)
            if grades:
                report = "\n".join(f"Course: {course_name}, Note: {grade}" for course_name, grade in grades)
                messagebox.showinfo("Rapport de Notes", report)
            else:
                messagebox.showinfo("Rapport de Notes", "Aucune note trouvée pour cet étudiant.")
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un numéro d'inscription.")

    tk.Button(app, text="Afficher Notes", command=display_grades).pack(pady=20)

    app.mainloop()