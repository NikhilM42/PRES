import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),options=chrome_options)

url="https://www.realtor.ca"

driver.get(url)

try:
    searchbtn = driver.find_element_by_id("homSearcchBtn")
    searchbar = driver.find_element_by_id("homeSearchTxt")

    if searchbtn.is_displayed():
        searchbar.clear()
        search_field.send_keys("Kitchener")
        search_field.send_keys(Keys.RETURN)

        listbtn = driver.find_element_by_class("toggleOption")
        listbtn.click()

        cnum = driver.find_element_by_id("select2-j17q-container").get_text()
        maxnum = eval(driver.find_element_by_class("paginationTotalPagesNum").get_text())

        nextpage = driver.find_element_by_class("lnkNextResultsPage")
        
        #while (cnum < maxnum): 
        listingCardList = driver.find_element_by_class("listingCardList")

        if listingCardList != None:
            for Card in listingCardList.find_elements_by_class("cardCon"):
                
                entry = {}
                entry['address'] = Card.find_element_by_class("listingCardAddress").get_text().strip()
                entry['price'] = Card.find_element_by_class("listingCardPrice").get_text()
                
                val = Card.find_elements_by_class("listingCardIconNum")
                entry['bedrooms'] = eval(val[0].get_text())
                entry['bathrooms'] = val[1].get_text()
                entry['link'] = baseurl + Card.find_element_by_class("blockLink")['href']

                data.append(entry)

            print(data)
            #nextpage.click()
        else:
            print(listingCardList)
            print("no data")
    driver.close()
except:
    driver.close()
