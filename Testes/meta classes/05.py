class MinhaMetaClass(type):
    def __new__(cls, name, bases, dct):
        
        dct["smogon"] = 1 
        
        return super().__new__(cls, name, bases, dct)
    
class Calculadora(metaclass= MinhaMetaClass):
    pass


print(Calculadora.__dict__) # smogon esta la