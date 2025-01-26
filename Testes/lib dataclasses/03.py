from dataclasses import dataclass, field

@dataclass
class ItemStorage:
    nome: str
    stock: int = field(default=0) # o valor padrão sera 0
    sub_items: list[int] = field(default_factory=list) # defini que os valores seram mutaveis(listas e dicionarios)
    
    