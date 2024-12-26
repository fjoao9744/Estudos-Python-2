class MinhaClasse:
    pass

print(type(MinhaClasse))

#class Pessoa:
    #nome = joão


Pessoa = type("Pessoa", (object,), {"nome" : "João"})

print(type(Pessoa))
