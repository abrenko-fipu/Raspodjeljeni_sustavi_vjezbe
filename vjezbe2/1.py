import asyncio

async def korutina():
    lista_brojeva = [x for x in range(1, 11)]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni.")
    return lista_brojeva

asyncio.run(korutina())