# ESSE CODIGO NÃO ESTA FUNCIONANDO
# mas é interessante para analise

import types

class MinhaMetaClass(type):
    def __new__(cls, name, bases, dct):
        
        def soma(self, x, y):
            return x + y
        
        dct["soma"] = types.FunctionType(
            soma.__code__, # codigo da função
            globals(), # variaveis globais
            "soma", #nome da função
            soma.__defaults__, # argumento padrão
            soma.__closure__ # para acessar parametros fora do escopo da função
            )
        
        return super().__new__(cls, name, bases, dct)
    
class Calculadora(metaclass= MinhaMetaClass):
    pass
        
c = Calculadora()

print(c.soma(2, 3))