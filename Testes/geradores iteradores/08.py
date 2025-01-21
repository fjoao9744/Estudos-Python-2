def gerador():
    print("gerador inciado")
    while True:
        num = yield 
        print(f"valor recebido: {num}")
        
gen = gerador()
print(next(gen))

print(gen.send(5))
print(gen.send(10))
print(gen.send(15))

print(next(gen)) # retorna None pq esta dentro do while

