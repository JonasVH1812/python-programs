import random
import time

teller = 1
antwoord = "niks"
computerAntwoord = "niks"
keuzes = ["Scissors", "Rock", "Paper"]


def start_up():
    global antwoord
    global teller
    global computerAntwoord
    teller = 1
    for i in range(len(keuzes)):
        print(teller, keuzes[i])
        teller += 1
    antwoord = int(input("Dit zijn je keuzes, kies een getal van het geen dat je wil spelen: "))
    computerAntwoord = random.randint(1, 4)
    spel()

def spel():
    global antwoord
    global computerAntwoord
    computerAntwoord = random.randint(1, 4)
    if antwoord == computerAntwoord:
        print("Er is niemand gewonnen De computer had: ",computerAntwoord)
    elif antwoord == 1 and computerAntwoord == 2:
        print("De Computer wint! De computer had: ",computerAntwoord)
    elif antwoord == 2 and computerAntwoord == 1:
        print("Jij wint! De computer had: ",computerAntwoord)
    elif antwoord == 2 and computerAntwoord == 3:
        print("De Computer wint! De computer had: ",computerAntwoord)
    elif antwoord == 3 and computerAntwoord == 2:
        print("Jij wint! De computer had: ",computerAntwoord)
    elif antwoord == 3 and computerAntwoord == 1:
        print("De Computer wint! De computer had: ",computerAntwoord)
    elif antwoord == 1 and computerAntwoord == 3:
        print("Jij wint! De computer had: ",computerAntwoord)
    else:
        print("Hmm raar er gebeurd niks wat een koppige computer, de computer had: ",computerAntwoord)
    nogEens = input("Wil je nog een?: ")
    if nogEens.lower() == "ja":
        start_up()
    elif nogEens.lower() == "nee":
        spelGedaan()
    else:
        print("geef een ja of een nee")


def spelGedaan():
    print("Oké tot de volgende!")


start_up()