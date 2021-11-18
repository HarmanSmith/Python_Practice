from pages.basePage import BasePage
from pages.homePage import HomePage
from pages.resultsPage import ResultPage

def test_website_search(browser):
    homePage = HomePage(browser)
    resultsPage = ResultPage(browser)
    searchPhrase = "zen"

    homePage.load()
    #assert page is loaded with a boolean from homePage object
    assert homePage.checkSearchButton()

    #search "zen" in the website
    homePage.inputSearchText(searchPhrase)

    #order low to high
    #TODO AttributeError: 'WebElement' object has no attribute 'select_by_visible_text'
    resultsPage.sortBy("Price: Low to High")

    #assert low to high with a method from the resultsPage
    assert resultsPage.checkLowToHigh()
