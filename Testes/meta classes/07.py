class MetaClasse(type):
    def __new__(cls, name, bases, dct):
        if "soma" not in dct:
            raise TypeError(f"A classe {name} deve ter o metodo calcular")
        
        return super().__new__(cls, name, bases, dct)
    
class Calculadora(metaclass = MetaClasse):
    @staticmethod
    def soma(x, y):
        print(x + y)
        
class Calculadora2(metaclass = MetaClasse):
    pass

c = Calculadora()
c2 = Calculadora2() # vai gerar um erro

