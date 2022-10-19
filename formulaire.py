import datetime
from tkinter import *
from tkinter import messagebox
import pandas as pd

# Nom, Prénom, Date embauche, Poste
df = pd.read_csv(r'liste_employes.csv')


# df = df.append(df.iloc[len(df)][0])


def write_line_in_csv(first_name,name, date, poste) :
    list_employes = pd.read_csv("liste_employes.csv")
    df_new_line =  pd.DataFrame([[first_name,name,date,poste]], columns=['Nom', 'Prénom', 'Date embauche', 'Poste'])
    list_employes = pd.concat([list_employes,df_new_line], ignore_index=True, axis=1)
    list_employes.to_csv('liste_employes.csv', index = False)

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

#================ LISTING ========================

frame3 = Frame(window, bg='#ededed')
label_title = Label(window, text='Listing des employés', font=("Courrier",24), bg='#ededed', pady=8) 
for index,row in df.iterrows():
    frame2 = Frame(frame3, bg='#ededed')
    text = Label(frame2, text='{} : {} {}'.format(row[3],row[1],row[0]), font=("Courrier",12), bg='#ededed') 
    fired_button = Button(frame2, text="Renvoyer", font=("Courrier",8), fg="#fff", bg="#555")
    frame2.pack(pady=3)
    text.grid(row=0, column=0, sticky=W) 
    fired_button.grid(row=0, column=1, sticky=W, padx=5)



#============== MENU ==========================

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ajout Employé", command=lambda:[frame.pack(expand=YES),frame3.pack_forget(), label_title.pack_forget()] )
menu_bar.add_cascade(label="Listing employés ", command=lambda:[frame.pack_forget(), label_title.pack(side=TOP), frame3.pack()])
menu_bar.add_cascade(label="Quitter ",command=lambda:[window.quit()] ) 
window.config(menu=menu_bar)

window.mainloop()


