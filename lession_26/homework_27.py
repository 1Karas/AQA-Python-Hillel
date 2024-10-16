from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePageClass


class Frame(BasePageClass):

    def iframe_check(self):
        try:
            self.driver.get("http://localhost:8000/dz.html")

            self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[src='dz_frame1.html']"))
            input_field1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "input1"))
            )
            input_field1.send_keys("Frame1_Secret")
            verify_button = self.driver.find_element(By.XPATH,
                                                     "//button[contains(@onclick, \"verifyInput('input1')\")]")
            verify_button.click()
            sleep(5)

            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            assert alert_text == "Верифікація пройшла успішно!", "Текст верифікації не збігся для першого фрейма"
            print("Перший фрейм: Верифікація пройшла успішно!")
            alert.accept()
            sleep(5)

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[src='dz_frame2.html']"))
            input_field2 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "input2"))
            )
            input_field2.send_keys("Frame2_Secret")
            verify_button1 = self.driver.find_element(By.XPATH,
                                                     "//button[contains(@onclick, \"verifyInput('input2')\")]")
            verify_button1.click()
            sleep(5)
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            assert alert_text == "Верифікація пройшла успішно!", "Текст верифікації не збігся для другого фрейма"
            print("Другий фрейм: Верифікація пройшла успішно!")
            alert.accept()

        finally:
            self.driver.quit()

if __name__ == "__main__":
    frame_test = Frame()
    frame_test.iframe_check()
