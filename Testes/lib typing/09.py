from typing import NewType
from dataclasses import dataclass

UserId = NewType('UserId', int)

@dataclass
class User:
    id: UserId
    nome: str
    idade: int
    
    
joao = User(UserId(123), "joao", 19)

print(joao)

