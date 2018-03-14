#coding: utf-8

### BONJOUR, ICI Jean-Hugues ###
### Et voici mes notes et corrections, toujours précédées de trois dièses ###

### Avec la page que tu as choisie, c'est plus facile de faire un copier-coller avec les tableaux

import csv
import requests 
from bs4 import BeautifulSoup 

fichier = "Moisson_cbj.csv"

#Cette adresse me donne une liste de chaque saison de chaque joueur
#qui joue présentement pour les Blue Jackets de Columbus.
url = "https://www.hockey-reference.com/teams/CBJ/2018.html"
contenu = requests.get(url)
page = BeautifulSoup(contenu.text,"html.parser")

#Je crée une boucle qui ira chercher de l'information
#présente dans les tableaux
# for joueur in page.find_all("tr"):

### Ça marche bien
	# print(joueur.a)

### Mais en effet, comme tu le dis, le nom du joueur apparaît trois fois...

#J'ai essayé plusieurs fois de trouver un moyen d'isoler seulement les éléments
#du premier tableau, mais en vain. Voici des exemples de lignes que j'ai
#essayées à la place de la ligne 18. Je ne sais vraiment pas si j'étais dans le
#champ complètement ou si l'une d'entre elles était près de la solution. À noter
#que dans le code html, le tableau que je cherchais avait un id="all_roster" alors
#que les autres avaient d'autres nomes. Ils avaient tous la même classe par contre.
#print(page.find("div", id_="all_roster").tr)
#print(page.find("div", id_="all_roster")joueur.a)
#print(page.find("div", id_="all_roster", data-stat_="player")joueur)
#C'est donc dire que pour l'instant, mon moissonage me donne tous les noms des joueurs
#trois fois, dans différents ordres selon les tableaux dont sont extraits les noms.
#Il me donne aussi les href qui me permetteraient, j'imagine, d'accéder à leurs pages
#respectives sur le site. À noter que le second tableau me permet d'obtenir des joueurs
#qui ont été retirés du premier, puisqu'ils ne jouent présentement pas avec l'équipe - soit
#parce qu'ils ont été échangé durant la saison ou qu'ils évoluent présentement dans la ligue
#américaine.

#J'essaie de trouver une façon d'utiliser ce href pour mon 
for joueur in page.find_all("tr"):

### L'autre façon que tu essaies est la bonne.
### Tu trouves tous les «tr» de ta page
### Mais je précise ton code en ajoutant qu'il s'agit seulement des «tr»
### qui se trouvent dans un «tbody», lui-même se trouvant dans une «table» de «id» "roster"
### Je change aussi ta variable «joueurs» par «j» parce que ça me tente (et pcq c plus court)

for j in page.find("table",id="roster").find("tbody").find_all("tr"):

### Première étape: crée-toi une liste dans laquelle tu vas enregistrer les infos que tu recueilles
	joueur = []

### Voici son numéro de chandail
	jersey = j.find("th",attrs={"data-stat":"number"}).text
	joueur.append(jersey)

### Et voici son nom
	nom = j.find("td",attrs={"data-stat":"player"}).text
	joueur.append(nom)

### Et voici sa nationalité
	pays = j.find("td",attrs={"data-stat":"flag"}).text
	joueur.append(pays)

### Et ainsi de suite
	position = j.find("td",attrs={"data-stat":"pos"}).text
	joueur.append(position)

	age = j.find("td",attrs={"data-stat":"age"}).text
	joueur.append(age)

	taille = j.find("td",attrs={"data-stat":"height"}).text
	joueur.append(taille)

	poids = j.find("td",attrs={"data-stat":"weight"}).text
	joueur.append(poids)

	drGauche = j.find("td",attrs={"data-stat":"shoots_and_catches"}).text
	joueur.append(drGauche)

	exp = j.find("td",attrs={"data-stat":"years_experience"}).text
	joueur.append(exp)

	dateNaiss = j.find("td",attrs={"data-stat":"birth_date"}).text
	joueur.append(dateNaiss)

	sommaire = j.find("td",attrs={"data-stat":"summary"}).text
	joueur.append(sommaire)

	salaire = j.find("td",attrs={"data-stat":"salary"}).text
	joueur.append(salaire)

	rep = j.find("td",attrs={"data-stat":"draft"}).text
	joueur.append(rep)

	print(joueur)

	# for page_joueur in range(27):
	# 	url = "https://www.hockey-reference.com{joueur.a:href}"
		# print(url)

		#coding: utf-8

# import csv
# import requests 
# from bs4 import BeautifulSoup 

# fichier = "Moisson_cbj.csv"

# #Cette adresse me donne une liste de chaque saison de chaque joueur
# #qui joue présentement pour les Blue Jackets de Columbus.
# url = "https://www.hockey-reference.com/teams/CBJ/2018.html"
# contenu = requests.get(url)
# page = BeautifulSoup(contenu.text,"html.parser")

# #J'essaie de trouver un façon d'utiliser ce href pour accéder aux pages
# url_joueur = page.find_all("tr", "href")
# for lien in url_joueur:
# 	nom = []
# 	lien = lien.a["href"]
# 	lien_joueur = "https://www.hockey-reference.com" + lien
# 	print(lien_joueur)
# #autre essai
# for joueur in page.find_all("tr"):
	# print(joueur.a)
#Ceci n'a pas fonctionné pour l'instant :(
