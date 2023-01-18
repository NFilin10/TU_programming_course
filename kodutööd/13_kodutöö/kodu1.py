class Sõiduk:
    def __init__(self, mark, hind, kytuse_kulu):
        self.mark = mark
        self.hind = hind
        self.kytuse_kulu = kytuse_kulu
    
    def __str__(self):
        return f"{self.mark}, hind {self.hind} eurot, kütusekulu 100 km kohta {self.kytuse_kulu} liitrit"
    
class Veoauto(Sõiduk):
    def sõidu_maksumus(self, teepikkus):
        return round(((teepikkus*float(self.kytuse_kulu))/100)*1.8, 1)
    
    def hobujõud(self):
        print("Veoautol on 500 hobujõudu")
  
  
class Sõiduauto(Sõiduk):
    def sõidu_maksumus(self, teepikkus):
        return round(((teepikkus*float(self.kytuse_kulu))/100)*1.9, 1)
    
    def hobujõud(self):
        print("Sõiduautol on 180 hobujõudu")
        

class Mootorratas(Sõiduk):
    def sõidu_maksumus(self, teepikkus):
        return round(((teepikkus*float(self.kytuse_kulu))/100)*1.85, 1)
    
    def hobujõud(self):
        print("Mootorrattal on 85 hobujõudu")
        

class Garaaž(Sõiduk):
    def __init__(self, autode_jrj):
        self.autode_jrj = autode_jrj
            
        
    def kuva(self):
        for i in self.autode_jrj:
            print(i.__str__())
            i.hobujõud()
            print(i.sõidu_maksumus(186))
        


with open("sõidukid.txt") as f:
    sisu = f.read().strip().split("\n")


soidukite_jrj = []
for i in sisu:
    tyyp = i.split(" - ")[0]
    mark, hind, kulu = i.split(" - ")[1].split(",")
 
    if tyyp == "Veoauto":
        soidukite_jrj.append(Veoauto(mark, hind, kulu))
    
    elif tyyp == "Sõiduauto":
        soidukite_jrj.append(Sõiduauto(mark, hind, kulu))
        
    elif tyyp == "Mootorratas":
        soidukite_jrj.append(Mootorratas(mark, hind, kulu))

lisa = Garaaž(soidukite_jrj)
lisa.kuva()


    
    
    
    
    
    
    
    
    
    
    