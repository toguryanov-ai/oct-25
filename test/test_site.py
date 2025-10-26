import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    homepage = HomePage(browser)    
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')

def test_two_moinitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(3)
    homepage.check_product_count(2)