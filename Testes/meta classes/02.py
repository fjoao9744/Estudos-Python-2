
class MinhaMetaClass(type):
    def __new__(cls, name, bases, dct): # é obrigatorio ter esses 4 argumentos
        '''
        name = nome da classe criada a partir dessa metaclasse
        bases = são as classes base(por padrão é a object)
        dct = é o dicionario com funções e atributos da classe
        '''
        print(f"A classe {name} esta sendo criada")
        
        instancia = super().__new__(cls, name, bases, dct)
        return instancia
    
mt = MinhaMetaClass("joao", (object, ), {"nome":"joao"}) # é isso que uma classe passa automaticamente quando ela é criada

print(mt)
