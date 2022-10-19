import pandas as pd 
liste = pd.read_table("liste_employes.txt")
liste = pd.read_csv("liste_employes.txt",sep=",")
liste = liste.set_axis(['Nom', 'Prenom', 'Date', 'Poste'], axis=1, inplace=False)
liste.to_csv('liste_employes.csv', index = False)