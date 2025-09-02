import csv

en_tete=["Nom", "Heures travaillées"]
Noms =[]
Salaires = []

#Je récupère les informations dans le fichier input de l'énoncé (voir input.csv)
with open('input.csv', 'r') as input_csv:
    reader = csv.DictReader(input_csv, delimiter=',')
    #Je stock les informations de chaque ligne dans des listes
    for ligne in reader:
        Noms.append(ligne['nom'])
        #En même temps que je stock les informations dans les listes j'en profite pour transformé les heures de travail en salaire
        try:
            Salaires.append(int(ligne['heures_travaillees'])*15)
        except:
            Noms.clear()
            Salaires.clear()
            break

if not Salaires:
    print("les heures de travailles ne sont pas au format numérique, veuillez corriger le fichier input_csv")
else:
    #Je créé le fichier output pour présenter les informations transformées
    with open('output.csv', 'w', newline='') as ouput_csv:
        writer = csv.writer(ouput_csv, delimiter=',')
        writer.writerow(en_tete)
        #J'écris les éléments récupérés et transformés dans les lignes du nouveau fichier
        for nom, salaire in zip(Noms, Salaires):
            writer.writerow([nom,salaire])