

def get_customized_firefox_driver():
  from selenium import webdriver
  profile = webdriver.FirefoxProfile()
  profile.set_preference('startup.homepage_welcome_url.additional', '')
  profile.set_preference("browser.startup.homepage_override.mstone", "ignore")
  dr = webdriver.Firefox(profile)
  return dr