from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import Locators
import time


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.field_username_id = Locators.field_username_id
        self.fieald_passwod_id = Locators.fieald_passwod_id
        self.btn_sign_in_id = Locators.btn_sign_in_id

    def do_login(self, login, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.btn_sign_in_id)))
        fieldUsername = self.driver.find_element_by_id(self.field_username_id)

        fieldUsername.clear()
        fieldUsername.send_keys(login)

        fieldPassword = self.driver.find_element_by_id(self.fieald_passwod_id)

        fieldPassword.clear()
        fieldPassword.send_keys(password)

        btnSignIn = self.driver.find_element_by_id(self.btn_sign_in_id)

        btnSignIn.click()



