import tkinter as tk
from tkinter import messagebox, ttk
from db import delete_course, view_courses  # Assurez-vous que ces fonctions existent dans db.py

def delete_course_frame():
    app = tk.Toplevel()
    app.title("Supprimer un Cours")
    app.geometry("600x400")

    tk.Label(app, text="Supprimer un Cours", font=("Helvetica", 18)).pack(pady=20)

    tree = ttk.Treeview(app, columns=("ID", "Nom du Cours"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nom du Cours", text="Nom du Cours")
    tree.pack(expand=True, fill='both')

    # Charger les cours dans le Treeview
    courses = view_courses()
    for course in courses:
        tree.insert("", "end", values=(course[0], course[1]))

    def remove_course():
        selected_item = tree.selection()
        if selected_item:
            course_data = tree.item(selected_item)["values"]
            course_id = course_data[0]  # Supposons que l'ID est le premier élément

            # Demander une confirmation avant de supprimer
            if messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce cours ?"):
                try:
                    delete_course(course_id)  # Appeler la fonction pour supprimer le cours
                    messagebox.showinfo("Succès", "Cours supprimé avec succès.")
                    tree.delete(selected_item)
                except Exception as e:
                    messagebox.showerror("Erreur", str(e))
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un cours à supprimer.")

    tk.Button(app, text="Supprimer Cours", command=remove_course).pack(pady=20)

    app.mainloop()