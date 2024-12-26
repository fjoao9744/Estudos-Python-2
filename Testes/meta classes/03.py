class MinhaMetaClass(type):
    def __new__(cls, name, bases, dct): 

        print(f"A classe {name} esta sendo criada")
        
        return super().__new__(cls, name, bases, dct)
    
class Pessoa(metaclass= MinhaMetaClass):
    pass

joao = Pessoa()

print(joao)
