import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTC5():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
  
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
    self.driver.get("https://chimmymeowspa.com//")
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-492 .menu-text").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "username").send_keys(account)
    self.driver.find_element(By.ID, "password").send_keys("")
    self.driver.find_element(By.NAME, "login").click()
    time.sleep(3)
    elements = self.driver.find_elements(By.ID, "user-registration")
    assert len(elements) > 0