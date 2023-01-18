class Kandidaat:
    def __init__(self, nimi, h_arv):
        self.nimi = nimi
        self.häälete_arv = h_arv
    
    def lisa_hääl(self):
        self.häälete_arv += 1
    
    
class Valija:
    def __init__(self, kandidaat_isend):
        kandidaat_isend.lisa_hääl()
        
           
hääletused  = {"Kaja": ["Jaanus", "Maarja", "Siim", "Ain"], "Jüri": ["Urve", "Jaanus", "Maarja"], "Martin": ["Ain", "Siim"]}

häälete_dict = {}

for kandidaat, valijad in hääletused.items():
    kandidaadi_isend = Kandidaat(kandidaat, 0)
    for valija in valijad:
        valija_isend = Valija(kandidaadi_isend)
      
    häälete_dict[kandidaadi_isend.häälete_arv] = [kandidaadi_isend.nimi]
    print(kandidaadi_isend.nimi, int(kandidaadi_isend.häälete_arv), "häält")
    
võitja = sorted(häälete_dict, reverse=True)

print("Võitja on", "".join(häälete_dict[võitja[0]]), "kes sai", võitja[0], "häält")

