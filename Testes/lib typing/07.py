from typing import ClassVar

class Pessoa:
    raca: ClassVar[str] = "Humano"
    vivo: bool
    
    def morrer(self) -> None:
        self.vivo = False
        
        
    