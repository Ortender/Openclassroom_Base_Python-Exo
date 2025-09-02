import Exo_ETL
import csv

en_tete = ["Produit", "Prix", "Description"]
Produits_clean = Exo_ETL.extraction_html()
Noms = []
Prixs = []
Descriptions = []

with open('produits.csv', 'w', newline="") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)
    for produits in Produits_clean:
        Noms.append(produits)
        Prixs.append(Produits_clean[produits]['prix'])
        Descriptions.append(Produits_clean[produits]['Description'].strip('Description :'))
    for produits,prix,description in zip(Noms,Prixs,Descriptions):
        writer.writerow([produits,prix,description])