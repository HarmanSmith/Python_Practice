from pages.basePage import BasePage
from pages.homePage import HomePage
from pages.searchPage import ResultPage

def test_website_search(browser):
    homePage = HomePage(browser)
    searchPage = ResultPage(browser)
    searchPhrase = "zen"

    homePage.load()
    #assert page is loaded
    pass
    #search zen
    homePage.inputSearchText(searchPhrase)

    #order low to high
    
    #assert low to high
