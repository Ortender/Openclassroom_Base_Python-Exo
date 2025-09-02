import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content

# transforme (parse) le HTML en objet BeautifulSoup
soup = BeautifulSoup(page, "html.parser")

# récupération de tous les éléments
elements = soup.find_all("li", class_="gem-c-document-list__item")

#fonction pour traiter les éléments et les mettre dans des listes
def recuperation_donnees(a, b, c):
    information = a.find(b,class_=c)
    return information.string

resultats = []

for element in elements:
    donnee = (recuperation_donnees(element, 'a', "govuk-link"), recuperation_donnees(element, "p", "gem-c-document-list__item-description"))
    resultats.append(donnee)

'''for element in elements:
    titre = element.find("a", class_="govuk-link")
    description = element.find("p", class_="gem-c-document-list__item-description")
    donnee = (titre.string, description.string)
    resultats.append(donnee)'''

# création du fichier data.csv
en_tete = ["titre", "description"]
with open("data.csv", "w", newline="") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)
    # zip permet d'itérer sur deux listes à la fois
    for donnee in resultats:
        writer.writerow(donnee)
