import json, requests, colorama
from colorama import Fore,Style,Back
from bs4 import BeautifulSoup

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
        r=requests.get(self.url1 + self.plaque)
        self.idcar=json.loads(r.text)
        self.idcar=self.idcar['carId']
        return self.idcar

    def verif(self):
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
        r=requests.get(self.url2 + str(self.idcar))
        self.link=r.text
        return self.link
        
    def scrapElements(self):
        r=requests.get(self.url3 + self.link)
        soup = BeautifulSoup(r.text, 'html.parser')
        modele = soup.find('span',class_ ='bold').get_text()
        motorisation = soup.find('span',class_ ='bold').next_sibling
        annee = motorisation.find_next('span').contents[0]
        return modele, motorisation, annee.strip()

    def info(self):
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