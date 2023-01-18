class Õun:
    def __init__(self, nimi, värv):
        self.nimi = nimi
        self.värv = värv
        
    def muuda_värvi(self, uus_värv):
        self.värv = uus_värv
        
    def kilohind(self):
        if self.värv == "roheline":
            return 0.79
        elif self.värv == "kollane":
            return 1.89
        if self.värv == "punane":
            return 2.49
        
    def __str__(self):
        return f"{self.nimi}, {self.värv}, {self.kilohind()} eurot"


class Kuldrenett(Õun):
    def __init__(self, värv, suurus):
        super().__init__("Kuldrenett", värv)
        self.suurus = suurus
        
    def kilohind(self):
        return round(self.suurus * 0.55, 2)
    
oun = Õun("Suislepp", "roheline")
print(f"Õuna kilohind on {oun.kilohind()}")
oun.muuda_värvi("punane")
print("Värv muutub...")
print(f"Õuna kilohind on {oun.kilohind()}")
kuld = Kuldrenett("kollane", 6.5)
print(kuld.__str__())


