import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTC1():
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
  
  def test_tC1(self, account):
    self.driver.get("https://chimmymeowspa.com//")
    print("Mở trang chủ")
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-492 .menu-text").click()
    print("Mở trang đăng nhập")
    time.sleep(3)
    self.driver.find_element(By.ID, "username").send_keys(account)
    self.driver.find_element(By.ID, "password").send_keys("Quoc1997@")
    print("Nhập tài khoản:", account)
    self.driver.find_element(By.NAME, "login").click()
    time.sleep(3)
    print("Title hiện tại:", self.driver.title)
    assert self.driver.title == "Tài khoản -"