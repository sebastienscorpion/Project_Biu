import tkinter as tk
from tkinter import messagebox, ttk
from db import update_student, view_students, view_courses

def edit_student_frame():
    app = tk.Toplevel()
    app.title("Modifier un Étudiant")
    app.geometry("600x400")

    tk.Label(app, text="Modifier un Étudiant", font=("Helvetica", 18)).pack(pady=20)

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

    tk.Label(app, text="Nom").pack(pady=5)
    entry_name = tk.Entry(app)
    entry_name.pack(pady=5)

    tk.Label(app, text="Âge").pack(pady=5)
    entry_age = tk.Entry(app)
    entry_age.pack(pady=5)

    tk.Label(app, text="Sélectionner un Cours").pack(pady=5)

    course_combobox = ttk.Combobox(app)
    courses = view_courses()
    course_combobox['values'] = [course[1] for course in courses]
    course_combobox.pack(pady=5)

    def load_student_info(event):
        selected_item = tree.selection()
        if selected_item:
            student_data = tree.item(selected_item)["values"]
            entry_name.delete(0, tk.END)
            entry_age.delete(0, tk.END)
            entry_name.insert(0, student_data[1])
            entry_age.insert(0, student_data[2])
            course_combobox.set(next(course[1] for course in courses if course[0] == student_data[4]))

    tree.bind('<<TreeviewSelect>>', load_student_info)

    def update_student_info():
        selected_item = tree.selection()
        if selected_item:
            student_data = tree.item(selected_item)["values"]
            enrollment_number = student_data[3]
            name = entry_name.get()
            age = entry_age.get()
            course_name = course_combobox.get()

            # Validation des champs
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

            # Mettre à jour les informations de l'étudiant
            try:
                update_student(enrollment_number, name, age, course_id)
                messagebox.showinfo("Succès", "Informations de l'étudiant mises à jour avec succès.")
                tree.item(selected_item, values=(student_data[0], name, age, enrollment_number, course_name))
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

    tk.Button(app, text="Mettre à Jour", command=update_student_info).pack(pady=20)

    app.mainloop()  # Démarrer la boucle principale de la nouvelle fenêtre