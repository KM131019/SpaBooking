import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestTC8:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_tC8(self):
        driver = self.driver
        driver.get("https://chimmymeowspa.com/")

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-item-492 .menu-text"))).click()

        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Bạn chưa có tài khoản? Đăng ký ngay."))).click()

        self.wait.until(EC.visibility_of_element_located((By.ID, "user_login"))).send_keys(" tran van bay  ")
        driver.find_element(By.ID, "user_email").send_keys("BAY@gmail.com")
        driver.find_element(By.ID, "user_pass").send_keys("Bay130613@")
        driver.find_element(By.ID, "user_confirm_password").send_keys("Bay130613@")

        driver.find_element(By.CSS_SELECTOR, ".btn").click()

        # Verify lỗi Họ tên bắt buộc
        error = self.wait.until(EC.visibility_of_element_located((By.ID, "user_login-error")))
        assert error.is_displayed()