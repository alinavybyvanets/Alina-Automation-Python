import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)
if response.status_code != 200:
    print("Помилка запиту:", response.status_code)
    exit()
photos = response.json().get('photos', [])
for i, photo in enumerate(photos[:2]):
    image_url = photo['img_src']
    print(f"Завантаження фото {i+1}:{image_url}")

    image_response = requests.get(image_url)

    filename = f"mars_photo{i+1}.jpg"
    with open(filename, 'wb') as file:
        file.write(image_response.content)
    print(f'Збережено як {filename}')