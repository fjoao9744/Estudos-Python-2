from typing import AsyncGenerator
import asyncio

async def gerador() -> AsyncGenerator[int, None]:
    i: int = 0
    while True:
        yield i
        i += 1

async def main():        
    gen: AsyncGenerator = gerador()

    print(await anext(gen))
    print(await anext(gen))
    print(await anext(gen))
    print(await anext(gen))

asyncio.run(main())
