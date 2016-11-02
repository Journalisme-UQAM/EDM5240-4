# conding: utf-8
#Le but de ce travail était d’être en mesure d’avoir d’un seul coup toutes les données, mises sur plusieurs pages d’un tableau du gouvernement du Canada en un seul fichier. 

#J’ai pris le tableau des divulgations de contrats pour les affaires étrangères du premier trimestre 2016-2017. 

#Il serait intéressant d’essayer plus tard de comparer les montants des contrats enter le dernier gouvernement Harper et celui de Trudeau. 

#Pour cela, il faut, en premier, se créer un environnement virtuel. Pour ce faire il faut passer par BeautifulSoup. C’est une sorte de bibliothèque d’HTML écrit en script python, si je comprends bien. Donc, il faut converser avec le logiciel pour lui demander de réagir avec l’environnement de C9. 

#Alors, il faut dans les "commandes" partir ce logiciel.
#Par la suite, il faut démarrer BeautifulSoup dans les instructions (la section du haut de C9 pour moi, c'est la première étape après avoir enregistrer le travail).

import csv import requests from bs4 import BeautifulSoup

#Il faut créer une variable url pour préciser dans quel tableau BS4 doit travailler

url = "http://w03.international.gc.ca/dc/index_fa-ae.aspx?lang=fra&p=3&r=49" fichier = "contrat-affaires-etrangeres.csv"

#n tant que bon journaliste, il faut être poli et bien se présenter. Expliquer pourquoi nous voulons cette information.

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
