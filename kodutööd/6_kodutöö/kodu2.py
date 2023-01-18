
fail = open("taksohinnad.txt", "r")
pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

if pikkus <= 0:
    print("Viga")
    
else:
    read_file = fail.readlines()

    hinnad = []
    firma = []

    for i in read_file:
        firma.append(i.split(",")[0])
        hinnad.append(float(i.split(",")[1]) + pikkus * float(i.split(",")[2]))

    parim_hind = min(hinnad)

    print(f"Kõige odavam on {firma[hinnad.index(parim_hind)]}")
fail.close()