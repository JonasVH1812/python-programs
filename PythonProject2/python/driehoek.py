def pascal_driehoek(n):
    driehoek = []  # lijst van lijsten

    for i in range(n):
        rij = [1] * (i + 1)  # begin met allemaal enen
        for j in range(1, i):
            rij[j] = driehoek[i - 1][j - 1] + driehoek[i - 1][j]
        driehoek.append(rij)

    return driehoek


# Aantal rijen invoeren
n = int(input("Hoeveel rijen van de driehoek van Pascal wil je zien?: "))

driehoek = pascal_driehoek(n)

# Mooi afdrukken
for rij in driehoek:
    print(" ".join(str(x) for x in rij).center(n * 4))
