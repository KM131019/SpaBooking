import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestTC5:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize(
        "account",
        [
            "koko",
            "koko@gmail.com"
        ]
    )
    def test_tC5(self, account):
        driver = self.driver
        driver.get("https://chimmymeowspa.com/")

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-item-492 .menu-text"))).click()

        self.wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(account)
        driver.find_element(By.ID, "password").send_keys("Quoc@")

        driver.find_element(By.NAME, "login").click()

        error = self.wait.until(EC.visibility_of_element_located((By.ID, "user-registration")))
        assert error.is_displayed()