'''
Cristopher López Jiménez 
GIR0541
key: c470b1851cmshed028756f3fdb29p16695ejsn3b18a2974294
'''
import http.client

while True:
    
    api_key = input("Ingresa tu clave de la API (o 'exit' para salir): ").strip()

    if api_key.lower() == 'exit':
        break

    if not api_key:
        print("Error: Debes ingresar una clave de API.")
        continue

    conn = http.client.HTTPSConnection("jokes-by-api-ninjas.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': "jokes-by-api-ninjas.p.rapidapi.com"
    }

    conn.request("GET", "/v1/jokes", headers=headers)

    res = conn.getresponse()
    data = res.read()

    if res.status == 200:
        print("Respuesta de la API:")
        print(data.decode("utf-8"))
    else:
        print(f"Error en la solicitud. Código de estado: {res.status}")

    conn.close()

print("¡Hasta luego!")


