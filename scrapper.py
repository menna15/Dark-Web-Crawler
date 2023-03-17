from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import os
import time
def create_torbrowser_webdriver_instance():
  tor_binary_path_driver = '~/Downloads/tor-browser/Browser/firefox'
  geckodriver_path = 'driver/geckodriver'

  os.popen(tor_binary_path_driver)
  options = Options()
  options.add_argument('-headless')

  options = webdriver.FirefoxOptions()
  options.set_capability("proxy", 
    {
    "proxyType": "MANUAL",
    'socksProxy': '127.0.0.1:9150',
    "socksVersion": 5
  })
  driver = webdriver.Firefox(options=options)
  return driver

if __name__ == '__main__':
  driver = create_torbrowser_webdriver_instance()
  time.sleep(10)
  driver.find_element("id", 'connectButton').click()
  time.sleep(1)
  respond = driver.get("https://www.youtube.com/")
  print(respond)
  # do some scraping, crawling ...
  driver.close()