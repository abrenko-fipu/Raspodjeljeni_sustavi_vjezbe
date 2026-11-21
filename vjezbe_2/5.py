import asyncio
import time

osjetljivi_podaci=[
    {'prezime': 'Horvat', 'broj_kartice': '4532015112830366', 'CVV': '123'},
    {'prezime': 'Kovač', 'broj_kartice': '5425233430109903', 'CVV': '456'},
    {'prezime': 'Babić', 'broj_kartice': '4916338506082832', 'CVV': '789'},
]


async def secure_data(podaci):
    prezime=podaci["prezime"]
    broj_kartice=podaci["broj_kartice"]
    cvv=podaci["CVV"]

    e_broj_kartice=hash(broj_kartice)
    e_cvv=hash(cvv)

    await asyncio.sleep(3)

    return {"prezime":prezime,"broj_kartice":e_broj_kartice,"CVV":e_cvv}

async def main():
    tasks=[secure_data(podaci) for podaci in osjetljivi_podaci]
    return await asyncio.gather(*tasks)

pocetak=time.time()

print(asyncio.run(main()))

print(f"Trajanje: {(time.time()-pocetak):.2f}")





#print(f"'prezime': {prezime}, 'broj_kartice': {e_broj_kartice}, 'CVV':{e_cvv}")