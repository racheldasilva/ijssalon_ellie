def mijn_functie_1(n):
    return n * n

def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst
inputs = [(12, 3), (12, 2), (10, 5), (100, 20)]
for a,b in inputs:
    resultaat = mijn_functie_2(a,b)