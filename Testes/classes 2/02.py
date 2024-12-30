#Problema do diamante

class ObjetoA:
    def metodo(self):
        print("Estou na classe A")

class ObjetoB(ObjetoA):
    def metodo(self):
        print("Estou na classe B")

class ObjetoC(ObjetoA):
    def metodo(self):
        print("Estou na classe C")

class ObjetoD(ObjetoB, ObjetoC):
    pass
        
o = ObjetoD()

o.metodo() # ele printa o metodo da classe B

#help(o) # mostra a ordem da herança