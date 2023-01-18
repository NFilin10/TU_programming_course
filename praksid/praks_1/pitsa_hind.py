from math import pi

läbimõõt = int(input("Milline on pitsa läbimõõt? "))
hind = float(input("Mitu eurot pitsa maksab? "))

pitsa_pindala = (läbimõõt / 2) ** 2 * pi

res = hind / pitsa_pindala * 100
print("Pitsa ühe ruutsentimeetri hind on " + str(res) + " senti.")