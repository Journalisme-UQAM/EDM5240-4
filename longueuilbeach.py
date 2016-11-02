# conding: utf-8
#Le but de ce travail était d’être en mesure d’avoir d’un seul coup toutes les données, mises sur plusieurs pages d’un tableau du gouvernement du Canada en un seul fichier. 

#J’ai pris le tableau des divulgations de contrats pour les affaires étrangères du premier trimestre 2016-2017. 

#Il serait intéressant d’essayer plus tard de comparer les montants des contrats enter le dernier gouvernement Harper et celui de Trudeau. 

#Pour cela, il faut, en premier, se créer un environnement virtuel. Pour ce faire il faut passer par BeautifulSoup. C’est une sorte de bibliothèque d’HTML écrit en script python, si je comprends bien. Donc, il faut converser avec le logiciel pour lui demander de réagir avec l’environnement de C9. 

#Alors, il faut dans les "commandes" partir ce logiciel.
#Par la suite, il faut démarrer BeautifulSoup dans les instructions (la section du haut de C9 pour moi, c'est la première étape après avoir enregistrer le travail).

import csv import requests from bs4 import BeautifulSoup

#Il faut créer une variable url pour préciser dans quel tableau BS4 doit travailler.

url = "http://w03.international.gc.ca/dc/index_fa-ae.aspx?lang=fra&p=3&r=49" fichier = "contrat-affaires-etrangeres.csv"

#En tant que bon journaliste, il faut être poli et bien se présenter. Expliquer pourquoi nous voulons cette information.

entetes = { "User-Agent": "Raphae;;e Joo - pour un cours de journalisme à l'UQAM", "From":"rafoujoo@hotmail.com" }

information = requests.get(url, headers=entetes) page = BeautifulSoup(information.text,"html.parser")
#Pour nous assurer que nous sommes sur le bon chemin, nous imprimons la page de « base » celle qui contient l’information du premier tableau. 
print(page)

i = 0
# Dans les documents, il y a des en-têtes non désirés, qui ne contiennent pas de l’information concrète pour nous. Pour cela, il faut trier l’information. 
# La variable i = 0 est créée pour par la suite être en mesure d’obtenir l’information par « ligne ». 
# Plus bas dans le document il est important de préciser i +=1 car si nous indiquons seulement i = 0, toutes les variables rechercher vont rester à 0 donc nous n’aurions aucune information. 
# Pour aller chercher tous les rangers, ils sont après la ligne 0. 
# La première demande de i = 0 c’était vraiment pour retirer la première ligne, car la première ligne pour nous en langage de code est à la ligne zéro. 
# Lorsque l’on observe l’information tirée de la première « impression », on remarque qu’au début des colonnes elles sont inscrites en >tr<. 
# Donc il faut chercher toute l’information d’un immense tableau en tr. 
# Le terme find all est utilisé pour que toutes les lignes de tr du fichier soient imprimées lorsque l’on demande le print. 
# Il fallait vérifier en premier que le i= !0 fonctionne dans ce cas.
# Lorsque j’ai fait print, j’ai eu la chance que cela fonctionne contrairement à la première version.
# Ce qui signifie qu’après la colonne d’informations inutiles, de « vide », il n’y en avait pas de deuxième ou de troisième.  
# Lorsque les lignes sont imprimées, il y a l’information (href) qui apparaît. 
# En faite, ce que cela signifie, c’est que c’est notre porte d’entrée vers un nouveau monde. Celui de toutes les sous-informations cachées dans des sous-tableaux, des liens. 
# Il faut aller le chercher avec cette commande pour trier le lien et l’hyperlien qui, à deux, forme le tout. 
# La dernière étape de cette recette est d’ajouter l’ingrédient manquant, l’hyperlien. 
# Nous avons créé la variable lien.
#  Cette dernière n’était pas entière. 
# Il a fallu trouver le bon lien pour l’allier à la nouvelle variable de l’hyperlien. 
# Dans ce cas, l’url était particulier. 
# Il ne débutait pas par www.
# Il a fallu prendre la forme de « base » du site web pour que cela fonctionne. 
# C’est pourquoi les www ont été remplacés par w03.

for ligne in page.find_all("tr"): if i !=0: # print(ligne) lien = ligne.a.get("href") print(lien) hyperlien = "http://w03.international.gc.ca/dc/"+lien print(i, hyperlien)

# Pour obtenir l’information relative aux subventions il faut recréer la recette.
# C’est pourquoi il y a des numéros 2 dans les variables.
# Il faut demander d’aller chercher les sous-pages.
# C’est pourquoi on interagit avec la variable « hyperlien » créée à l’étape précédente. 
# De plus, on rappelle BeautifulSoup pour cette deuxième recette puisqu’elle est neuve.
# C'est très important de ne jamais quitter la première boucle créée. 
# Attention à la maudite indentation!

    contenu2 = requests.get(hyperlien, headers=entetes)
    page2 = BeautifulSoup(contenu2.text, "html.parser")
# Pour mieux lire l'information et pour y avoir accès sur une même page sans recommencer l'exercice, il faut créer un nouveau fichier en utilisant les crochets.
    information = []
# Pour s'assurer que le tout fonctionne bien, on refait le lien entre l'hyperlien et ce qu'on recherche. 
    information.append(hyperlien)
#  Puisque tout se trouve dans des tableaux individuels, il faut faire comme au début.
# Attention, cette fois-ci l'information est enregistrée en "td" au début des lignes. 
# Donc on reprend la même recette, mais avec la deuxième page programmer et on recherche en "td".
# Pour éviter les erreurs causées par des cellules coquines (des cellules vides), on demande au logiciel de passer par dessus et de seulement laisser un vide entre deux virgules lors de l'impression.
# Ainsi, oui, il y a l'étape du None, mais à cette étape on demande de donner l'information. Comme s'il n'avait pas de vide.
# Mais pour "remplir" les vides, il faut aller plus loin. Sinon le vide va rester vide pour notre script.
# Donc on ajouter la variable elss. 
    for item in page2.find_all("td"):
        print(item)
    if item.td is not None:
        information.append(item.td.text)
    else:
        information.append(None)
    print(information)
# Pour finaliser le tout, il faut ajouter des nouvelles lignes au fichier csv pour qu'il soit complet.
# Avec ces nouvelles lignes, l'information apparaît au complet et de façon structurer pour chaque case et sous tableau du tableau principal.
    bigmac = open(fichier,"a")
    fromage = csv.writer(bigmac)
    fromage.writerow(information)



i += 1
