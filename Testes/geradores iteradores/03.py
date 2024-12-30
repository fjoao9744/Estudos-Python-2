def gerador():
    variavel = "valor 1"
    yield variavel # retorna e pausa
    variavel = "valor 2"
    yield variavel # retorna e pausa
    variavel = "valor 3"
    yield variavel # retorna e pausa 
    variavel = "valor 4"
    yield variavel # retorna e pausa

g = gerador()
print(next(g)) # valor 1
print(next(g)) # valor 2
print(next(g)) # valor 3
print(next(g)) # valor 4


