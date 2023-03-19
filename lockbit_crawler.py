# import from selenium
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import os
import time
import pymongo
from pymongo import MongoClient
from selenium.webdriver.support.wait import WebDriverWait

client = MongoClient("mongodb://raghad:ra123@ac-nmbm3el-shard-00-00.gqycpcd.mongodb.net:27017,ac-nmbm3el-shard-00-01.gqycpcd.mongodb.net:27017,ac-nmbm3el-shard-00-02.gqycpcd.mongodb.net:27017/?ssl=true&replicaSet=atlas-zstffa-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.DataScience
collection = db.lockbit

binary = '../tor-browser/Browser/firefox'
# the location of firefox package inside Tor
if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)


def get_browser(binary=None,options=None):
    global browser  
    # only one instance of a browser opens, remove global for multiple instances
    if not browser: 
        browser = webdriver.Firefox(firefox_binary=binary,options=options)
    return browser

browser = None
browser = get_browser(binary=firefox_binary)

# click on connect to connect the tor browser to the remote nodes
browser.find_element_by_xpath('//*[@id="connectButton"]').click()
time.sleep(3)

# check my IP address
url='http://lockbitapt6vx57t3eeqjofwgcglmutr3a35nygvokja5uuccip4ykyd.onion'
browser.get(url)
#time.sleep(15)
# get attribute onclick value
items = WebDriverWait(browser, timeout=30).until(lambda d: d.find_elements_by_class_name("post-block")) #browser.find_elements_by_class_name("post-block")
liks_list=[]
for item in items:
    attribute_val=item.get_attribute("onclick")
    link=attribute_val[attribute_val.find("/post"):-4]
    liks_list.append(url+link)

print(len(liks_list))   

for link in liks_list:
    # to make sure the page is loaded
    #time.sleep(10)
    try:
        browser.get(link)
        deadline=items = WebDriverWait(browser, timeout=30).until(lambda d: d.find_elements_by_class_name("post-banner-p")) #browser.find_elements_by_class_name("post-block")
#browser.find_elements_by_class_name("post-banner-p")[0].text
        deadline=deadline[0].text
        # remove Deadline: from deadline
        deadline=deadline.replace("Deadline: ","")
        company_name=browser.find_elements_by_class_name("post-big-title")[0].text
        connect=browser.find_elements_by_class_name("desc")[0].text
        # remove any <br> and \n in connect
        connect=connect.replace("<br>","")
        print(deadline,company_name,connect)
        # insert into mongodb
        collection.insert_one({"deadline":deadline,"company_name":company_name,"connect":connect,"link":link})
    except:
        continue    

