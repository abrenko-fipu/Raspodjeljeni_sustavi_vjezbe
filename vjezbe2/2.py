import asyncio
import time

rjecnik_korisnici={
    1: {"ime": "Ana", "prezime": "Horvat", "email": "ana@example.com", "dob": 25},
    2: {"ime": "Marko", "prezime": "Kovač", "email": "marko@example.com", "dob": 31},
    3: {"ime": "Ivana", "prezime": "Babić", "email": "ivana@example.com", "dob": 28},
}

rjecnik_proizvodi = {
    1: {"naziv": "Laptop", "cijena": 899.99, "kolicina": 12, "kategorija": "Elektronika"},
    2: {"naziv": "Miš", "cijena": 19.90, "kolicina": 55, "kategorija": "Oprema"},
    3: {"naziv": "Tipkovnica", "cijena": 49.50, "kolicina": 30, "kategorija": "Oprema"},
}
async def korisnici():
    podaci_o_korisnicima=rjecnik_korisnici
    await asyncio.sleep(3)
    return podaci_o_korisnicima


async def proizvodi():
    podaci_o_proizvodima = rjecnik_proizvodi
    await asyncio.sleep(5)
    return podaci_o_proizvodima

async def main():
    kor, pod= await asyncio.gather(korisnici(),proizvodi())

    for x in [kor,pod]:
        for y in x.values():
            print(y)

pocetak=time.time()

asyncio.run(main())

print(f"Trajanje: {(time.time()-pocetak):.2f}")