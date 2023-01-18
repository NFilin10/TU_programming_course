class Raamat:
    def __init__(self, pealkiri, autor, lk, liik):
        self.pealkiri = pealkiri
        self.autor = autor
        self.lk = lk
        self.liik = liik
        
    def kuva_info(self):
        print(f"{self.pealkiri}, {self.autor}, {self.lk}, {self.liik}")
        

class Raamatukogu:
    def __init__(self):
        self.raamatute_jrj = []
        
    def lisa_raamat(self, isend):
        self.raamatute_jrj.append(isend)
        
    def kuva_raamatud(self):
        print("Raamatukogus olevad raamatud:")
        for raamat in self.raamatute_jrj:
            raamat.kuva_info()
            
    def laenuta_raamat(self, pealkiri):
        for raamat in self.raamatute_jrj:
            if raamat.pealkiri.lower() == pealkiri.lower():
                self.raamatute_jrj.remove(raamat)
                return raamat
        return None 
        
rk = Raamatukogu()

with open("raamatud.txt") as f:
    sisu = f.read().strip().split("\n")
    
for i in sisu:
    pealkiri, autor, lk, liik = i.strip().split(",")
    rk.lisa_raamat(Raamat(pealkiri, autor, lk, liik))
rk.kuva_raamatud()

while True:
    raamat_laenuks = input("Sisesta raamatu pealkiri, mida sa laenutada soovid: ")
    tulemus = rk.laenuta_raamat(raamat_laenuks)
    if tulemus == None:
        print("Ei leidnud sellist raamatut, proovi uuesti!")
        continue
    else:
        print(f"Raamat {raamat_laenuks} edukalt laenutatud!")
        rk.kuva_raamatud()
        break