from bs4 import BeautifulSoup
import json

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BosePriceMediaExpert:

    def __init__(self, url) -> None:
        self.__url = url
        self.bosePrice = self.__getBosePriceFromMediaExpert()

    def __getBosePriceFromMediaExpert(self) -> float: 

        gecko_service = Service(r"C:\Users\marcj\Documents\gecko\geckodriver.exe")

        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Firefox(service=gecko_service, options=options)

        try:
            driver.get(self.__url)

            price_meta = driver.find_element(By.XPATH, "//meta[@property='product:price:amount']")
    
            price = float(price_meta.get_attribute("content"))

            return price

        finally:
            driver.quit()
        
        return 0
    
    def getPrice(self) -> float:
        return self.bosePrice