# def register():
#     username = entry_username.get()
#     password = entry_password.get()
#     register_user(username, password)
#     print("Utilisateur enregistré.")
#
#
# def login():
#     global current_user
#     username = entry_username.get()
#     password = entry_password.get()
#     if login_user(username, password):
#         current_user = username  # Stocker l'utilisateur connecté
#         print("Connexion réussie.")
#         show_student_management_frame()  # Affiche le cadre de gestion des étudiants
#     else:
#         print("Échec de la connexion.")
#
#
# def logout():
#     global current_user
#     current_user = None  # Réinitialiser l'utilisateur connecté
#     print("Déconnexion réussie.")
#     show_login_frame()  # Retourner à l'écran de connexion
#
#
# def show_login_frame():
#     for widget in app.winfo_children():
#         widget.destroy()
#
#     tk.Label(app, text="Nom d'utilisateur", font=("Helvetica", 12)).pack(pady=5)
#     global entry_username
#     entry_username = tk.Entry(app, font=("Helvetica", 12))
#     entry_username.pack(pady=5)
#
#     tk.Label(app, text="Mot de passe", font=("Helvetica", 12)).pack(pady=5)
#     global entry_password
#     entry_password = tk.Entry(app, show='*', font=("Helvetica", 12))
#     entry_password.pack(pady=5)
#
#     tk.Button(app, text="S'inscrire", command=register, bg="#008CBA", fg="white", font=("Helvetica", 12)).pack(pady=10)
#     tk.Button(app, text="Se connecter", command=login, bg="#f44336", fg="white", font=("Helvetica", 12)).pack(pady=5)
#
#
# def show_student_management_frame():
#     for widget in app.winfo_children():
#         widget.destroy()
#
#     form_frame = tk.Frame(app, padx=20, pady=20)
#     form_frame.pack(side=tk.TOP, fill=tk.X)
#
#     # Afficher l'utilisateur connecté
#     user_label = tk.Label(form_frame, text=f"Connecté en tant que: {current_user}", font=("Helvetica", 12))
#     user_label.grid(row=0, column=0, columnspan=2, pady=5)
#
#     # Entrées pour ajouter ou modifier
#     tk.Label(form_frame, text="Nom", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
#     entry_name = tk.Entry(form_frame, font=("Helvetica", 12))
#     entry_name.grid(row=1, column=1, padx=5, pady=5)
#
#     tk.Label(form_frame, text="Âge", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=5)
#     entry_age = tk.Entry(form_frame, font=("Helvetica", 12))
#     entry_age.grid(row=2, column=1, padx=5, pady=5)
#
#     tk.Label(form_frame, text="Numéro d'inscription", font=("Helvetica", 12)).grid(row=3, column=0, padx=5, pady=5)
#     entry_enrollment = tk.Entry(form_frame, font=("Helvetica", 12))
#     entry_enrollment.grid(row=3, column=1, padx=5, pady=5)
#
#     # Boutons pour les opérations CRUD alignés horizontalement
#     button_frame = tk.Frame(form_frame)
#     button_frame.grid(row=4, column=0, columnspan=2, pady=10)
#
#     tk.Button(button_frame, text="Ajouter Étudiant",
#               command=lambda: add_student_to_db(entry_name.get(), entry_age.get(), entry_enrollment.get(), tree),
#               bg="#4CAF50", fg="white", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
#     tk.Button(button_frame, text="Modifier Étudiant",
#               command=lambda: update_student_in_db(entry_enrollment.get(), entry_name.get(), entry_age.get(), tree),
#               bg="#FFC107", fg="white", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
#     tk.Button(button_frame, text="Supprimer Étudiant",
#               command=lambda: delete_student_from_db(entry_enrollment.get(), tree), bg="#f44336", fg="white",
#               font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
#
#     # Bouton de déconnexion
#     tk.Button(form_frame, text="Déconnexion", command=logout, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(
#         row=5, column=0, columnspan=2, pady=5)
#
#     # Cadre pour l'affichage des étudiants
#     display_frame = tk.Frame(app, padx=20, pady=20)
#     display_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
#
#     # Affichage des étudiants
#     tk.Label(display_frame, text="Liste des Étudiants", font=("Helvetica", 14)).pack(pady=10)
#
#     # Créer un Treeview pour afficher les étudiants avec une bordure
#     columns = ("enrollment_number", "name", "age")
#     global tree
#     tree = ttk.Treeview(display_frame, columns=columns, show='headings')
#     tree.heading("enrollment_number", text="Numéro d'inscription")
#     tree.heading("name", text="Nom")
#     tree.heading("age", text="Âge")
#
#     # Ajouter une bordure
#     tree.pack(pady=10, fill=tk.BOTH, expand=True)
#     tree.bind("<ButtonRelease-1>", lambda event: on_tree_select(tree))  # Sélectionner une ligne
#
#     # Style pour ajouter une bordure
#     style = ttk.Style()
#     style.configure("Treeview", bordercolor="black", borderwidth=2)
#
#     # Charger les étudiants dans le Treeview
#     load_students(tree)
#
#     # Recherche
#     tk.Label(form_frame, text="Rechercher un étudiant (Nom ou Numéro)", font=("Helvetica", 12)).grid(row=8, column=0,
#                                                                                                      padx=5, pady=5)
#     entry_search = tk.Entry(form_frame, font=("Helvetica", 12))
#     entry_search.grid(row=8, column=1, padx=5, pady=5)
#     tk.Button(form_frame, text="Rechercher", command=lambda: search_students_in_db(entry_search.get(), tree),
#               bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=9, column=0, columnspan=2, pady=5)
#
#
# def load_students(tree):
#     # Effacer les éléments existants
#     for item in tree.get_children():
#         tree.delete(item)
#     students = view_students()  # Récupérer les étudiants de la base de données
#     for student in students:
#         tree.insert("", tk.END, values=(student[2], student[1], student[3]))  # Format: Numéro d'inscription, Nom, Âge
#
#
# def add_student_to_db(name, age, enrollment_number, tree):
#     add_student(name, age, enrollment_number)
#     load_students(tree)  # Recharge la liste des étudiants
#
#
# def update_student_in_db(enrollment_number, name, age, tree):
#     update_student(enrollment_number, name if name else None, age if age else None)
#     load_students(tree)  # Recharge la liste des étudiants
#
#
# def delete_student_from_db(enrollment_number, tree):
#     delete_student(enrollment_number)
#     load_students(tree)  # Recharge la liste des étudiants
#
#
# def search_students_in_db(search_term, tree):
#     # Effacer les éléments existants
#     for item in tree.get_children():
#         tree.delete(item)
#     results = search_students(search_term)  # Récupérer les résultats de la recherche
#     for student in results:
#         tree.insert("", tk.END, values=(student[2], student[1], student[3]))  # Format: Numéro d'inscription, Nom, Âge
#
#
# def on_tree_select(tree):
#     selected_item = tree.selection()[0]
#     item_values = tree.item(selected_item, 'values')
#     entry_enrollment.delete(0, tk.END)
#     entry_enrollment.insert(0, item_values[0])  # Numéro d'inscription
#     entry_name.delete(0, tk.END)
#     entry_name.insert(0, item_values[1])  # Nom
#     entry_age.delete(0, tk.END)
#     entry_age.insert(0, item_values[2])  # Âge
#
#
# def show_home_page():
#     for widget in app.winfo_children():
#         widget.destroy()
#     tk.Label(app, text="Bienvenue sur la page d'accueil", font=("Helvetica", 18)).pack(pady=20)
#
#
# def show_add_admin_page():
#     for widget in app.winfo_children():
#         widget.destroy()
#     tk.Label(app, text="Ajout des Administrateurs", font=("Helvetica", 18)).pack(pady=20)
#     # Ajoutez ici les éléments pour l'ajout d'administrateurs
#
#
# # Configuration de la fenêtre principale
# app = tk.Tk()
# app.title("Système de Gestion Étudiante")
# app.geometry("600x700")  # Taille de la fenêtre
#
# # Création de la barre de menu
# menu_bar = tk.Menu(app)
#
# # Menu Accueil
# home_menu = tk.Menu(menu_bar, tearoff=0)
# home_menu.add_command(label="Accueil", command=show_home_page)
# home_menu.add_command(label="Ajouter Administrateur", command=show_add_admin_page)
# menu_bar.add_cascade(label="Menu", menu=home_menu)
#
# app.config(menu=menu_bar)
#
# # Initialiser les entrées dans le cadre de connexion
# entry_username = None
# entry_password = None
#
# show_login_frame()  # Afficher le cadre de connexion au démarrage
#
# app.mainloop()  # Dé


















