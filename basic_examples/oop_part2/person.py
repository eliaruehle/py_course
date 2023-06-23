
class Person:

    def __init__(self, forename:str, surename:str, age:int, gender:str) -> None:
        self.forename = forename
        self.surename = surename
        self.age = age
        self.gender = gender
        self.mail = ""
    
    def __str__(self) -> str:
        return f"{self.forename} {self.surename}"
    
    def get_age(self) -> int:
        return self.age
    
    def get_gender(self) -> str:
        return self.gender
    
    def set_gender(self, gender:str):
        self.gender = gender
    
    def set_age(self, age:int):
        self.age = age
    
    def register_mail(self, mail:str):
        if "@" in mail:
            self.mail = mail
        else:
            print("Wrong mail format!")
    
    def get_mail(self) -> str:
        if self.mail == "":
            print("No mail registered!")
        else: 
            return self.mail
    
    def has_birthday(self):
        self.age += 1