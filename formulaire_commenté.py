"""
    Module docstring
"""
# Importation des bibliothèques
import datetime
from tkinter import *
from tkinter import messagebox
import pandas as pd

def write_line_in_csv(first_name,name, date, poste) :

    """
    Cette fonction ajoute une nouvelle ligne au fichier CSV contenant la liste des employés.
    La nouvelle ligne est créée à partir des informations fournies en entrée : nom, prénom, date d'embauche et poste.

    Parameters:
    ----------
        :first_name : str
            Le prénom de l'employé.
        :name : str
            Le nom de l'employé.
        :date : str
            La date d'embauche de l'employé, au format "YYYY-MM-DD".
        :poste : str
            Le poste occupé par l'employé.

    Returns:
    -------
        None
            Cette fonction ne retourne rien, mais modifie le fichier CSV "liste_employes.csv" en ajoutant une nouvelle ligne.

    Examples:
    --------
        >>> write_line_in_csv('Alice', 'Dupont', '2022-01-01', 'Ingénieur')
        # Le fichier CSV "liste_employes.csv" est modifié et contient maintenant une nouvelle ligne avec les informations sur l'employé Alice Dupont.
    """

    # Chargement de la liste des employés depuis le fichier CSV
    list_employes = pd.read_csv("liste_employes.csv")
    # Création d'une nouvelle ligne avec les données du nouvel employé
    df_new_line =  pd.DataFrame([[first_name,name,date,poste]],columns=[ 'Nom','Prenom', 'Date','Poste'] )
    # Concaténation de la nouvelle ligne à la liste des employés
    list_employes = pd.concat([list_employes,df_new_line], ignore_index=True)
    # Écriture de la liste mise à jour dans le fichier CSV
    list_employes.to_csv('liste_employes.csv', index = False)


def check_form(first_name, name, poste) :

    
    
    """
    Cette fonction vérifie si les champs "Prénom" et "Nom" du formulaire d'ajout d'un employé sont remplis, et affiche un message d'erreur le cas échéant.
    Si les champs sont remplis, elle ajoute le nouvel employé à la liste des employés et affiche un message de validation.

    Parameters:
    ----------
        :first_name : str
            Le prénom de l'employé.
        :name : str
            Le nom de l'employé.
        :poste : str
            Le poste occupé par l'employé.

    Returns:
    -------
        None
            Cette fonction ne retourne rien, mais affiche des messages d'erreur ou de validation et modifie le fichier CSV "liste_employes.csv" si nécessaire.

    Examples:
    --------
        >>> check_form('Alice', '', 'Ingénieur')
        # Un message d'erreur est affiché indiquant que le nom est manquant.
        >>> check_form('', 'Dupont', 'Ingénieur')
        # Un message d'erreur est affiché indiquant que le prénom est manquant.
        >>> check_form('Alice', 'Dupont', 'Ingénieur')
        # Le nouvel employé Alice Dupont est ajouté à la liste des employés et un message de validation est affiché.
      
        """

    # Initialisation du flag indiquant s'il y a une erreur
    badValue = True
    error_message = 'erreur'
    # Vérification que les champs "Prénom" et "Nom" ne sont pas vides
    if len(first_name.strip()) == 0: 
        error_message = 'Prénom manquant'
        if len(name.strip()) == 0:
            error_message = 'Prénom et nom manquants'
    elif len(name.strip()) == 0 :
        error_message = 'Nom manquant'
    else :
        # Si aucun champ n'est vide, on met à jour le flag
        badValue = False
    
    if badValue :
        # Affichage de l'erreur
        messagebox.showerror("Erreur", error_message)
        pass
    else :
        # Récupération de la date du jour
        x = datetime.datetime.now()
        today = "{}/{}/{}".format( x.day, x.month, x.year)        
        # Ajout du nouvel employé à la liste des employés
        write_line_in_csv( first_name.capitalize(), name.capitalize(), today, poste)
        # Affichage d'un message de validation
        messagebox.showinfo("Traitement du formulaire", "Employé ajouté !")
        pass



if __name__ == "__main__":
    # Nom, Prénom, Date embauche, Poste
    df = pd.read_csv(r'liste_employes.csv')


    # Chargement de la liste des employés depuis le fichier CSV
    list_employes = pd.read_csv("liste_employes.csv")
    # Création de la fenêtre principale
    window = Tk()
    # Configuration de la fenêtre
    window.title("Gestion des employés")
    window.geometry("480x360" )
    window.maxsize(800, 600)
    window.config(background='#2f5df3')
    # Ajout d'une icône à la fenêtre
    window.iconphoto(False, PhotoImage(file='simplon.png'))

    #================ FORMULAIRE ========================

    # Création du formulaire d'ajout d'un employé
    frame = Frame(window, bd=2, background="#ededed", relief=SUNKEN, pady=20, padx=10)
    # Création des champs du formulaire
    first_name = Label(frame, text = "Prénom", bg="#ededed", pady=10)
    a_first_name = Entry(frame)
    name = Label(frame, text = "Nom",bg="#ededed", pady=10)
    a_name = Entry(frame)
    poste = Label(frame, text = "Poste",bg="#ededed", pady=10)
    a_poste = Entry(frame)
    # Création du bouton d'envoi du formulaire
    b = Button(frame ,text="Enregistrer",command=lambda:[check_form(a_first_name.get(), a_name.get(), a_poste.get())])
    # Ajout des champs et du bouton au formulaire
    first_name.pack()
    a_first_name.pack()
    name.pack()
    a_name.pack()
    poste.pack()
    a_poste.pack()
    b.pack(expand=YES, pady=15)

    #================ LISTING ========================

    # Création du listing des employés
    frame3 = Frame(window, bg='#ededed')
    label_title = Label(window, text='Listing des employés', font=("Courrier",24), bg='#ededed', pady=8) 
    # Parcours de la liste des employés
    for index,row in df.iterrows():
        # Création d'une ligne du listing
        frame2 = Frame(frame3, bg='#ededed')
        text = Label(frame2, text='{} : {} {}'.format(row[3],row[1],row[0]), font=("Courrier",12), bg='#ededed') 
        fired_button = Button(frame2, text="Renvoyer", font=("Courrier",8), fg="#fff", bg="#555")
        # Ajout de la ligne au listing
        frame2.pack(pady=3)
        text.grid(row=0, column=0, sticky=W) 
        fired_button.grid(row=0, column=1, sticky=W, padx=5)


    #============== MENU ==========================

    # Création du menu de l'application
    menu_bar = Menu(window)
    file_menu = Menu(menu_bar, tearoff=0)
    # Ajout de l'option "Ajout Employé" au menu
    menu_bar.add_cascade(label="Ajout Employé", command=lambda:[frame.pack(expand=YES),frame3.pack_forget(), label_title.pack_forget()] )
    # Ajout de l'option "Listing employés" au menu
    menu_bar.add_cascade(label="Listing employés ", command=lambda:[frame.pack_forget(), label_title.pack(side=TOP), frame3.pack()])
    # Ajout de l'option "Quitter" au menu
    menu_bar.add_cascade(label="Quitter ",command=lambda:[window.quit()] ) 
    # Ajout du menu à la fenêtre
    window.config(menu=menu_bar)

    # Boucle d'exécution de l'interface graphique
    window.mainloop()


