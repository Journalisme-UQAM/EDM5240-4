# conding: utf-8
import csv import requests from bs4 import BeautifulSoup

url = "http://w03.international.gc.ca/dc/index_fa-ae.aspx?lang=fra&p=3&r=49" fichier = "contrat-affaires-etrangeres.csv"

entetes = { "User-Agent": "Raphae;;e Joo - pour un cours de journalisme à l'UQAM", "From":"rafoujoo@hotmail.com" }

information = requests.get(url, headers=entetes) page = BeautifulSoup(information.text,"html.parser")

print(page)

i = 0

for ligne in page.find_all("tr"): if i !=0: # print(ligne) lien = ligne.a.get("href") print(lien) hyperlien = "http://w03.international.gc.ca/dc/"+lien print(i, hyperlien)

    contenu2 = requests.get(hyperlien, headers=entetes)
    page2 = BeautifulSoup(contenu2.text, "html.parser")

    information = []

    information.append(hyperlien)

    for item in page2.find_all("td"):
        print(item)
    if item.td is not None:
        information.append(item.td.text)
    else:
        information.append(None)
    print(information)

    bigmac = open(fichier,"a")
    fromage = csv.writer(bigmac)
    fromage.writerow(information)



i += 1
