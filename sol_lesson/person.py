
class Person:

    def __init__(self, forename:str, surename:str, age:int, gender:str, mail=""):
        self.forename = forename
        self.surename = surename 
        self.age = age 
        self.gender = gender
        self.mail = mail
    
    def __str__(self):
        return f"{self.forename} {self.surename}"
    
    def get_age(self):
        return self.age
    
    def get_gender(self) -> int:
        return self.gender
    
    def set_age(self, new_age:int):
        self.age = new_age
    
    def set_gender(self, new_gender:str):
        self.gender = new_gender
    
    def register_mail(self, mail:str) -> None:
        # if "@" in mail:
        if mail.__contains__("@"):
            self.mail = mail
        else:
            print("Invalid mail!")
    
    def get_mail(self):
        #if bool(self.mail):
        if self.mail == "":
            print("No email!")
        else:
            return self.mail


if __name__ == "__main__":
    person = Person("Uwe", "Assmann", 50, "m")
    #print(person.get_age())
    #person.set_age(30)
    person.register_mail("test@test")
    print(person.get_mail())
    print(person.get_gender())