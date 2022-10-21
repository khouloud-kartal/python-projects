#Le programme devra donc choisir aléatoirement un mot dans le dictionnaire disponible ici, et afficher :
#- Le nombre de vies restantes au joueur
#- Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire. En expert, la liste n’apparaîtra pas)
#- Des “_” pour remplacer les lettres non trouvées
#- Les lettres proposées qui se trouvent dans le mot



#choisir le mode de jeu
difficulte = input("Bonjour, à quel niveau souhaites tu jouer?.débutant, intermédiaire ou expert: ")

Vies = 0
    
def niveau(param):

    nbVies = 0

    while nbVies == 0:
        
        if param == "débutant":
            nbVies = 10

        elif param == "intermédiaire":
            nbVies = 7

        elif param == "expert":
            nbVies = 4

        else:
            param = input("Veuillez choisir un mode de jeu: débutant, intermédiaire ou expert: ")

    return(nbVies)

while Vies == 0:
    Vies = niveau(difficulte)


def underscore2(mot , L = []):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
            
    return r[:-1]

def saisie():
    lettre = input("entrez une lettre: ")
    if len(lettre) > 1 or ord(lettre) < 65 or ord(lettre) > 122:
        print(" ")
        return saisie()
    else:
        print(" ")
        return lettre.upper()


import random

with open("dico_france.txt", "r", encoding='ISO-8859-1') as file:
    allText = file.read()
    words = list(map(str, allText.split()))

    ranword = random.choice(words)
    ranword = ranword.upper()

    ranWord = ranword
    
    tableau = { 'éèêẽ' : 'e'
            , 'ç'    : 'c'
            , 'àâã'  : 'a'
            , 'ù'    : 'u'
            }

    ranWord_sans_accents = ''
    for i in ranword:
        for k in tableau:
            if i in k: i = tableau[k]; break
        ranWord_sans_accents += i

    ranWord = ranWord_sans_accents

# Tant qu'il reste des vies au joueur, le jeu continu
for Vies in range (Vies, 0, -1):  
    lettres_deja_proposees = []
    affichage = underscore2(ranWord)
    print(affichage)

    while '_' in affichage:
        if difficulte == "débutant" or difficulte == "intermédiaire":
        
            print("Lettres déjà proposées: " + str(lettres_deja_proposees))
        
        print("Nombre de vies restante: " + str(Vies))
        lettre = saisie()
        
        if lettre not in lettres_deja_proposees:
            lettres_deja_proposees += [ lettre ]
        
        elif lettre in lettres_deja_proposees:
            print ("lettre déjà saissie")
            Vies +=1
        if lettre not in ranWord:
            Vies -= 1
            
        affichage = underscore2(ranWord , lettres_deja_proposees)
        print(affichage)

        if Vies == 0:
            print("Vous avez perdu")
            break

        print("Vous avez gagné")
    break

