import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTC2():
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
  
  def test_tC2(self, account):
    self.driver.get("https://chimmymeowspa.com//")
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-492 .menu-text").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "username").send_keys(account)
    self.driver.find_element(By.ID, "password").send_keys("Quoc1997@")
    self.driver.find_element(By.ID, "rememberme").click()
    self.driver.find_element(By.NAME, "login").click()
    time.sleep(3)
    assert self.driver.title == "Tài khoản -"