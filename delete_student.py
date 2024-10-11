import tkinter as tk
from tkinter import messagebox, ttk
from db import delete_student, view_students

def delete_student_frame():
    app = tk.Toplevel()
    app.title("Supprimer un Étudiant")
    app.geometry("600x400")

    tk.Label(app, text="Supprimer un Étudiant", font=("Helvetica", 18)).pack(pady=20)

    tree = ttk.Treeview(app, columns=("ID", "Nom", "Âge", "Numéro d'inscription", "Cours"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nom", text="Nom")
    tree.heading("Âge", text="Âge")
    tree.heading("Numéro d'inscription", text="Numéro d'inscription")
    tree.heading("Cours", text="Cours")
    tree.pack(expand=True, fill='both')

    students = view_students()

    for student in students:
        tree.insert("", "end", values=student)

    def remove_student():
        selected_item = tree.selection()
        if selected_item:
            student_data = tree.item(selected_item)["values"]
            enrollment_number = student_data[3]

            try:
                delete_student(enrollment_number)
                messagebox.showinfo("Succès", "Étudiant supprimé avec succès.")
                tree.delete(selected_item)
            except Exception as e:
                messagebox.showerror("Erreur", str(e))
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un étudiant à supprimer.")

    tk.Button(app, text="Supprimer Étudiant", command=remove_student).pack(pady=20)

    app.mainloop()  # Démarrer la boucle principale de la nouvelle fenêtre