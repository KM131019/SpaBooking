import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestTC3:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_tC3(self):
        driver = self.driver
        driver.get("https://chimmymeowspa.com/")

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-item-492 .menu-text"))).click()

        self.wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("")
        driver.find_element(By.ID, "password").send_keys("Quoc1997@")

        driver.find_element(By.NAME, "login").click()

        error = self.wait.until(EC.visibility_of_element_located((By.ID, "user-registration")))
        assert error.is_displayed()