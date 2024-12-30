def gerador():
    i = 0
    while True:
        yield i
        i += 1

g = gerador()  
     
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3
print(next(g)) # 4
print(next(g)) # 5
print(next(g)) # 6


