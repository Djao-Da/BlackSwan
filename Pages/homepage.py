import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import Locators

class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.header_discover_css = Locators.header_discover_css
        self.menu_cubes_css = Locators.menu_cubes_css
        self.advanced_search_css = Locators.advanced_search_css

    def proceed_to_advenced_search(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.header_discover_css)))
        menuDiscover = self.driver.find_element_by_css_selector(self.header_discover_css)

        menuDiscover.click()

        menuCubes = self.driver.find_element_by_css_selector(self.menu_cubes_css)

        menuCubes.click()

        btnAdvancedSearch = self.driver.find_element_by_css_selector(self.advanced_search_css)

        # btnAdvancedSearch.click()

    def select_type(self):
        time.sleep(5)

    def search_for(self, company, jurisdiction):
        time.sleep(5)
