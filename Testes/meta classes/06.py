class MinhaMetaClass(type):
    def __new__(cls, name, bases, dct):
        
        dct["smogon"] = 1 # atributo da classe
        
        return super().__new__(cls, name, bases, dct)
    
class Person(metaclass= MinhaMetaClass):    
    def __init__(self):
        pass
    
p = Person()

print(Person.smogon) # smogon é um atributo da classe Person e não da instancia p