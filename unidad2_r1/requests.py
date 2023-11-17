'''
Cristopher Lopez Jimenez 
Gir0541
'''
import requests

while True:
    numero = input("Ingresar un año (q para salir): ")

    if numero.lower() == "q":
        print("Adiós")
        break

    url = f"https://numbersapi.p.rapidapi.com/{numero}/year"

    querystring = {"json": "true", "fragment": "true"}

    headers = {
        "X-RapidAPI-Key": "6584bddea8msh4c57f51bac25061p138a58jsn9d319332199d",
        "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
    }

    respuesta = requests.get (url, headers=headers, params=querystring)

    if respuesta.status_code == 200:
        datos_json = respuesta.json()
        fragmento = datos_json["text"]
        print(f"Datos interesantes sobre ese año {numero}: {fragmento}")
    else:
        print("Hubo un error con la llamada a la API.")
