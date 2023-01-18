import string

def eelarve(inimesi):
    return inimesi * 10 + 55

faili_nimi = input("Sisesta failinimi: ")
fail = open(faili_nimi)
sisu = fail.read()

tuleb = sisu.count("+")
ei_tule = sisu.count("-")
ei_tea = sisu.count("?")

print(f"Kokku on kutsutud {tuleb + ei_tule + ei_tea} inimest")
print(f"Vähim võimalik osavõtjate arv on {tuleb}")
print(f"Suurim võimalik osavõtjate arv on {tuleb + ei_tea}")
print(f"Peo vähim võimalik eelarve on {eelarve(tuleb)} eurot")
print(f"Peo suurim võimalik eelarve on {eelarve(tuleb + ei_tea)} eurot")

