def contador(maximo):
    num = 0
    while num < maximo:
        yield num
        num += 1    
for c in contador(5):
    print(c)
    
    