# 
# 
# sisud = ['''Mikk
# Triin
# Riina''',
# '''Vahur
# Riina
# Kaido
# Mikk
# ''',
# '''Riina
# Ellen
# Vahur
# Triin
# ''']
# for i in range(3):
#     with open("üritused"+str(i+1)+".txt", "w") as fail:
#         fail.write(sisud[i])


urituste_arv = int(input("Sisesta ürituste arv: "))
osalejad = set()
populaarseim = 0
suurim_esmakordsete_arv = 0

for i in range(urituste_arv):
    esmakordsed = 0
    with open("üritused"+str(i+1)+".txt") as fail:
        nimed = fail.read().strip().split("\n")
    
    for nimi in nimed:
        if nimi not in osalejad and i > 0:
            esmakordsed += 1
            
        osalejad.add(nimi)
    
    if esmakordsed > suurim_esmakordsete_arv:
        suurim_esmakordsete_arv = esmakordsed
        populaarseim = i+1
    


print(f"Kõige rohkem esmakordseid osalejaid, {suurim_esmakordsete_arv} osalejat, oli üritusel {populaarseim}.")
    
    
    
    
    
    