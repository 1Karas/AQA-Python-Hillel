from lession_27.homework_28 import NovaPoshtaTrackingPage

def test_parcel_tracking():
    btn = NovaPoshtaTrackingPage()

    # Открываем страницу и вводим номер посылки
    btn.open_link_and_enter_number()

    # Кликаем на кнопку "Добре", если она присутствует
    btn.check_and_click_button()

    # Ожидаем получения статуса посылки
    actual_status = btn.get_parcel_status()

    # Ожидаемый статус посылки
    expected_status = "Отримана"

    # Проверка соответствия статуса
    assert actual_status == expected_status, f"Ожидался статус '{expected_status}', но получен '{actual_status}'"