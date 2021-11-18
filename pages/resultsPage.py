from pages.basePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
#todo Q: ^^^ for dropdown?
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ResultPage():
    def __init__(self, browser):
        self.browser = browser
        #super().__init__(self, browser)

    #Sort dropbox web element
    searchSort = (By.XPATH, "//div[contains(@class, 'search-sort')]")

    #list of web elements (24 per page)
    itemPrices = (By.XPATH, "//img[contains(@alt, 'Bells')]")

    #Sort method
    def sortBy(self, option):
        dropbox = self.browser.find_element(*self.searchSort)
        #selenium command to click the sort dropbox
        dropdown = self.browser.find_element(*self.searchSort)
        dropdown.select_by_visible_text(option)

    #check sorted low to high
    def checkLowToHigh(self):
        pricesList = self.browser.find_element(*self.itemPrices)
        #for loop checking item prices
        previousPrice = 0
        for price in pricesList:
            currentPrice = price.gettext().int()
            if previousPrice < currentPrice:
                return False
        #when the loop finishes if the prices were ordered we return true
        return True



