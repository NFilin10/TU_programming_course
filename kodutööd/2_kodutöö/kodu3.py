import math

pikkus = float(input("Sisesta ruumi pikkus: "))
laius = float(input("Sisesta ruumi laius: "))
kõrgus = float(input("Sisesta ruumi kõrgus: "))
maht = float(input("Sisesta purgi maht: "))

pindala_värvimiseks = 2 * (laius + pikkus) * kõrgus
l_värvi = pindala_värvimiseks / 8
purke = l_värvi / maht
print("Tuleb osata", math.ceil(purke), "purki värvi.")