import csv

en_tete=["Nom", "Salaires"]
donnees_brute =[]
donnees_charge=[]

#Je récupère les informations dans le fichier input de l'énoncé (voir input.csv)
with open('input.csv', 'r') as input_csv:
    reader = csv.DictReader(input_csv, delimiter=',')
    #Je stock les informations de chaque ligne dans des dictionnaires
    for ligne in reader:
        donnees_brute.append(ligne)
print(donnees_brute)

for donnee in donnees_brute:
    donnes_transforme ={}
    donnes_transforme['Nom']=donnee['nom']
    try:
        donnes_transforme['Salaires']=int(donnee['heures_travaillees'])*15
    except:
        donnees_charge.clear()
        break
    donnees_charge.append(donnes_transforme)
print(donnees_charge)

if not donnees_charge:
    print("les heures de travailles ne sont pas au format numérique, veuillez corriger le fichier input_csv")
else:
    #Je créé le fichier output pour présenter les informations transformées
    with open('output.csv', 'w', newline='') as ouput_csv:
        writer = csv.DictWriter(ouput_csv, fieldnames=en_tete)
        writer.writeheader()
        #J'écris les éléments récupérés et transformés dans les lignes du nouveau fichier
        for donnees in donnees_charge:
            writer.writerow(donnees)