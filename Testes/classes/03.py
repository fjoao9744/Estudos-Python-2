# __slots__

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade
        
class PessoaSlots:
    __slots__ = ["nome", "idade"] # Define quais atributos a classe pode ter
    
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
from sys import getsizeof

p1 = Pessoa("João", 30)
p2 = PessoaSlots("João", 30)

print(f"Tamanho de Pessoa: {getsizeof(p1.__dict__)} bytes")  # Usa dicionário interno
print(f"Tamanho de PessoaSlots: {getsizeof(p2)} bytes")  # Sem dicionário interno(o __slots__ elimina ele)