class Isik:
    def __init__(self, nimi, vanus, pikkus, kaal):
        self.nimi = str(nimi)
        self.vanus = int(vanus)
        self.pikkus = int(pikkus)
        self.kaal = int(kaal)
    
    def kmi(self):
        return round(self.kaal / (self.pikkus/100)**2, 1)
    

with open("tervisekontroll.txt") as f:
    sisu = f.read().strip().split("\n")
    
for i in sisu:
    nimi, vanus, pikkus, kaal = i.split(",")
    isik = Isik(nimi, vanus, pikkus, kaal)
    indeks = isik.kmi()

    if 19 <= indeks <= 25:
        print(f"{isik.nimi}, {isik.vanus}-aastane: sinu kehamassiindeks on {indeks}, oled normaalkaalus")
    
    elif indeks > 25:
        print(f"{isik.nimi}, {isik.vanus}-aastane: sinu kehamassiindeks on {indeks}, peaksid maha võtma")
    
    else:
        print(f"{isik.nimi}, {isik.vanus}-aastane: sinu kehamassiindeks on {indeks}, peaksid juurde võtma")
    
