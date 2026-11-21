import asyncio
import time
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj%2==0:
        print(f"Broj {broj} je paran.")
    else:
        print(f"Broj {broj} je neparan.")

async def main():
    lista_brojeva=random.sample([x for x in range(100)],k=10)
    zadaci=[provjeri_parnost(broj) for broj in lista_brojeva]
    await asyncio.gather(*zadaci)

pocetak=time.time()

asyncio.run(main())

print(f"Trajanje: {(time.time()-pocetak):.2f}")