# la partie add_student
#
# # add_student.py
# import tkinter as tk
# from tkinter import messagebox
# from db import add_student  # Assurez-vous que la fonction add_student est correctement importée
#
# def add_student_frame():
#     # Création de la fenêtre principale
#     app = tk.Toplevel()  # Utilisez Toplevel pour créer une nouvelle fenêtre
#     app.title("Ajouter Étudiant")
#     app.geometry("400x300")  # Taille de la fenêtre
#
#     # Fonction pour ajouter un étudiant
#     def submit_student():
#         name = entry_name.get()
#         age = entry_age.get()
#         enrollment_number = entry_enrollment.get()
#
#         if name and age and enrollment_number:
#             add_student(name, age, enrollment_number)  # Appel à la fonction d'ajout dans la base de données
#             messagebox.showinfo("Succès", "Étudiant ajouté avec succès.")
#             entry_name.delete(0, tk.END)  # Effacer le champ
#             entry_age.delete(0, tk.END)  # Effacer le champ
#             entry_enrollment.delete(0, tk.END)  # Effacer le champ
#         else:
#             messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
#
#     # Champ pour le nom
#     tk.Label(app, text="Nom", font=("Helvetica", 12)).pack(pady=10)
#     entry_name = tk.Entry(app, font=("Helvetica", 12))
#     entry_name.pack(pady=5)
#
#     # Champ pour l'âge
#     tk.Label(app, text="Âge", font=("Helvetica", 12)).pack(pady=10)
#     entry_age = tk.Entry(app, font=("Helvetica", 12))
#     entry_age.pack(pady=5)
#
#     # Champ pour le numéro d'inscription
#     tk.Label(app, text="Numéro d'inscription", font=("Helvetica", 12)).pack(pady=10)
#     entry_enrollment = tk.Entry(app, font=("Helvetica", 12))
#     entry_enrollment.pack(pady=5)
#
#     # Bouton pour soumettre l'ajout de l'étudiant
#     tk.Button(app, text="Ajouter Étudiant", command=submit_student, font=("Helvetica", 12)).pack(pady=20)
#
#     app.mainloop()  # Démarrer la boucle principale de la nouvelle fenêtre






