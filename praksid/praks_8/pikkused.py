
pikkused = "195 167 165 190 172 182 187 189 168 174".split()

pikkused.reverse()

p_pikkus = pikkused[0]
p_indeks = 0
p_kaugus = 0
kaugus = 0
kandidaadi_indeks = 0
pikkus = pikkused[0]


for i in range(1, len(pikkused)):
    if pikkused[i] < pikkus:
        kaugus += 1 
    else:
        kandidaadi_indeks = i
        pikkus = pikkused[i]
        kaugus = 0
        
    if kaugus > p_kaugus:
        p_pikkus = pikkus
        p_kaugus = kaugus
        p_indeks = kandidaadi_indeks
    
print(f"Inimene nr {len(pikkused)-p_indeks} pikkusega {p_pikkus} näeb kõige kaugemale.")     
    
    