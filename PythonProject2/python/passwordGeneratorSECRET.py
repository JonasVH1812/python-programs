import secrets
import string
import sys

def genereer(length: int) -> str:
    """Genereer een veilig wachtwoord van 'length' tekens."""
    # Kies welke tekens toegestaan zijn:
    letters = string.ascii_letters + string.digits + string.punctuation
    # Bouw wachtwoord met secrets.choice voor cryptografische veiligheid:
    return ''.join(secrets.choice(letters) for _ in range(length))

def main():
    while True:
        # 'Scherm wissen' door een paar nieuwe regels — cross-platform alternatief:
        print("\n" * 30)
        print("Je huidige wachtwoord is nog niet gegenereerd." )
        antwoord = input("Wil je een paswoord genereren? (ja/nee) ").strip().lower()

        if antwoord in ("nee", "n", "stop", "quit", "exit"):
            print("Tot ziens!")
            sys.exit(0)

        if antwoord not in ("ja", "y", "j"):
            print("Onbekende invoer — typ 'ja' of 'nee'.")
            input("Druk op Enter om opnieuw te proberen...")
            continue

        lengte_str = input("Welke lengte moet je wachtwoord zijn (bijv. 12): ").strip()
        try:
            lengte = int(lengte_str)
            if lengte < 4:
                print("Kies a.u.b. minimaal 4 tekens voor bruikbaarheid.")
                input("Druk op Enter om opnieuw te proberen...")
                continue
            if lengte > 128:
                print("128 tekens is het maximum (veilig en praktisch).")
                input("Druk op Enter om opnieuw te proberen...")
                continue
        except ValueError:
            print("Ongeldige lengte — voer een geheel getal in.")
            input("Druk op Enter om opnieuw te proberen...")
            continue

        wachtwoord = genereer(lengte)
        print("\nJe wachtwoord is:", wachtwoord)
        # Optioneel: kopiëren naar klembord of bewaren (niet automatisch voor veiligheid)
        again = input("\nNog een wachtwoord genereren? (ja/nee) ").strip().lower()
        if again not in ("ja", "y", "j"):
            print("Tot ziens!")
            break

if __name__ == "__main__":
    main()
