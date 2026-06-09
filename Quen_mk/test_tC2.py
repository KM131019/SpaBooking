import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTC2():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_tC2(self):
    self.driver.get("https://chimmymeowspa.com//")
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-492 .menu-text").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Quên mật khẩu?").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "user_login").send_keys("")
    self.driver.find_element(By.CSS_SELECTOR, ".user-registration-Button").click()
    time.sleep(3)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".user-registration-error")
    assert len(elements) > 0
  
