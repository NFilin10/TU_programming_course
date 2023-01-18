class Auto:
    def __init__(self, uus_mark, uus_labisoit, uus_kulu, uus_tyyp):
        self.mark = uus_mark
        self.labisoit = uus_labisoit
        self.kutusekulu = uus_kulu
        if uus_tyyp in ['bensiin', 'diisel']:
            self.kutusetyyp = uus_tyyp
        else:
            raise Exception("Kutusetyyp ei sobi")
    
    def kütuse_maksumus(self, teekonna_pikkus):
        if not str(teekonna_pikkus).isnumeric():
            raise Exception("Teekonna pikkus peab olema arv")
        if self.kutusetyyp == "bensiin":
            return teekonna_pikkus * self.kutusekulu / 100 * 1.9
        elif self.kutusetyyp == "diisel":
            return teekonna_pikkus * self.kutusekulu / 100 * 1.8
        

auto1 = Auto("Audi", 10000, 5, "bensiin")
auto2 = Auto("BMW", 30000, 7, "diisel")
print(auto1.kütuse_maksumus(100))
print(auto2.kütuse_maksumus(100))