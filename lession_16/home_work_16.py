import requests
from pathlib import Path

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

download_folder = Path('C:\\Users\\User\\PycharmProjects\\AQA-Python-Hillel\\lession_16\\mars_photos')
download_folder.mkdir(parents=True, exist_ok=True)

response = requests.get(url, params=params)

if response.status_code == 200:
    try:
        data = response.json()
        photos = data.get('photos', [])
        if photos:
            for index, photo in enumerate(photos[:5], start=1):
                image_url = photo['img_src']
                image_response = requests.get(image_url)

                if image_response.status_code == 200:
                    file_name = f"mars_photo{index}.jpg"
                    file_path = download_folder / file_name

                    with file_path.open('wb') as image_file:
                        image_file.write(image_response.content)

                    print(f"Фото сохранено в {file_name}")
                else:
                    print(f"Ошибка при загрузке {index}: {image_url}")
        else:
            print("Фото не найдено")
    except ValueError as result:
        print(f"Ошибка при парсинге JSON: {result}")
else:
    print(f"Ошибка: {response.status_code}")

