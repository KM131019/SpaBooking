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
  
  def test_tC1(self):
    self.driver.get("https://chimmymeowspa.com//")
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-492 .menu-text").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "username").send_keys("chimchim")
    self.driver.find_element(By.ID, "password").send_keys("Quoc1997Man1995@")
    self.driver.find_element(By.NAME, "login").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Edit Profile").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "user_registration_user_email").clear()
    self.driver.find_element(By.ID, "user_registration_user_email").send_keys("chimmy@gmail.com")
    self.driver.find_element(By.NAME, "save_account_details").click()
    time.sleep(3)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".user-registration-message")
    assert len(elements) > 0
  
