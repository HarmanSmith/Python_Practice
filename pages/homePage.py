from pages.basePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    def __init__(self, browser, searchTerm):
        super().__init__(self, browser=browser)

    url = "https://nookazon.com/"

    #using self.browser.find_element ??
    searchInput = (By.xpath("//input[contains(@placeholder, 'Search items')]"))

    searchButton = (By.xpath("//button[contains(@type, 'submit')]"))


    def checkSearchButton(self):
        searchButton = self.browser.find_element(*self.searchButton)
        #value = searchButton.element_to_be_clickable?
        #return value?
        pass

    def inputSearchText(self, text):
        search_input = self.browser.find_element(*self.searchInput)
        search_input.send_keys(text + Keys.RETURN)