import datetime
from tkinter import *
from tkinter import messagebox
import pandas as pd

list_employes = pd.read_csv("liste_employes.csv")

def write_line_in_csv(first_name,name, date, poste) :
    
    df_new_line = list_employes([[first_name,name,date,poste]], columns=['Nom','Prénom','Date embauche','Poste'] )
    list_employes = pd.concat([list_employes,df_new_line], ignore_index=True)


def check_form(first_name, name, poste) :
    badValue = True
    error_message = 'erreur'
    #erreurs si un des champs nom et/ou prénom est vide
    if len(first_name.strip()) == 0: 
        error_message = 'Prénom manquant'
        if len(name.strip()) == 0:
            error_message = 'Prénom et nom manquants'
    elif len(name.strip()) == 0 :
        error_message = 'Nom manquant'
    else : badValue = False
    
    if badValue :
        messagebox.showerror("Erreur", error_message)
        pass
    else :
        x = datetime.datetime.now()
        today = "{}/{}/{}".format( x.day, x.month, x.year)        
        # ecrire dans le Csv 
        write_line_in_csv( first_name.capitalize(), name.capitalize(), today, poste)
        # message de validation
        messagebox.showinfo("Traitement du formulaire", "Employé ajouté !")
        pass

# création fenêtre
window = Tk()
window.title("Gestion des employés")
window.geometry("480x360" )
window.maxsize(800, 600)
window.config(background='#2f5df3')
window.iconphoto(False, PhotoImage(file='simplon.png'))

#================ FORMULAIRE ========================

#ajout d'une boite
frame = Frame(window, bd=2, background="#ededed", relief=SUNKEN, pady=20, padx=10)
frame.pack(expand=YES)

first_name = Label(frame, text = "Prénom", bg="#ededed", pady=10)
a_first_name = Entry(frame)
name = Label(frame, text = "Nom",bg="#ededed", pady=10)
a_name = Entry(frame)
poste = Label(frame, text = "Poste",bg="#ededed", pady=10)
a_poste = Entry(frame)
b = Button(frame ,text="Enregistrer",command=lambda:[check_form(a_first_name.get(), a_name.get(), a_poste.get())])

first_name.pack()
a_first_name.pack()
name.pack()
a_name.pack()
poste.pack()
a_poste.pack()
b.pack(expand=YES, pady=15)

window.mainloop()


