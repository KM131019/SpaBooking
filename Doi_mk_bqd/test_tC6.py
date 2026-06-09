import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTC6():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_tC6(self):
    self.driver.get("https://chimmymeowspa.com//")
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-492 .menu-text").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "username").send_keys("mimi")
    self.driver.find_element(By.ID, "password").send_keys("Tuan1997Phac1995@")
    self.driver.find_element(By.NAME, "login").click()
    time.sleep(3)
    assert self.driver.title == "Tài khoản -"
    self.driver.find_element(By.LINK_TEXT, "Change Password").click()
    self.driver.find_element(By.ID, "password_current").send_keys("Tuan1997Phac1995@")
    self.driver.find_element(By.ID, "password_1").send_keys("Quoc1997Man1995@")
    self.driver.find_element(By.ID, "password_2").send_keys("")
    self.driver.find_element(By.NAME, "save_change_password").click()
    time.sleep(3)
    elements = self.driver.find_elements(By.ID, "user-registration")
    assert len(elements) > 0