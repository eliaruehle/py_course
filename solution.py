class Person:
    def __init__(self, name:str, alter:int, beziehungsstatus:str):
        self.name = name
        self.alter = alter
        self.beziehungsstatus = beziehungsstatus
        return
    
    def geburtstag (self):
        self.alter += 1
        
class Kind(Person):
    def __init__(self, name:str, alter:int, papa: Person):
        self.name = name
        self.alter = alter
        self.mittagsschlaf = self.check_alter(alter)
        self.papa = papa
        return
    
    def check_alter(self, alter:int):
        if alter < 5:
            return True
        else: 
            return False

    def geburtstag(self):
        self.alter+=1
        self.mittagsschlaf= self.check_alter(self.alter)

class Auto:
    def __init__(self,farbe : str, marke : str, baujahr: int, fahrer : Person):
        self.farbe = farbe
        self.marke = marke 
        self.baujahr = baujahr
        self.fahrer = fahrer
        return
    
    def umlackierung (self, farbe):
        self.farbe = farbe
        return
    
person1 = Person ("Elia", 21, "ledig" )

auto1 = Auto("grün", "Mercedes", 1990, person1)

print(type(auto1.fahrer),auto1.fahrer.name,person1.alter, auto1.farbe)

auto1.umlackierung("blau")
person1.geburtstag()

print(type(auto1.fahrer),auto1.fahrer.name,person1.alter, auto1.farbe)

kind1 = Kind("Mo", 4, person1)

print(kind1.papa.name + " ist der Vater von " + kind1.name)
print(kind1.name, kind1.mittagsschlaf)
kind1.geburtstag()

print(kind1.name, kind1.mittagsschlaf)