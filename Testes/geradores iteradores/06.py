# gerador assincrono

import asyncio
async def gerador_async(n):
    for i in range(n):
        await asyncio.sleep(1)
        yield i

async def main():
    async for numero in gerador_async(5): # async for itera sobre um iterador assincrono
        print(numero)

asyncio.run(main())


