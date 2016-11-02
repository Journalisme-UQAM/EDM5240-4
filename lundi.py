conding: utf-8

import csv import requests from bs4 import BeautifulSoup

url = "http://www.acdi-cida.gc.ca/acdi-cida/contributions.nsf/vQuarter-Fra?OpenView&RestrictToCategory=p1-2015-2016-Q4"

fichier = "subvention.csv"

entetes = { "User-Agent":"Raphaelle Joo - projet dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)", "From":"rafoujoo@hotmail.com" }

contenu = requests.get(url, headers=entetes) page = BeautifulSoup(contenu.text,"html.parser")

print(page)

i = 0 for ligne in page.find_all("tr"): if i > 1: # print(ligne) lien = ligne.a.get("href") print(lien) hyperlien = "http://www.acdi-cida.gc.ca"+lien print(i, hyperlien)

    contenu2 = requests.get(hyperlien, headers=entetes)
    page2 = BeautifulSoup(contenu2.text, "html.parser")

    subvention = []

    subvention.append(hyperlien)

    for item in page2.find_all("td"):
        print(item)
    if item.td is not None:
        subvention.append(item.td.text)
    else:
        subvention.append(None)
    print(subvention)

    poutine = open(fichier,"a")
    fouine = csv.writer(poutine)
    fouine.writerow(subvention)

i += 1
