from pages.basePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class HomePage():
    url = "https://nookazon.com/"

    def __init__(self, browser):
        self.browser = browser
    #super().__init__(self, browser)

    def load(self):
        self.browser.get(self.url)

    #Question using "@"self.browser.find_element" ?
    searchInput = (By.XPATH, "//input[contains(@placeholder, 'Search items')]")

    searchButton = (By.XPATH, "//button[contains(@type, 'submit')]")

    def checkSearchButton(self):
        button = self.browser.find_element(*self.searchButton)
        return button.is_displayed()

    def inputSearchText(self, text):
        search_input = self.browser.find_element(*self.searchInput)
        search_input.send_keys(text + Keys.RETURN)
