'''
Cristopher Lopez Jimenez 
Gir0541
'''
import requests

while True:

    ciudad = input("Nombre de ciudad (q para salir)")
    if ciudad.lower() == "q" :
        print("Adiós")
        break

    url = f"https://weatherapi-com.p.rapidapi.com/current.json?q={ciudad}"
    headers = {
        "X-RapidAPI-Key": "6584bddea8msh4c57f51bac25061p138a58jsn9d319332199d",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    respuesta = requests.get(url, headers=headers)
    datos_json = respuesta.json()
    estado_json = datos_json["current"]["condition"]["text"]
    if respuesta.status_code == 200:
        print(f"El clima en {ciudad} es {estado_json}")
    else:
        print("Hubo un error con la llamada a la API.")
