import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def pocetna():
    return {"poruka": "Ok 200 :)"}

@app.get("/api/vrijeme_Pula")
def dohvati_vrijeme():
    url = "https://api.open-meteo.com/v1/forecast"

    parametri = {
        "latitude": 44.87,
        "longitude": 13.85,
        "current": "temperature_2m,wind_speed_10m"
    }

    odgovor = requests.get(url, params=parametri).json()['current']

    temp= odgovor["temperature_2m"]
    wind= odgovor["wind_speed_10m"]

    return [temp, wind]


