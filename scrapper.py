from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import os
import time
def create_torbrowser_webdriver_instance():
  tor_binary_path_driver = '~/Downloads/tor-browser/Browser/firefox'
  geckodriver_path = 'driver/geckodriver'

  # os.popen(tor_binary_path_driver)
  options = Options()
  options.binary_location = tor_binary_path_driver
  # options.add_argument('-headless')

  tor_browser = webdriver.Firefox(options=options)
  options = webdriver.FirefoxOptions()
  options.set_capability("proxy", 
    {
    "proxyType": "MANUAL",
    'socksProxy': '127.0.0.1:9150',
    "socksVersion": 5
  })
  driver = webdriver.Firefox(options=options)
  return driver, tor_browser

if __name__ == '__main__':
  driver, tor_browser = create_torbrowser_webdriver_instance()
  tor_browser.find_element("xpath", '//*[@id="connectButton"]').click()
  time.sleep(10)
  driver.get("http://ransomwr3tsydeii4q43vazm7wofla5ujdajquitomtd47cxjtfgwyyd.onion/")
  # do some scraping, crawling ...
  driver.close()