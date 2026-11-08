async function ucitajVrijeme() {
  const adresa = "https://testni-web.onrender.com/api/vrijeme_Pula";

  const odgovor = await fetch(adresa);
  const vrijeme = await odgovor.json();

  const lista = document.getElementById("vrijeme");

  lista.innerHTML = "";

  const temperatura = vrijeme[0];
  const vjetar = vrijeme[1];

  const stavka_temp = document.createElement("li");
  stavka_temp.textContent = "Temperature: " + temperatura + " °C";

  const stavka_wind = document.createElement("li");
  stavka_wind.textContent = "Wind: " + vjetar + " km/h";

  lista.appendChild(stavka_temp);
  lista.appendChild(stavka_wind);
}

document.getElementById("btn").addEventListener("click", ucitajVrijeme);