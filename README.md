# ViveLesCollegues

Projet collaboratif.

Ce code a pour but de créer une interface graphique (avec la bibliothèque tkinter) permettant de gérer une liste d'employés. 
L'interface comporte un formulaire permettant d'ajouter un employé à la liste en entrant son nom, prénom, poste et en cliquant sur le bouton "Enregistrer". 
La liste est enregistrée dans un fichier CSV (Comma Separated Values) nommé "liste_employes.csv".

La fonction "check_form" vérifie que les champs "Prénom" et "Nom" du formulaire ne sont pas vides, et affiche une erreur le cas échéant. Si les champs sont remplis, la fonction appelle la fonction "write_line_in_csv" pour ajouter les données du nouvel employé au fichier CSV, puis affiche un message de validation.

La fonction "write_line_in_csv" lit le fichier CSV, ajoute les données du nouvel employé à la fin de celui-ci et réécrit le fichier CSV avec les données mises à jour.

L'interface comporte également un listing des employés enregistrés dans le fichier CSV, qui est affiché sous le formulaire.



