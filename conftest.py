import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def driver():
    # Khởi tạo Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver          # Trả driver cho test sử dụng
    driver.quit()         # Đóng trình duyệt sau khi test xong