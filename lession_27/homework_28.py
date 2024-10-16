from time import sleep
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Chrome_package.base_page import BasePageClass


class NovaPoshtaTrackingPage(BasePageClass):

    def open_link_and_enter_number(self):
        """Открывает страницу и вводит номер посылки."""
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

        input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='en' and @placeholder='Номер посилки']"))
        )
        input_field.send_keys("20451016269790")
        button_find = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@class='track__form-group-btn green-active']"))
        )
        # Выполните клик с помощью JavaScript
        self.driver.execute_script("arguments[0].click();", button_find)
        sleep(5)

    def check_and_click_button(self):
        """Проверяет и кликает по кнопке 'Добре'."""
        try:
            # Ожидаем, пока кнопка станет кликабельной
            button_great = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Добре')]"))
            )
            action = ActionChains(self.driver)
            action.move_to_element(button_great).perform()
            # Если кнопка найдена и кликабельна, выполняем клик
            self.driver.execute_script("arguments[0].click();", button_great)
            sleep(5)
            print("Кнопка 'Добре' найдена и кликнута.")

        except TimeoutException:
            # Если кнопка не найдена в течение 10 секунд
            print("Кнопка 'Добре' не отображается, продолжаем тест.")

    def get_parcel_status(self):
        """Получает статус посылки и возвращает его."""
        try:
            # Ожидаем, пока статус посылки станет видимым
            status_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='header__status-text']"))
            )
            status_text = status_element.text
            print(f"Статус посылки: {status_text}")
            return status_text
        except TimeoutException:
            print("Не удалось получить статус посылки.")
            return None








