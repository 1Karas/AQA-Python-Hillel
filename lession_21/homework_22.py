import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("test_search.log"),
    logging.StreamHandler()
])

# URL для аутентификации и поиска автомобилей
BASE_URL = "http://127.0.0.1:8080"
AUTH_URL = f"{BASE_URL}/auth"
CARS_URL = f"{BASE_URL}/cars"


# Фикстура для аутентификации и получения токена, с scope='class'
@pytest.fixture(scope='class')
def auth_token():
    session = requests.Session()
    response = session.post(AUTH_URL, auth=HTTPBasicAuth('test_user', 'test_pass'))

    assert response.status_code == 200, "Аутентификация не прошла!"

    access_token = response.json().get('access_token')
    assert access_token, "Токен не был получен!"

    # Добавляем токен авторизации к заголовкам сессии
    session.headers.update({'Authorization': f'Bearer {access_token}'})
    return session


# Параметры для теста
test_data = [
    ('price', '5'),
    ('year', '10'),
    ('engine_volume', '3'),
    ('brand', '7'),
    (None, '4'),
    ('price', None),
    (None, None)
]


@pytest.mark.parametrize("sort_by, limit", test_data)
def test_search_cars(auth_token, sort_by, limit):
    # Формирование параметров запроса
    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    # Логирование запроса
    logging.info(f"Запрос с параметрами: sort_by={sort_by}, limit={limit}")

    # Отправка GET запроса на поиск автомобилей
    response = auth_token.get(CARS_URL, params=params)

    # Проверка статуса ответа
    assert response.status_code == 200, f"Ошибка при запросе: {response.status_code}"

    # Проверка данных в ответе
    cars = response.json()
    logging.info(f"Получено автомобилей: {len(cars)}")

    # Проверка на корректность данных
    assert isinstance(cars, list), "Ожидается, что результат будет списком автомобилей"
    if limit:
        assert len(cars) <= int(limit), f"Ожидаемое количество автомобилей не должно превышать {limit}"

    logging.info("Тест успешно завершен.\n")


