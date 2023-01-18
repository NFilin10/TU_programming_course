class Lennuk:
    def __init__(self, lennuki_nimi, maht, kesk_kiirus, kulu):
        self.nimi = lennuki_nimi
        self.reisijate_arv = maht
        self.keskmine_kiirus = kesk_kiirus
        self.kütusekulu = kulu
    

class Reis:
    def __init__(self, lennuk, sihtkoht, pikkus, pileteid):
        self.lendav_lennuk = lennuk
        self.reisi_sihtkoht = sihtkoht
        self.reisi_pikkus = pikkus
        self.ostetud_piletid = pileteid
        
    def reisi_kestvus(self):
        tunde = self.reisi_pikkus / self.lendav_lennuk.keskmine_kiirus
        return int(round(tunde * 60, 0))
    
    def vabu_kohti(self):
        return self.lendav_lennuk.reisijate_arv - self.ostetud_piletid
    
    
    def osta_pilet(self):
        if self.vabu_kohti() > 0:
            self.ostetud_piletid += 1
            print("Pilet ostetud")
        else:
            print("Lend on välja müüdud")
    
    
    def reisi_kütusekulu(self):
        return int(round(self.lendav_lennuk.kütusekulu * self.ostetud_piletid * self.reisi_pikkus / 100, 0))
        
    
lennuk = Lennuk("Boeing-767", 123, 800, 4)
reis = Reis(lennuk, "Madrid", 3500, 110)

print("Reisi kestvus on", reis.reisi_kestvus(), "minutit")
print("Vabade kohtade arv reisile sihtkohta Madrid on", str(reis.vabu_kohti()), ".")
reis.osta_pilet()
print("Vabade kohtade arv reisile sihtkohta Madrid on", str(reis.vabu_kohti()), ".")
print("Kütusekulu lendamiseks sihtkohta", reis.reisi_sihtkoht, "on", reis.reisi_kütusekulu(), "liitrit.")

