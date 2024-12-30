class ItemError(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self):
        return f"Erro na criação do item: {self.error_message}"
    
class ItemDependences(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        print(args, kwargs)
        if kwargs["is_equipable"] and not "atributs" in kwargs:
            raise ItemError("Um item que é equipavel precisa ter atributos")

        return instance

class Item(metaclass = ItemDependences):
    def __init__(self, name: str, description: str, price: float = 1.0, is_equipable: bool = False, atributs: dict = {}) -> None:        
        self.name = name
        self.description = description
        self.price = price
        
        if atributs:
            is_equipable = True
            
        if is_equipable:
            self.atributs = atributs
            
            
espada = Item("espada", "Uma simples espada de ferro", is_equipable=True)

