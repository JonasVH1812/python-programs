import random
from num2words import num2words

def clean_text(t):
    return t.replace(",", "").strip()

while True:
    number = random.randint(1, 1_000_000)
    correct_text = clean_text(num2words(number))

    print(f"\nschrijf deze nummer in woorden: {number}")
    answer = clean_text(input("Je antwoord: ").strip().lower())

    if answer == correct_text:
        print("JUIST!")
    else:
        print("Fout volgende keer beter :) : ")
        print(f"Dit was het juiste: {correct_text}")

    again = input("\nNog een nummer? (ja/nee): ").strip().lower()
    if again != "ja":
        break

print("Dada!")
