import requests
import sys

url = "http://127.0.0.1:8000/"

response = requests.get(url, stream=True)

if response.status_code == 200:
    for chunk in response.iter_content(decode_unicode=True):
        sys.stdout.write(chunk)
        sys.stdout.flush()  
else:
    print("Failed to fetch the stream. Status code:", response.status_code)
