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
# import file đọc email
from utils.read_email import get_reset_link

class TestTC4():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC4(self):
    self.driver.get("https://chimmymeowspa.com//")
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-492 .menu-text").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Quên mật khẩu?").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "user_login").send_keys("mymy")
    self.driver.find_element(By.CSS_SELECTOR, ".user-registration-Button").click()
    time.sleep(3)
    elements = self.driver.find_elements(By.CSS_SELECTOR, "#user-registration .user-registration-message")
    assert len(elements) > 0
    time.sleep(3)

    # LẤY LINK RESET TỪ EMAIL IMAP
    reset_link = get_reset_link(
      gmail="tmy4840@gmail.com",
      app_password="guhk zfrl qiep bins"
    )
    print("Link reset:")
    print(reset_link)
    assert reset_link is not None
    # MỞ LINK RESET
    self.driver.get(reset_link)
    wait = WebDriverWait(self.driver,70)

    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#password_1"))).send_keys("")
    self.driver.find_element(By.CSS_SELECTOR, "#password_2").send_keys("Tuan1997Phac1995@")
    self.driver.find_element(By.CSS_SELECTOR, ".user-registration-Button").click()
    time.sleep(3)
    elements = self.driver.find_elements(By.CSS_SELECTOR, "#ur-frontend-form > form")
    assert len(elements) > 0