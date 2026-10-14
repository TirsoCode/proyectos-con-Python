import requests 
respuesta=requests.get("https://www.google.com")
print(respuesta.status_code)