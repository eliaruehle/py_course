

class Bankkonto:

    vorname:str
    nachname:str 
    vermoegen:str

    def __init__(self, vorname:str, nachname:str, vermoegen:float, aktiv=True):
        self.vorname = vorname
        self.nachname = nachname
        self.vermoegen = vermoegen
        self.aktiv = aktiv

    def __str__(self):
        return "Name: " + self.vorname + " " + self.nachname + " Kontostand: " + str(self.vermoegen)

    def get_name(self):
        return self.vorname + " " + self.nachname

    def get_kontostand(self):
        return self.vermoegen
    
    def einzahlung(self, amount:float):
        if not self.aktiv:
            print("Das Konto ist nicht aktiv")
            return
        if amount <= 0:
            print("Fehler in Einzahlung")
        elif amount >= 15000.0: 
            self.vermoegen += 0.99*amount
        else:
            self.vermoegen += amount
    
    def auszahlung(self, amount:float):
        if not self.aktiv:
            print("Das Konto ist nicht aktiv")
            return
        if amount <= 0:
            print("Fehler bei der Auszahlung")
        elif self.vermoegen - amount < 0: 
            print("Nicht genügend Geld vorhanden")
        else:
            self.vermoegen -= amount
    
    def aktivieren(self):
        if self.aktiv:
            return 
        else:
            self.aktiv = True
            # self.aktiv = !self.aktiv
    
    def deaktivieren(self):
        if not self.aktiv:
            return 
        else:
            self.aktiv = False

        
    
konto = Bankkonto("Uwe", "Aßmann", 5000.50)
konto.deaktivieren()
konto.einzahlung(500)
konto.aktivieren()
konto.einzahlung(500)
print(konto.get_kontostand())