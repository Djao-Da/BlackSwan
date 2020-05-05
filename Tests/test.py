import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.loginpage import LoginPage
from Pages.welcomepage import WelcomePage
from Pages.homepage import HomePage



class BlackTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testLoginAndSearch(self):
        self.driver.get("https://demo1.element.xara.ai/element/login")
        loginpage = LoginPage(self.driver)
        welcomepage = WelcomePage(self.driver)
        homepage = HomePage(self.driver)

        loginpage.do_login(login="support", password="$upp0rto1")

        welcomepage.skip_to_dashboard()

        homepage.proceed_to_advenced_search()
        homepage.select_type()
        homepage.search_for(company="Adidas", jurisdiction="Germany")


        # result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'some_css_selector')))
        # self.assertEqual('ADIDAS AG', result.get_attribute('innerText'))

    @classmethod
    def tearDown(self):
        self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='BlackSwan_report'))
