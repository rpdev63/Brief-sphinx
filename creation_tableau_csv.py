import pandas as pd 
#liste = pd.read_table("liste_employes.txt")
liste = pd.read_csv("liste_employes.txt",sep=",")
liste.to_csv('liste_employes.csv', index = False)