from typing import Union, Optional

def analisador_dados(dado: Union[int, str]) -> str:
    if isinstance(dado, int):
        return "É um numero"
    
    if isinstance(dado, str):
        return "É uma string"
    
    return "O valor não é nem um numero nem uma string"

def only_string(dado: Optional[str]) -> Union[str, bool]: # só aceita str ou None
    return dado or False

print(analisador_dados("smogon"))
print(analisador_dados(15))

print(only_string("smogon"))
print(only_string(None)) # Se 
