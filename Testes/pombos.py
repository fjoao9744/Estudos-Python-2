def pombos(Ncasas, Npombos):
    casas = [[] for c in range(Ncasas)]
    
    i = i2 = 0

    while i < Npombos:
        casas[i2].append(0)
        i2 += 1
        i += 1

        if i2 == len(casas):
            i2 = 0
        
    return casas

print(pombos(5, 25))
