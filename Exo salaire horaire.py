def conversion_entier (a,b):
    entier1 = int(a)
    entier2 = int(b)
    return entier1, entier2
def salaire_mensuel(x):
    resultat = x/12
    return resultat
def salaire_hebdomadaire(y):
    resultat = y/4
    return resultat
def salaire_horaire(a,b):
    resultat = a/b
    return resultat

salaire_annuel = input("veuillez saisir votre salaire annuel ")
heure_travaillées = input("veuillez saisir votre temps de travail hebdomdaire ")
salaire_annuel_et_heures = ()
while not salaire_annuel_et_heures :
    try:
        salaire_annuel_et_heures = conversion_entier(salaire_annuel, heure_travaillées)
    except:
        salaire_annuel = input("le salaire annuel ou les heures travaillées n'ont pas été saisis au bon format. Merci de les saisir à nouvau. Salaire annuel: ")
        heure_travaillées = input("Heures travaillées: ")

salaire_mois = salaire_mensuel(salaire_annuel_et_heures[0])
salaire_semaine = salaire_hebdomadaire(salaire_mois)
taux_horaire = salaire_horaire(salaire_semaine, salaire_annuel_et_heures[1])
print(f"votre salaire horaire est {round(taux_horaire, 2)}€")