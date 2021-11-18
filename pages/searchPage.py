from pages.basePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ResultPage(BasePage):
    def __init__(self, browser):
        super().__init__(self, browser=browser)

#Sort dropbox web element
    searchSort = browser.find_element(By.xpath("//div[contains(@class, 'search-sort')]"))

#list of web elements (24 per page)
    itemPrices = browser.find_element(By.xpath("//img[contains(@alt, 'Bells')]"))

#Sort method
    def sortBy(self,sortOption):
        pass

#check sorted low to high
    def checkLowToHigh(self):
        pass
