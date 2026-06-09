import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTC13():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_tC13(self):
    self.driver.get("https://chimmymeowspa.com//")
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-492 .menu-text").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Bạn chưa có tài khoản? Đăng ký ngay.").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "user_login").send_keys("Bay")
    self.driver.find_element(By.ID, "user_email").send_keys("BAY@gmail.com")
    self.driver.find_element(By.ID, "user_pass").send_keys("Bay7@")
    self.driver.find_element(By.ID, "user_confirm_password").send_keys("Bay7@")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(3)
    elements = self.driver.find_elements(By.ID, "user_pass-error")
    assert len(elements) > 0