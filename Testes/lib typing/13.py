from typing import Coroutine
import asyncio

async def coroutina() -> Coroutine[None, None, int]:
    await asyncio.sleep(1)
    
    return 12

async def main():
    print(await coroutina())
    
asyncio.run(main())