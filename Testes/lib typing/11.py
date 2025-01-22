from typing import Generator

def gerador() -> Generator[int, None, int]:
    i = 0
    while True:
        yield i
        i += 1
        
gen = gerador()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
