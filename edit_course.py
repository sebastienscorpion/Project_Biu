import tkinter as tk
from tkinter import ttk, messagebox
from db import edit_course, view_courses  # Assurez-vous que ces fonctions existent dans db.py


def edit_course_frame():
    app = tk.Toplevel()
    app.title("Modifier un Cours")
    app.geometry("600x400")

    tk.Label(app, text="Modifier un Cours", font=("Helvetica", 18)).pack(pady=20)

    tree = ttk.Treeview(app, columns=("ID", "Nom du Cours"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nom du Cours", text="Nom du Cours")
    tree.pack(expand=True, fill='both')

    # Charger les cours dans le Treeview
    courses = view_courses()  # Récupérer les cours de la base de données
    for course in courses:
        tree.insert("", "end", values=(course[0], course[1]))  # Ajustez les indices selon votre structure de données

    # Champ pour entrer le nouveau nom du cours
    tk.Label(app, text="Nouveau Nom du Cours :").pack(pady=5)
    name_entry = tk.Entry(app)
    name_entry.pack(pady=5)

    def on_select(event):
        selected_item = tree.selection()
        if selected_item:
            course_data = tree.item(selected_item)["values"]
            course_id = course_data[0]  # Supposons que l'ID est le premier élément
            course_name = course_data[1]  # Supposons que le nom est le deuxième élément

            # Mettre à jour le champ de saisie avec le nom du cours sélectionné
            name_entry.delete(0, tk.END)  # Effacer le champ avant de le remplir
            name_entry.insert(0, course_name)  # Insérer le nom du cours

    tree.bind('<<TreeviewSelect>>', on_select)  # Lier l'événement de sélection

    def update_course():
        selected_item = tree.selection()
        if selected_item:
            course_data = tree.item(selected_item)["values"]
            course_id = course_data[0]  # Supposons que l'ID est le premier élément

            new_name = name_entry.get()  # Récupérer le nouveau nom du cours
            if new_name:
                try:
                    edit_course(course_id, new_name)  # Appel de la fonction pour modifier le cours
                    messagebox.showinfo("Succès", "Cours modifié avec succès.")
                    tree.item(selected_item, values=(course_id, new_name))
                except Exception as e:
                    messagebox.showerror("Erreur", str(e))  # Afficher l'erreur si la modification échoue
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un nouveau nom de cours.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un cours à modifier.")

    tk.Button(app, text="Modifier Cours", command=update_course).pack(pady=20)

    app.mainloop()