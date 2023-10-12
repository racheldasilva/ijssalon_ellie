import math
def discriminant(a,b,c):
    D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
    D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
    uitvoer = [D1, D2]
    return uitvoer
print("voor de formuleax^2 +bx + c:" )
a = int(input("Geef a: "))
b = int(input("Geef b: "))
c = int(input("Geef c: "))
try:
    uitkomst = discriminant(a,b,c)
    D1 = uitkomst[0]
    D2 = uitkomst[1]
    print(f"voor waarde a={a}, b={b}, c={c}, zijn de wortels D1={D1} en D2={D2}")
except ValueError:
    print("geen oplossing voor D1 en D2")