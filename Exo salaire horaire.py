def get_int (phrase):
    user_input_int = None
    while not user_input_int:
        try:
            user_input = input(phrase)
            user_input_int = int(user_input)
        except:
            phrase = "le format est incorret, veuillez saisir l'information à nouveau: "
            continue
    return user_input_int
def salaire_mensuel(x):
    resultat = x/12
    return resultat
def salaire_hebdomadaire(y):
    resultat = y/4
    return resultat
def salaire_horaire(a,b):
    resultat = a/b
    return resultat

salaire_annuel = get_int("veuillez saisir votre salaire annuel ")
heure_travaillées = get_int("veuillez saisir votre temps de travail hebdomdaire ")

salaire_mois = salaire_mensuel(salaire_annuel)
salaire_semaine = salaire_hebdomadaire(salaire_mois)
taux_horaire = salaire_horaire(salaire_semaine, heure_travaillées)
print(f"votre salaire horaire est {round(taux_horaire, 2)}€")