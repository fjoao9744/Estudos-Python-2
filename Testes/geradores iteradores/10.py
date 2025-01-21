def gerador1():
    num = 0
    while True:
        yield num
        num += 1
        
def gerador2():
    num = 0
    while True:
        yield num
        num += 1
        
"""def gerador3(): # sem yeild from
    gen1 = gerador1()
    gen2 = gerador2()
    while True:
        yield next(gen1)
        yield next(gen2)"""
        
def gerador3(): # com yeild from
    while True:
        yield from gerador1()
        yield from gerador2()
        
gen = gerador3()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

    
