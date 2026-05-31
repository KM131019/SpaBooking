import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTC3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC3(self):
    wait = WebDriverWait(self.driver,20)
    self.driver.get("https://chimmymeowspa.com//")
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-23 .menu-text").click()
    time.sleep(3)

    element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập ngay")
    self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
    time.sleep(3)
    self.driver.execute_script("arguments[0].click();", element)

    time.sleep(3)
    self.driver.find_element(By.ID, "username").send_keys("mimi")
    self.driver.find_element(By.ID, "password").send_keys("Tuan1997Phac1995@")
    self.driver.find_element(By.NAME, "login").click()
    time.sleep(3)
    assert self.driver.title == "Tài khoản -"
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-23 .menu-text").click()
    time.sleep(3)

    # Chọn ngày
    self.driver.find_element(By.CSS_SELECTOR, ".bookly\\3A flex:nth-child(5) > .bookly\\3Ah-10:nth-child(6)").click()
    # Dropdown dịch vụ
    service_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[id*='services']")))
    service_dropdown.click()
    service_dropdown.find_element(By.CSS_SELECTOR, "option[value='2']").click()
    time.sleep(3)
    # Dropdown nhân viên
    staff_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[id*='staff']")))
    staff_dropdown.click()
    staff_dropdown.find_element(By.CSS_SELECTOR, "option[value='2']").click()
    time.sleep(3)
    # Chọn dịch vụ
    self.driver.find_element(By.CSS_SELECTOR, ".bookly\\3A\\@max-2xl\\/main\\3Aw-full").click()
    time.sleep(3)
    # Chọn khung giờ
    self.driver.find_element(By.XPATH, "//button[contains(.,'11:00')]").click()
    time.sleep(3)
    # Điền thông tin
    self.driver.find_element(By.CSS_SELECTOR, "input[id*='full-name']").clear()
    self.driver.find_element(By.CSS_SELECTOR, "input[id*='full-name']").send_keys(" ")
    self.driver.find_element(By.CSS_SELECTOR, "input[id*='email']").clear()
    self.driver.find_element(By.CSS_SELECTOR, "input[id*='email']").send_keys("lajibolala672@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, "input[id*='phone']").clear()
    self.driver.find_element(By.CSS_SELECTOR, "input[id*='phone']").send_keys("0912546783")
    self.driver.find_element(By.CSS_SELECTOR, "textarea[id*='notes']").send_keys("abcxyz")
    self.driver.find_element(By.CSS_SELECTOR, "button[title='Book now']").click()
    time.sleep(3)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".bookly\\:text-red-800")
    assert len(elements) > 0