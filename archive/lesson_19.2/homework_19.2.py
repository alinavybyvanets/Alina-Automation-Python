import requests

image_path = "example.png"
server_url = "http://127.0.0.1:8080"

with open(image_path, "rb") as image_file:
    files = {"image": image_file}
    response = requests.post(f"{server_url}/upload", files=files)
print("Upload:", response.json())
if response.status_code == 201:
    image_url = response.json()["image_url"]
    filename = image_url.split("/")[-1]
else:
    exit("Помилка завантаження")

headers = {"Content-Type": "text"}
response = requests.get(f"{server_url}/image/{filename}", headers=headers)
print("Get:", response.status_code, response.json())

response = requests.delete(f"{server_url}/delete/{filename}")
print("Delete:", response.status_code, response.json())

