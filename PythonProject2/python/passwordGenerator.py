import random
import string

antwoord = "niks"
result_str = "niks"

while True:
    def vraag():
        global antwoord
        for i in range(50):
            print("\n")
        print("je wachtwoord is ", result_str)
        antwoord = input("wil je een paswoord genereren: ")
        if antwoord.lower() == "ja":
            lenght = input("welke lengte moet je wachtwoord zijn: ")
            genereer(lenght)
        elif antwoord.lower() == "nee":
            print("tot siens")


    def genereer(length):
        global result_str
        int(length)
        letters = string.ascii_uppercase + string.ascii_lowercase + string.hexdigits + "!@#$%&"
        result_str = ''.join(random.choice(letters) for i in range(int(length)))
        print("je wachtwoord is ", result_str)
    vraag()
