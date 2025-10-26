from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')  # без графического интерфейса (можно убрать, если хочешь видеть окно)
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(4)

    yield driver

    driver.quit()
