# exemplo de singleton

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs): # call é usado para garantir que só uma instancia será criada
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs) # contrutor
            
        print(cls._instances) # printa todas as instancias
        
        return cls._instances[cls] # retona a instancia se ela ja existir
            
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.__smogon = 1
    
    @property
    def smogon(self):
        return self.__smogon
    
    @smogon.setter
    def smogon(self, new_smogon):
        self.__smogon = new_smogon
    

class test(metaclass=SingletonMeta):
    pass

s = Singleton()
a = test()
b = Singleton()
c = Singleton()

b.smogon = 2

print(s.smogon)
print(b.smogon)

s.smogon = 3

print(s.smogon)
print(b.smogon)
print(c.smogon)

# Percebe-se que as instancias estão "conectadas" pois o singleton só suporta apenas uma instancia