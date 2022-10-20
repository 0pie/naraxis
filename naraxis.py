import os, sys, colorama
from colorama import Fore,Style,Back
from core.plate import sivSearch

mainMenu = """
 [1] Property Research
 [e] Exit script    [c] Clear Screen"""

propertyMenu = """
 [1] Recherche SIV
 [b] Main Menu    [c] Clear Screen"""

information = "["+Fore.BLUE+"#"+Fore.RESET+"]"
def menu():

	menu = r"""
           ____                      ,
          /---.'.__             ____//
               '--.\           /.---'                                                     
          _______  \\         //               __   _ _______  ______ _______ _     _ _____ _______       
        /.------.\  \|      .'/  ______        | \  | |_____| |_____/ |_____|  \___/    |   |______     
       //  ___  \ \ ||/|\  //  _/_----.\__     |  \_| |     | |    \_ |     | _/   \_ __|__ ______|      
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'         
         //   \'. | \'.|.'/ /_/ /  \\          
        //     \ \_\/" ' ~\-'.-'    \\         Version:       [ """+Fore.GREEN+"1.0"+Fore.RESET+r""" ]
       //       '-._| :H: |'-.__     \\        Author:        [ """+Fore.GREEN+"0pie"+Fore.RESET+r""" ]
      //           (/'vvv'\)'-._\     ||       Scripts:       [ %s ]
      ||                        \\    \|       Database:      [ %s | %s Ko ]
      ||                         \\            
      |/                          ||         Let the spider search for you on its web.  
                                  ||
                                   \\
                                    '
	"""
	print(menu)

os.system('cls')
menu()
print(mainMenu)

try:
    while True:
        option = input("\n naraxis("+Fore.GREEN + "~" + Fore.RESET + ")$ ")

        if option.lower() == 'b':
            os.system('cls')
            menu()
            print(mainMenu)

        elif option.lower() == 'c':
            os.system('cls')

        elif option.lower() == 'e':
            sys.exit("\n "+ information+" Goodbye ")

        elif option == '1':
            print(propertyMenu)
            option = input("\n naraxis("+Fore.GREEN + "~" + Fore.RESET + ")$ ")
            
            while True:
                if option == '1':
                    print("\n "+ information+" Veuillez entrer une plaque d'immatriculation.")
                    siv=sivSearch(input("\n naraxis("+Fore.GREEN + "siv" + Fore.RESET + ")$ "))
                    print(siv.info())

except KeyboardInterrupt:
	sys.exit("\n "+information+" Goodbye")