import json, requests, colorama
from colorama import Fore,Style,Back
from bs4 import BeautifulSoup # BeautifulSoup permet de recuperer des éléments HTML (genre tu precise la classe et ça te recupère le texte)

erreur = "["+Fore.RED+"X"+Fore.RESET+"]"

class sivSearch:
    plaque: str = ''
    def __init__(self, plaque):
        self.url1: str = 'https://www.piecesauto.com/homepage/numberplate?value='
        self.url2: str = 'https://www.piecesauto.com/common/seekCar?carid='
        self.url3: str = 'https://www.piecesauto.com'
        self.plaque: str = plaque
        self.idcar: int = 0
        self.link: str = ''
        self.res1: int = 0
        self.res2: int = 0

    def scrapId(self):
        """
        Fonction retournant l'identifiant de la voiture sur la base SIV
        """
        r=requests.get(self.url1 + self.plaque)
        self.idcar=json.loads(r.text)
        self.idcar=self.idcar['carId']
        return self.idcar

    def verif(self):
        """
        Fonction verifiant si la plaque est valide
        """
        r=requests.get(self.url1 + self.plaque)
        cle=json.loads(r.text)
        if 'message' in cle:
            self.res1 = 1
        elif 'error' in cle:
            self.res1 = 2
        if self.res1 == 1:
            message=cle['message']
            if str(message) == 'Aucune voiture ne correspond \u00e0 cette plaque':
                self.res2 = 1
            elif str(message) == 'Format de plaque d\'immatriculation non valide':
                self.res2 = 2
        return self.res1, self.res2

    def scrapLink(self):
        """
        Fonction qui retourne le lien de la page contenant les informations sur la voiture
        """
        r=requests.get(self.url2 + str(self.idcar))
        self.link=r.text
        return self.link
        
    def scrapElements(self):
        """
        Fonction qui recupère les élements relatifs à la voiture
        """
        r=requests.get(self.url3 + self.link) # on fait la requête sur l'adresse
        soup = BeautifulSoup(r.text, 'html.parser') # on étudie le resultat de la requête (page web) grâce à BeautifulSoup
        modele = soup.find('span',class_ ='bold').get_text() # on recupère l'élement span de class bold
        motorisation = soup.find('span',class_ ='bold').next_sibling # on recupère l'élement suivant
        annee = motorisation.find_next('span').contents[0] # on recupère le span suivant
        return modele, motorisation, annee.strip() # .strip() parce que y'avais des espaces dégueulasses partout sinon

    def info(self):
        """
        Fonction qui gère les différents cas de figures et qui renvoi le résultat au programme principal
        """
        self.verif()
        if self.res1 == 2:
            return("\n "+erreur+' Cooldown, réessayez dans 30min.')
        if self.res2 == 1:
            return("\n "+erreur+' Aucune voiture ne correspond à cette plaque.')
        if self.res2 == 2:
            return("\n "+erreur+' Format de plaque d\'immatriculation non valide.')
        self.scrapId()
        self.scrapLink()
        elem=self.scrapElements()
        return(f'   Modele : {elem[0]}\n   Motorisation : {elem[1]}\n   Production : {elem[2]}')