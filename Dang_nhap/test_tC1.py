import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTC1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
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