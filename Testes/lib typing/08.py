from typing import Self

class ContaBancaria:
    saldo: float
    
    def depositar(self, dindin) -> Self:
        self.saldo += dindin
        
        return self
    
