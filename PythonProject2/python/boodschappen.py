boodschappen = []

command = "niks"

def command_vragen():
    global command
    command = input("geef je commando (voor tips h): ")

command_vragen()

while True:
    if command.lower() == "h":
        print("\n\n")
        print("voor items toe te voegen a")
        print("voor te verwijderen v")
        print("voor te stoppen s")
        print("voor je lijstje te tonen l")
        command = "niks"
        for i in range(3):
            print("")
        command_vragen()
    elif command.lower() == "a":
        print("\n\n")
        new_item = input("wat wil je toevoegen: ")
        boodschappen.append(new_item)
        print(new_item + " is toegevoegd aan je lijstje")
        print("je lijstje bevat nu:")
        for i in boodschappen:
            print(i)
        command = "niks"
        command_vragen()
    elif command.lower() == "v":
        print("\n\n")
        print("dit is de volgorde ")
        teller = 0
        for i in boodschappen:
            teller = teller + 1
            print(teller,i)
        te_verwijdere = input("Geef de nummer van het te verwijderen item: ")
        int(te_verwijdere)
        te_verwijdere = int(te_verwijdere) - 1
        boodschappen.pop(te_verwijdere)
        print("\n\n")
        print("dit is je lijstje nu")
        for i in boodschappen:
            print(i)
        command_vragen()
    elif command.lower() == "l":
        print("\n\n")
        teller = 0
        for i in boodschappen:
            teller = teller + 1
            print(teller, i)
        command_vragen()
    elif command.lower() == "s":
        print("\n\n")
        print("Ok tot de volgende keer!")
        break
    else:
        print("command niet gekend")
        command_vragen()