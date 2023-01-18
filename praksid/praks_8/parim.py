
def loe_andmed(failinimi):
    with open(failinimi) as fail:
        sisu = fail.read().strip().split("\n")
     
    tulemus = []
    for rida in sisu:
        ajutine = rida.split(';')
        for i in range(len(ajutine)):
            if i != 0:
                ajutine[i] = int(ajutine[i])
                
        tulemus.append(ajutine)
        
    return tulemus


def parim_töötaja(andmed, kuu):
    parim_nimi = ''
    suurim_myyk = 0
    
    for rida in andmed:
        if rida[kuu] > suurim_myyk:
            parim_nimi = rida[0]
            suurim_myyk = rida[kuu]
    return parim_nimi

print(parim_töötaja(loe_andmed("müügid.txt"), 5))
