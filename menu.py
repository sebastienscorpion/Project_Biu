import tkinter as tk
from tkinter import messagebox
from add_student import add_student_frame  # Importer la fonction pour ajouter un étudiant
from view_students import view_students_frame
from delete_student import delete_student_frame
from edit_student import edit_student_frame
from add_course import add_course_frame  # Importer la fonction pour ajouter un cours
from view_courses import view_courses_frame  # Importer la fonction pour afficher les cours
from delete_course import delete_course_frame  # Importer la fonction pour supprimer un cours
from edit_course import edit_course_frame  # Importer la fonction pour modifier un cours
from add_grade import add_grade_frame  # Importer la fonction pour ajouter une note
from view_grades import view_grades_frame  # Importer la fonction pour afficher les notes
from delete_grade import delete_grade_frame  # Importer la fonction pour supprimer une note
from edit_grade import edit_grade_frame  # Importer la fonction pour modifier une note

def create_menu(app):
    # Création de la barre de menu
    menu_bar = tk.Menu(app)

    # Menu Accueil
    home_menu = tk.Menu(menu_bar, tearoff=0)
    home_menu.add_command(label="Accueil", command=lambda: show_home_page(app))
    menu_bar.add_cascade(label="Accueil", menu=home_menu)

    # Menu Gestion des Étudiants
    student_menu = tk.Menu(menu_bar, tearoff=0)
    student_menu.add_command(label="Ajouter Étudiant", command=lambda: add_student_frame())
    student_menu.add_command(label="Modifier Étudiant", command=lambda: show_edit_student_page(app))
    student_menu.add_command(label="Supprimer Étudiant", command=lambda: show_delete_student_page(app))
    student_menu.add_command(label="Afficher la Liste des Étudiants", command=lambda: show_student_list_page(app))
    menu_bar.add_cascade(label="Gestion des Étudiants", menu=student_menu)

    # Menu Gestion des Cours
    course_menu = tk.Menu(menu_bar, tearoff=0)
    course_menu.add_command(label="Ajouter Cours", command=lambda: add_course_frame())
    course_menu.add_command(label="Modifier Cours", command=lambda: show_edit_course_page(app))
    course_menu.add_command(label="Supprimer Cours", command=lambda: show_delete_course_page(app))
    course_menu.add_command(label="Afficher la Liste des Cours", command=lambda: show_course_list_page(app))
    menu_bar.add_cascade(label="Gestion des Cours", menu=course_menu)

    # Menu Gestion des Notes
    grade_menu = tk.Menu(menu_bar, tearoff=0)
    grade_menu.add_command(label="Ajouter Note", command=lambda: add_grade_frame())
    grade_menu.add_command(label="Modifier Note", command=lambda: show_edit_grade_page(app))
    grade_menu.add_command(label="Supprimer Note", command=lambda: show_delete_grade_page(app))
    grade_menu.add_command(label="Afficher les Notes", command=lambda: show_grades_list_page(app))
    menu_bar.add_cascade(label="Gestion des Notes", menu=grade_menu)

    # Menu Gestion des Administrateurs
    admin_menu = tk.Menu(menu_bar, tearoff=0)
    admin_menu.add_command(label="Ajouter Administrateur", command=lambda: show_add_admin_page(app))
    admin_menu.add_command(label="Modifier Administrateur", command=lambda: show_edit_admin_page(app))
    admin_menu.add_command(label="Supprimer Administrateur", command=lambda: show_delete_admin_page(app))
    menu_bar.add_cascade(label="Gestion des Administrateurs", menu=admin_menu)

    # Menu Rapports
    report_menu = tk.Menu(menu_bar, tearoff=0)
    report_menu.add_command(label="Générer Rapport des Étudiants", command=lambda: generate_student_report(app))
    report_menu.add_command(label="Générer Rapport des Administrateurs", command=lambda: generate_admin_report(app))
    menu_bar.add_cascade(label="Rapports", menu=report_menu)

    # Menu Paramètres
    settings_menu = tk.Menu(menu_bar, tearoff=0)
    settings_menu.add_command(label="Modifier Profil", command=lambda: show_edit_profile_page(app))
    settings_menu.add_command(label="Changer Mot de Passe", command=lambda: show_change_password_page(app))
    menu_bar.add_cascade(label="Paramètres", menu=settings_menu)

    # Menu Aide
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="Documentation", command=open_documentation)
    help_menu.add_command(label="Support", command=show_support_info)
    help_menu.add_command(label="À Propos", command=show_about_info)
    menu_bar.add_cascade(label="Aide", menu=help_menu)

    app.config(menu=menu_bar)

def clear_frame(app):
    for widget in app.winfo_children():
        widget.destroy()

def show_home_page(app):
    clear_frame(app)
    tk.Label(app, text="Bienvenue sur la page d'accueil", font=("Helvetica", 18)).pack(pady=20)

# Pages de gestion des étudiants
def show_add_student_page(app):
    add_student_frame()

def show_edit_student_page(app):
    edit_student_frame()

def show_delete_student_page(app):
    delete_student_frame()

def show_student_list_page(app):
    view_students_frame()

# Pages de gestion des cours
def show_add_course_page(app):
    add_course_frame()

def show_edit_course_page(app):
    edit_course_frame()

def show_delete_course_page(app):
    delete_course_frame()

def show_course_list_page(app):
    view_courses_frame()

# Pages de gestion des notes
def show_add_grade_page(app):
    add_grade_frame()

def show_edit_grade_page(app):
    edit_grade_frame()

def show_delete_grade_page(app):
    delete_grade_frame()

def show_grades_list_page(app):
    view_grades_frame()

# Pages de gestion des administrateurs
def show_add_admin_page(app):
    clear_frame(app)
    tk.Label(app, text="Ajouter un Administrateur", font=("Helvetica", 18)).pack(pady=20)

def show_edit_admin_page(app):
    clear_frame(app)
    tk.Label(app, text="Modifier un Administrateur", font=("Helvetica", 18)).pack(pady=20)

def show_delete_admin_page(app):
    clear_frame(app)
    tk.Label(app, text="Supprimer un Administrateur", font=("Helvetica", 18)).pack(pady=20)

def generate_student_report(app):
    messagebox.showinfo("Générer Rapport", "Rapport des Étudiants généré avec succès.")

def generate_admin_report(app):
    messagebox.showinfo("Générer Rapport", "Rapport des Administrateurs généré avec succès.")

def show_edit_profile_page(app):
    clear_frame(app)
    tk.Label(app, text="Modifier Profil", font=("Helvetica", 18)).pack(pady=20)

def show_change_password_page(app):
    clear_frame(app)
    tk.Label(app, text="Changer Mot de Passe", font=("Helvetica", 18)).pack(pady=20)

def open_documentation():
    messagebox.showinfo("Documentation", "Ouvrir la documentation de l'application.")

def show_support_info():
    messagebox.showinfo("Support", "Contactez-nous à support@example.com.")

def show_about_info():
    messagebox.showinfo("À Propos", "Système de Gestion Étudiante v1.0\nDéveloppé par [Votre Nom]")