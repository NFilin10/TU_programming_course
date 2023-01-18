class Taluloom:
    def __init__(self, nimetus, kaal, vanus):
        self.nimetus = nimetus
        self.kaal = kaal
        self.vanus = vanus
        
    def toit(self):
        return round(self.kaal * 0.02, 1)
    
    def pesu(self):
        if self.vanus < 5:
            return 1
        elif self.vanus < 11:
            return 3
    
        else:
            return 5
        

class Hobune(Taluloom):
    def hääl(self):
        print("Hiii!")
        

class Siga(Taluloom):
    def hääl(self):
        print("Röh-röhh")
        

class Lammas(Taluloom):
    def hääl(self):
        print("Mää...")
        
        
hobune = Hobune("Hobune", 400, 11)
siga = Siga("Siga", 100, 17)
lammas = Lammas("Lammas", 57, 3)


hobune.hääl()
print(hobune.toit())
print(hobune.pesu())

siga.hääl()
print(siga.toit())
print(siga.pesu())

lammas.hääl()
print(lammas.toit())
print(lammas.pesu())






        
