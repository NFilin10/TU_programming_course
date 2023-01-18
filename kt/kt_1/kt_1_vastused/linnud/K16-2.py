from math import sqrt, pi

def kraavi_pikkus(pindala, kuju):
    if kuju == "ruut":
        return round(sqrt(pindala * 10_000) * 4, 1)
    else:
        return round(sqrt(pindala * 10_000 / pi) * pi * 2, 1)

def kraavi_hind(pikkus, tunnipalk):
    return 2 * pikkus * tunnipalk

pindala = int(input("Sisesta soo pindala: "))
kuju = input("Sisesta soo kuju: ")
tunnipalk = float(input("Sisesta sulase tunnipalk: "))
print(f"Soo kaevamiseks kulub {kraavi_hind(kraavi_pikkus(pindala, kuju), tunnipalk)} eurot.")
