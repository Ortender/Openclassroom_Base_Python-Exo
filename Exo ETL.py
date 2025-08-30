import re
from bs4 import BeautifulSoup
with open("index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')
Page_title = soup.title.string
H1_Title = soup.find('h1', id="titre").string
Product_info_clean={}
#Les information de chaque produits sont encapsulées dans une balise 'li', je créé une liste contenant les éléments de chaque produit.
#Je parcours la liste de pour en extraire et rangé les informations dans chaque catégorie (nom, pix, description)
for product in soup.find_all('li'):
   #Pour chaque élément j'identifie la balise qui l'encapsule et je récupère la chaine de caractère entre les balise
   Product_name=product.find('h2').string
  #Je veux le prix en nombre entier, alors j'utilise a fonction split pour enlever le texte subterflu (+ le signe € est mal interprété alors je le nettoieavec â)
   Price_raw=product.find('p', class_="price").string.split(":")
   Price_intermediary=Price_raw[1].split("â")
   Product_Price=int(Price_intermediary[0])
   Product_Description=product.find(string= re.compile("Description")).string
   #Je range les informations de chaque produit dans un dictionnaire
   Product_info_clean[Product_name]={"prix" : Product_Price}
   Product_info_clean[Product_name]["Description"]=Product_Description
#Je converti le prix en Euro en Dollars pour chaque produit
for product in Product_info_clean:
   Product_info_clean[Product_name]["prix"]=Product_info_clean[Product_name]["prix"]*1.2
   print(f'{product}: {round(Product_info_clean[Product_name]["prix"],2)}$')
'''
for Product in All_Product:
    All_Product_string.append(Product.string)
print(All_Product_string)
Price = soup.find("p", class_="price").string
print(Price)
description = soup.find(string= re.compile("Description"))
print(description)
for i in soup.find_all('li'):
   Product[soup.find('h2')] = soup.select("p.price", limit=1) + soup.find("Description")
   print(Product)
'''