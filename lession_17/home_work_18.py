import requests

# Адреса сервера
base_url = 'http://127.0.0.1:8080'

# Шлях до файлу зображення, яке потрібно завантажити
file_path = 'C:\\Users\\User\\PycharmProjects\\AQA-Python-Hillel\\lession_17\\uploads\\images.jpg'

upload_url = f"{base_url}/upload"
with open(file_path, 'rb') as image_file:
    files = {'image': image_file}
    response = requests.post(upload_url, files=files)

if response.status_code == 201:
    image_url = response.json()['image_url']
    print(f'Избражение загужено {image_url}')
else:
    print(f'Ошибка при загрузке {response.status_code}')
    exit()

filename = image_url.split('/')[-1]

get_image_url = f"{base_url}/image/{filename}"
headers = {"Content-Type":"text"}
response = requests.get(get_image_url, headers=headers)

if response.status_code == 200:
    print(f"Урл изображени: {response.json()['image_url']} ")
else:
    print(f"Ошибка при получении изображения: {response.status_code}")

delete_image_url = f"{base_url}/delete/{filename}"
response = requests.delete(delete_image_url)

if response.status_code == 200:
    print(f"Изображени {filename} удалено")
else:
    print(f"Ошибка при удалении {response.status_code}")