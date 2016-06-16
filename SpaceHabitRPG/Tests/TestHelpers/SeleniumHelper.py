from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

phantomServiceArgs = ['--load-images=false','--proxy-type=None','--ignore-ssl-errors=true-']

def wait_for_page_load(driver,timeout,pageTitle):
    wait = WebDriverWait(driver,timeout)
    wait.until(expected_conditions.title_is(pageTitle))


def get_firefox_profile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.startup.homepage_overriden.mstone","ignore")
    profile.set_preference("startup.homepage.welcome_url.additional","about:blank")
    return profile