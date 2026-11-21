import asyncio
import time


baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autentifikacija(korisnik) :

    kor_ime=korisnik['korisnicko_ime']
    kor_email=korisnik['email']
    kor_lozinka=korisnik['lozinka']

    aut = asyncio.create_task(autorizacija(korisnik, kor_lozinka))
    wait = asyncio.create_task(asyncio.sleep(3))

    naden = False

    for k in baza_korisnika:
        if (k['korisnicko_ime'],k['email']) == (kor_ime,kor_email):
            naden=True
            break

    await wait
    aut = await aut

    if not naden:
        print(f"Korisnik {kor_ime} nije pronađen.")
        return

    if aut==True:
        rezultat = f"Korisnik {kor_ime}: Autorizacija uspješna."
    else:
        rezultat = f"Korisnik {kor_ime}: Autorizacija neuspješna."

    print(rezultat)

async def autorizacija(korisnik,lozinka):
    aut=False
    for k in baza_lozinka:
        if k['korisnicko_ime']==korisnik["korisnicko_ime"]:
            if lozinka == k['lozinka']:
                aut = True
    await asyncio.sleep(2)
    return aut


async def main():
    await autentifikacija({'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka':'lozinka123'})


pocetak=time.time()

asyncio.run(main())

print(f"Trajanje: {(time.time()-pocetak):.2f}")