# la partie de edit_student
#
# import tkinter as tk
# from tkinter import messagebox, ttk
# from db import update_student, view_students  # Assurez-vous que ces fonctions existent
#
# def edit_student_frame():
#     app = tk.Toplevel()  # Ouvrir une nouvelle fenêtre
#     app.title("Modifier un Étudiant")
#     app.geometry("800x700")  # Taille de la fenêtre
#
#     # Titre de la fenêtre
#     tk.Label(app, text="Modifier un Étudiant", font=("Helvetica", 18)).pack(pady=20)
#
#     # Création d'un tableau pour afficher les étudiants
#     tree = ttk.Treeview(app, columns=("ID", "Nom", "Âge", "Numéro d'inscription"), show='headings')
#     tree.heading("ID", text="ID")
#     tree.heading("Nom", text="Nom")
#     tree.heading("Âge", text="Âge")
#     tree.heading("Numéro d'inscription", text="Numéro d'inscription")
#     tree.pack(expand=True, fill='both')
#
#     # Récupération des étudiants depuis la base de données
#     students = view_students()  # Cette fonction doit renvoyer une liste de tuples (id, nom, âge, numéro)
#
#     # Remplissage du tableau avec les données des étudiants
#     for student in students:
#         tree.insert("", "end", values=student)
#
#     # Champs de saisie pour la modification
#     tk.Label(app, text="Nom").pack(pady=5)
#     entry_name = tk.Entry(app)
#     entry_name.pack(pady=5)
#
#     tk.Label(app, text="Âge").pack(pady=5)
#     entry_age = tk.Entry(app)
#     entry_age.pack(pady=5)
#
#     # Fonction pour charger les informations de l'étudiant sélectionné
#     def load_student_info(event):
#         selected_item = tree.selection()  # Obtenir l'élément sélectionné
#         if selected_item:
#             student_data = tree.item(selected_item)["values"]
#             entry_name.delete(0, tk.END)
#             entry_age.delete(0, tk.END)
#             entry_name.insert(0, student_data[1])  # Nom
#             entry_age.insert(0, student_data[2])    # Âge
#         else:
#             messagebox.showerror("Erreur", "Veuillez sélectionner un étudiant à modifier.")
#
#     # Lier l'événement de sélection à la fonction
#     tree.bind('<<TreeviewSelect>>', load_student_info)
#
#     # Fonction pour mettre à jour les informations de l'étudiant
#     def update_student_info():
#         selected_item = tree.selection()
#         if selected_item:
#             student_data = tree.item(selected_item)["values"]
#             enrollment_number = student_data[3]  # Numéro d'inscription
#             name = entry_name.get()
#             age = entry_age.get()
#
#             if name and age:
#                 update_student(enrollment_number, name, age)  # Appel à la fonction de mise à jour
#                 messagebox.showinfo("Succès", "Informations de l'étudiant mises à jour avec succès.")
#                 tree.item(selected_item, values=(student_data[0], name, age, enrollment_number))  # Mettre à jour l'affichage
#             else:
#                 messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
#         else:
#             messagebox.showerror("Erreur", "Veuillez sélectionner un étudiant à modifier.")
#
#     # Bouton pour mettre à jour l'étudiant sélectionné
#     tk.Button(app, text="Mettre à Jour", command=update_student_info).pack(pady=20)
#
#     app.mainloop()  # Démarrer la boucle principale de la nouvelle fenêtre


