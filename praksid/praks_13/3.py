class Mari:
    def __init__(self, marja_nimetus, kogus):
        self.marja_nimetus = marja_nimetus
        self.kogus = kogus
    
    def __str__(self):
        return f"{self.marja_nimetus} - {self.kogus}"
    
    
class Maaskas(Mari):
    def maksumus(self, kogus):
        return round(kogus/1000*9, 2)

    def mitu_marja(self, kogus):
        return int((kogus/1000)*125)


class Mustikas(Mari):
    def maksumus(self, kogus):
        return round(kogus/1000*12, 2)

    def mitu_marja(self, kogus):
        return int((kogus/1000)*425)
    

class Vaarikas(Mari):
    def maksumus(self, kogus):
        return round(kogus/1000*11, 2)

    def mitu_marja(self, kogus):
        return int((kogus/1000)*260)
    

class Marjapood:
    def __init__(self, marjade_jrj):
        self.marjade_jrj = marjade_jrj
    
    def pood(self):
        print("Tere tulemast marjapoodi!/nPoes on olemas järgmised marjad:\nMaasikas - 10 kg\nMustikas - 7 kg\nVaarikas - 4.5 kg\n-------------")
        print("Saad anda järgmisi käske:\nK - kuva poes olevad marjad ja nende kogused\nO <marja_nimi> <kogus_grammides> - osta marju kindlas koguses\nL - lahku poest")
        eelarve = float(input("Mitu eurot sul on? "))
        print("-------------")
        while True:
            print(f"Raha jääk {eelarve} eurot.")
            käsk = input("Sisesta käsk: ")
            
            if käsk == "K":
                for i in self.marjade_jrj:
                    print(i)
            
            elif käsk == "L":
                print("Nägemist!")
                break
            
            else:
                try:
                    checker = False  
                    kask, mari, kogus = käsk.split()
                    mari = mari.capitalize()
                    kogus = float(kogus)
                    for i in self.marjade_jrj:
                        if mari == i.marja_nimetus:
                            checker = True 
                            maksmus = i.maksumus(kogus)
                            if kogus/1000 > i.kogus:
                                print(f"Seda marja ({mari}) poes nii palju ei ole.")
                                print("-------------")
                            elif maksmus > eelarve:
                                print("Sul pole piisavalt raha!")
                                print("-------------")
                            else:
                                print(f"Vaarikas läks sulle maksma {maksmus} eurot ja kokku said {i.mitu_marja(kogus)} marja.")
                                eelarve -= maksmus
                                i.kogus -= kogus/1000
                           
     
                    if not checker:                           
                        print("Sellist marja poes ei ole!")
                        print("-------------")
                        
                    
                           
                            
                except Exception as e:
                    print(e)
                    print("Sisestasid liiga palju/vähe andmeid")
                    continue 
                






maasikas = Maaskas("Maasikas", float(10))
mustikas = Mustikas("Mustikas", float(7))
vaarikas = Vaarikas("Vaarikas", float(4.5))

marjad = [maasikas, mustikas, vaarikas]


pood = Marjapood(marjad)

pood.pood()
    


        
        
    