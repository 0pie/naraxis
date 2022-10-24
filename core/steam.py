import json, requests, colorama
from colorama import Fore,Style,Back
from bs4 import BeautifulSoup
colorama.init()

erreur = "["+Fore.RED+"x"+Fore.RESET+"]"
unsure = "["+Fore.YELLOW+"~"+Fore.RESET+"]"
found = "["+Fore.GREEN+"!"+Fore.RESET+"]"
info = "["+Fore.BLUE+"?"+Fore.RESET+"]"

class steamSearch:
    param: str = ''
    def __init__(self,param):
        self.url: str = 'https://www.steamidfinder.com/lookup/'
        self.param = param
        self.elems = []
        self.fr = []

    def scrapInfo(self):
        r=requests.get(self.url + self.param)
        soup = BeautifulSoup(r.text, 'html.parser')
        div = soup.find('div', class_ = 'panel-body')
        self.elems = div.find_all('code')
        return self.elems

    def scrapFriends(self):
        r=requests.get(f'https://steamcommunity.com/profiles/{self.elems[2].get_text()}/friends/')
        soup = BeautifulSoup(r.text, 'html.parser')
        div=soup.find('div', class_ ="friends_content")
        for friends in div.find_all('a', href=True):
            self.fr.append(friends['href'])
        return self.fr
    
    def dispInfo(self):
        self.scrapInfo()
        self.scrapFriends()
        customid=self.elems[4].get_text().split('/')[4]
        if self.elems[4].get_text().split('/')[3] == 'id':
            idstate=found
            if(self.elems[7].get_text()=='Private'):
                print(" ["+Fore.RED+"!"+Fore.RESET+"] Profile is private")
                crstate=""
                nastate=""
                lostate=""
            elif(self.elems[10].get_text()=='Not set' or self.elems[9].get_text()=='Not set'):
                crstate=(f'\n {found} Creation Date: {self.elems[7].get_text()}')
                if(self.elems[9].get_text()=='Not set'):
                    nastate=""
                    lostate=(f'\n {found} Location: {self.elems[10].get_text()}')
                elif(self.elems[10].get_text()=='Not set'):
                    lostate=""
                    nastate=(f'\n {found} Real Name: {self.elems[9].get_text()}')
            else:
                crstate=(f'\n {found} Creation Date: {self.elems[7].get_text()}')
                lostate=(f'\n {found} Location: {self.elems[10].get_text()}')
                nastate=(f'\n {found} Real Name: {self.elems[9].get_text()}')
            return(f' {found} Username: {self.elems[8].get_text()} {nastate} \n {found} SteamID: {self.elems[0].get_text()}\n {idstate} Custom Id: {customid} {lostate} {crstate}')
        else:
            idstate=unsure
            if(self.elems[6].get_text()=='Private'):
                print(" ["+Fore.RED+"!"+Fore.RESET+"] Profile is private")
                crstate=""
                nastate=""
                lostate=""
            elif(self.elems[9].get_text()=='Not set' or self.elems[8].get_text()=='Not set'):
                crstate=(f'\n {found} Creation Date: {self.elems[6].get_text()}')
                if(self.elems[8].get_text()=='Not set'):
                    nastate=""
                    lostate=(f'\n {found} Location: {self.elems[9].get_text()}')
                elif(self.elems[9].get_text()=='Not set'):
                    lostate=""
                    nastate=(f'\n {found} Real Name: {self.elems[8].get_text()}')
            else:
                crstate=(f'\n {found} Creation Date: {self.elems[6].get_text()}')
                lostate=(f'\n {found} Location: {self.elems[9].get_text()}')
                nastate=(f'\n {found} Real Name: {self.elems[8].get_text()}')
            return(f' {found} Username: {self.elems[7].get_text()} {nastate} \n {found} SteamID: {self.elems[0].get_text()}\n {idstate} Custom Id: {customid} {lostate} {crstate}')