# import tkinter as tk
# from tkinter import messagebox, ttk
# from db import delete_student, view_students  # Assurez-vous que ces fonctions existent
#
# def delete_student_frame():
#     app = tk.Toplevel()  # Ouvrir une nouvelle fenêtre
#     app.title("Supprimer un Étudiant")
#     app.geometry("800x700")  # Taille de la fenêtre
#
#     # Titre de la fenêtre
#     tk.Label(app, text="Supprimer un Étudiant", font=("Helvetica", 18)).pack(pady=20)
#
#     # Création d'un tableau pour afficher les étudiants
#     tree = ttk.Treeview(app, columns=("ID", "Nom", "Âge", "Numéro d'inscription"), show='headings')
#     tree.heading("ID", text="ID")
#     tree.heading("Nom", text="Nom")
#     tree.heading("Âge", text="Âge")
#     tree.heading("Numéro d'inscription", text="Numéro d'inscription")
#     tree.pack(expand=True, fill='both')
#
#     # Récupération des étudiants depuis la base de données
#     students = view_students()  # Cette fonction doit renvoyer une liste de tuples (id, nom, âge, numéro)
#
#     # Remplissage du tableau avec les données des étudiants
#     for student in students:
#         tree.insert("", "end", values=student)
#
#     # Fonction pour supprimer l'étudiant sélectionné
#     def remove_student():
#         selected_item = tree.selection()  # Obtenir l'élément sélectionné
#         if selected_item:
#             student_data = tree.item(selected_item)["values"]
#             enrollment_number = student_data[3]  # Numéro d'inscription
#             delete_student(enrollment_number)  # Appel à la fonction de suppression
#             messagebox.showinfo("Succès", "Étudiant supprimé avec succès.")
#             tree.delete(selected_item)  # Supprimer l'élément de l'affichage
#         else:
#             messagebox.showerror("Erreur", "Veuillez sélectionner un étudiant à supprimer.")
#
#     # Bouton pour supprimer l'étudiant sélectionné
#     tk.Button(app, text="Supprimer Étudiant", command=remove_student).pack(pady=20)
#
#     app.mainloop()  # Démarrer la boucle principale de la nouvelle fenêtre