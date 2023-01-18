from math import pi

läbimõõt = float(input("Milline on pitsa läbimõõt? "))
hind = float(input("Mitu eurot pitsa maksab? "))

pitsa_pindala = (läbimõõt / 2) ** 2 * pi
res = hind / pitsa_pindala
print("Pitsa ühe ruutsentimeetri hind on", res, "eurot")

