import requests

def coletar_dados():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    return response.json()