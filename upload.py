import requests
import os

api_key = os.environ.get('API_KEY')

if api_key is None:
    print("No se encontró la API key en las variables de entorno.")
    exit()

file_path = input("Introduce la ruta del archivo PDF: ")

files = [
    ('file', ('file', open(file_path, 'rb'), 'application/octet-stream'))
]
headers = {
    'x-api-key': api_key
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)

