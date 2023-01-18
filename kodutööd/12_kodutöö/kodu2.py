class Tõukeratas:
    def __init__(self, firma, alustus_tasu, sada_m_hind, kaugus):
        self.firma = firma
        self.alustus_tasu = alustus_tasu
        self.sada_m_hind = sada_m_hind
        self.kaugus = kaugus
    
    
    def sõidu_hind(self, pikkus):
        if pikkus <= self.kaugus:
            return self.alustus_tasu + (pikkus*self.sada_m_hind/0.1)
        else:
            return 1000
      
    def sõida(self, pikkus):
        self.kaugus = self.kaugus - pikkus
        if self.kaugus <= 0:
            self.pikkus = 0
    
    def lae(self, km):
        self.kaugus += km


class Laenutus:
    def __init__(self, firmad):
        self.isendite_jrj = firmad
               
    def kuva_valik(self, pikkus):
        c = 1
        firmade_dict = {}
        for i in self.isendite_jrj:
           firmade_dict[i.firma] = i.sõidu_hind(pikkus)
        for k in sorted(firmade_dict, key=firmade_dict.get):      
             print(f"{c}. {k} - {round(firmade_dict[k], 1)} eurot")
             c += 1
       
    def laenuta(self, firma, pikkus):
        for isend in self.isendite_jrj:
            if isend.firma == firma:
                if pikkus <= isend.kaugus:  
                    print(f"Sõidu hind oli {round(isend.sõidu_hind(pikkus), 1)} eurot")
                    isend.sõida(pikkus)   
                else:
                    print("Tõukeratta aku on liiga tühi selle sõidu jaoks.")
                          
    def lae_tõukeratast(self, firma, km):
        for isend in self.isendite_jrj:
            if isend.firma == firma:
                isend.lae(km)

                  
firma1 = input("Sisesta firma, alustustasu, saja meetri hind, sõidukaugus: ").split(",")
firma2 = input("Sisesta firma, alustustasu, saja meetri hind, sõidukaugus: ").split(",")
firma3 = input("Sisesta firma, alustustasu, saja meetri hind, sõidukaugus: ").split(",")


firma1 = Tõukeratas(firma1[0], float(firma1[1]), float(firma1[2]), float(firma1[3]))
firma2 = Tõukeratas(firma2[0], float(firma2[1]), float(firma2[2]), float(firma2[3]))
firma3 = Tõukeratas(firma3[0], float(firma3[1]), float(firma3[2]), float(firma3[3]))

firmad = [firma1, firma2, firma3]

rk = Laenutus(firmad)

rk.kuva_valik(2)
rk.laenuta("Bolt", 3)
rk.laenuta("Tuul", 18)
rk.laenuta("Tuul", 5)
rk.lae_tõukeratast("Tuul", 5)
rk.laenuta("Tuul", 2)


