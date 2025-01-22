from typing import Awaitable
import asyncio

async def corotina() -> int:
    return 12

async def retorna_corotina() -> Awaitable[int]:
    return corotina()

async def main():
    print(await retorna_corotina())
    
asyncio.run(main())



