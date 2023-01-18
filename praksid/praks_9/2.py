
def loe_failist_sonastikku(failinimi):
    sonastik = {}
    
    with open(failinimi) as fail:
        read = fail.read().strip().split('\n')

    for rida in read:
        poeg, isa = rida.split(": ")
        sonastik[poeg] = isa
    
    return sonastik

sonastik = loe_failist_sonastikku("meesliinid.txt")

print(sonastik)


def on_eellane(sonastik, eellane, jarglane):
    
    while True:
        if jarglane in sonastik:
          jarglane = sonastik[jarglane]
          
        else:
            return False
        
        if jarglane == eellane:
            return True


nimed = set()
for k, v in sonastik.items():
    nimed.add(k)
    nimed.add(v)
    
print(nimed)

for nimi1 in nimed:
    for nimi2 in nimed:
        if on_eellane(sonastik, nimi1, nimi2):
            print(nimi1, 'on', nimi2, 'eellane')

