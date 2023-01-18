class Tont:
    def __init__(self, nimi, vanus, elukoht):
        self.nimi = nimi
        self.vanu = int(vanus)
        self.elukoht = elukoht
    
    def kummita(self):
        print(f"{self.nimi} kummitab elukohas {self.elukoht}!")
        
    def __str__(self):
        return f"Nimi: {self.nimi}, vanus: {self.vanu}, elukoht: {self.elukoht}"
    
    
class Võlur(Tont):
    def nõiu(self, isend):
        print(f"{isend.nimi} pani nõudise, millega sai pihta {self.nimi}!")
        


n = Tont("Norbert", 31, "Tartu")
h = Võlur("Harry", 17, "Tartu")
s = Võlur("Snape", 35, "Tartu")

print(n.__str__())
n.kummita()
print(h.__str__())
print(s.__str__())
s.nõiu(h)