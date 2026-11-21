#simuliramo realni proces povezivanja s vanjskim računalom

import asyncio #Uvozimo biblioteku koja nam omogućava istovremeno izvođenje operacija

async def timer(name, delay): #definiramo asinkronu funkciju tajmer s parametrima ime i odgoda
    for i in range(delay, 0, -1): #inicijaliziramo petlju koja iterira kroz vrijednosi od 0 do zadanog broja sekundi odgode
        print(f'{name}: {i} sekundi preostalo...') #ispisujemo koliko je sekundi preostalo do kraja procesa
        await asyncio.sleep(1) # odgoda od 1 sekunde
    print(f'{name}: Vrijeme je isteklo!') #ispisujemo da je proces došao do kraja

async def main(): #definiramo glavnu funkciju kojom ćemo pokrenuti ostale funkcije u skripti (oblikujemo arhitekturu procesa)
    timers = [ #definiramo sadatke koje cemo staviti u raspored za istovremeno izvođenje (scheduling)
        asyncio.create_task(timer('Timer 1', 3)), #schedulamo funkciju tajmer u trajanju od 3 sekunde
        asyncio.create_task(timer('Timer 2', 5)), #schedulamo funkciju tajmer u trajanju od 5 sekundi
        asyncio.create_task(timer('Timer 3', 7)) #schedulamo funkciju tajmer u trajanju od 7 sekundi
        ]
    await asyncio.gather(*timers) #pokrećemo asinkrone funkcije istvremeno


asyncio.run(main()) #pokrećemo glavnu funkciju