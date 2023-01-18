from random import *

class Inimene:
    def __init__(self, vanus, kuupalk):
        self.vanus = vanus
        self.kuupalk = kuupalk
        

class Hoone:
    def __init__(self, tyyp, kogupind, elanikud):
        self.tyyp = tyyp
        self.kogupind = kogupind
        self.elanikud = elanikud
    
    def __str__(self):
        return f"Hoone tüüp on: {self.tyyp}\nHoone kogupind on: {self.kogupind}\nHoones elab: {len(self.elanikud)} elanikku"
    
    def keskmine_vanus(self):
        vanused = []
        for elanik in self.elanikud:
            vanused.append(elanik.vanus)
        
        return round(sum(vanused) / len(vanused), 0)
    
    def keskmine_palk(self):
        palgad = []
        
        for elanik in self.elanikud:
            palgad.append(elanik.kuupalk)
        
        return round(sum(palgad) / len(palgad), 1)
    
    
class Eramaja(Hoone):
    def __init__(self, kogupind, elanikud):
        super().__init__('Eramaja', kogupind, elanikud)
    def ruutmeetri_hind(self):
        return 500000 / self.kogupind
    
    def elanikke_korrusel(self):
        return len(self.elanikud) / 1


class Kortermaja(Hoone):
    def __init__(self, kogupind, elanikud):
        super().__init__('Kortermaja', kogupind, elanikud)
    def ruutmeetri_hind(self):
        return 5000000 / self.kogupind
    
    def elanikke_korrusel(self):
        return len(self.elanikud) / 9
    
 
class Ridaelamu(Hoone):
    def __init__(self, kogupind, elanikud):
        super().__init__('Ridaelamu', kogupind, elanikud)
    def ruutmeetri_hind(self):
        return 3000000 / self.kogupind
    
    def elanikke_korrusel(self):
        return len(self.elanikud) / 2


class Hotell(Hoone):
    def __init__(self, kogupind, elanikud):
        super().__init__('Hotell', kogupind, elanikud)
    def ruutmeetri_hind(self):
        return 10000000 / self.kogupind
    
    def elanikke_korrusel(self):
        return len(self.elanikud) / 9



def elanikud(n):
    tagastatav = []
    for i in range(n):
        vanus = randint(0, 100)
        palk = randint(600, 6000)
        inimene = Inimene(vanus, palk)
        tagastatav.append(inimene)
    
    return tagastatav
        
    

era = Eramaja(200, elanikud(4))
rida = Ridaelamu(2000, elanikud(24))
korter = Kortermaja(2000, elanikud(100))
hotell = Hotell(6000, elanikud(300))


for hoone in [era, rida, korter, hotell]:
    print(hoone)
    print("Keskmine vanus on:", hoone.keskmine_vanus())
    print("Keskmine palk on:", hoone.keskmine_palk())
    print("Ruutmeetri hind on", hoone.ruutmeetri_hind())
    print("Elanikke korrusel on:", hoone.elanikke_korrusel())

    
    
    
    
    
    
    
    
    
    
    
    
        
        
        