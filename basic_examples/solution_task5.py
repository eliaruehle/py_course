class Bankkonto:

    # set class members for better readability
    vorname:str
    nachname:str
    kontostand:float
    aktiv:bool

    def __init__(self, vorname:str, nachname:str, vermoegen:float):
        self.vorname = vorname
        self.nachname = nachname
        self.kontostand = vermoegen
        self.aktiv = True
    
    def __str__(self):
        return f"Das ist das Bankkonto von {self.vorname} {self.nachname}."
    
    def inhaber_name(self):
        return self.vorname + " " + self.nachname

    def aktueller_kontostand(self):
        return self.kontostand
    
    def auszahlung(self, betrag:float) -> bool:
        if self.kontostand - betrag >= 0:
            self.kontostand -= betrag
            return True 
        else:
            print("Nicht genügend Geld vorhanden!")
            return False
    
    def einzahlung(self, betrag:float) -> bool:
        if betrag <= 0:
            raise ValueError("Einzahlungsbetrag zu niedrig!")
        if betrag >= 15000:
            betrag *= 0.99
        self.kontostand += betrag 

    def deaktivieren(self):
        if self.aktiv:
            self.aktiv = False
        else:
            print("Konto bereits inaktiv.")
        
    def aktivieren(self):
        if not self.aktiv:
            self.aktiv = True
        else:
            print("Konto bereits aktiv.")
    

    

    

if __name__ == "__main__":
    obj = Bankkonto("Elia", "Ruehle", 1000)
    print(obj)
    obj.einzahlung(1000)
    assert obj.aktueller_kontostand() == 2000.0
    obj.auszahlung(1500)
    assert obj.aktueller_kontostand() == 500.0
    obj.auszahlung(1000)