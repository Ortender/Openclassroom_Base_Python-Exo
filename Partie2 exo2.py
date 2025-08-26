#je déclare les variables et les listes afin de pourvoir les manipuler dans les boucles
liste = []
liste_entiers = []
resultat_sommes = 0
superieur_moyenne = 0
#je demande à l'utilisateur de m'indiquer la série de nombres
nombres = input("Veuillez indiquer une série de nombres séparés par des virgules, exemple : 1, 22, 3, 174 ")
#la boucle while va permettre de vérifier si l'utilisateur a founi une série de nombres et sinon de lui redemander une information correcte
while not liste_entiers :
    liste = nombres.split(',')
    #la fonction try permet de vérifier la série fourni par l'utilisateur sans déclencher d'erreur interrompant le programme
    try:
        for y in liste:
            liste_entiers.append(int(y))
    except:
        liste_entiers.clear()
        nombres = input("La série indiqué ne comporte pas que des nombres, veuillez indiquer une série de nombres ")
#la boucle for permet d'additioner les valeurs de la série
for x in liste_entiers:
    nombres_a_additioner = x
    resultat_sommes = resultat_sommes + nombres_a_additioner
print(f'la somme des nombres est égale à {resultat_sommes}')
#la moyenne est obtenue en réutilisant la le résultat de la somme et en la divisant par la longueur de la série
Moyenne = round(resultat_sommes / len(liste_entiers), 2)
print(f'la moyenne des nombres est égale à {Moyenne}')
#avec cette boucle on va incrémenter une variable à chaque fois qu'un nombre est supérieure à la moyenne calculé précedemment
for x in liste_entiers:
    if x > Moyenne:
        superieur_moyenne = superieur_moyenne + 1
    else:
        continue
print(f'{superieur_moyenne} nombres sont supérieures à la moyenne')