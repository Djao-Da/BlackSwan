from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import Locators

class WelcomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.btn_no_thanks_css = Locators.btn_no_thanks_css

    def skip_to_dashboard(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.btn_no_thanks_css)))
        btnNoThanks = self.driver.find_element_by_css_selector(self.btn_no_thanks_css)

        btnNoThanks.click()