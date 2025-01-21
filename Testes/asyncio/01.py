import asyncio

async def rotina(tarefa, time):
    print(f"começando rotina {tarefa}")
    await asyncio.sleep(time)
    print(f"rotina {tarefa} acabou")
    
async def main():
    print("Começado o main")
    
    await asyncio.gather(
        rotina("rotina1", 3),
        rotina("rotina2", 1),
        rotina("rotina3", 2)
    )
    
    print("acabando o main")
    
asyncio.run(main())

