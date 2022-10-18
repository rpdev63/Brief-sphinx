def main(): 
    
    confirmation =''
    #Récupération des donnée
    while ( confirmation != 'o' and confirmation !='n' ):
        answer = str(input("Entrez le prénom ou (q)uitter : \n"))
        answer2 = str(input("Entrez le nom ou (q)uitter : \n"))
        answer3 = str(input("Entrez le poste ou (q)uitter : \n"))   
        confirmation = str('Voulez vous confirmer : (o)ui - (n)on') 
    print(answer) 
    print(answer2)
    print(answer3)
   

        


if __name__ == "__main__":
    main()