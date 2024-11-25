from bs4 import BeautifulSoup
import json

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BosePriceMediaMarkt:

    def __init__(self, url) -> None:
        self.__url = url
        self.bosePrice = self.__getBosePriceFromMediaMarkt()

    def __getBosePriceFromMediaMarkt(self) -> float: 

        gecko_service = Service(r"C:\Users\marcj\Documents\gecko\geckodriver.exe")

        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Firefox(service=gecko_service, options=options)

        try:
            driver.get(self.__url)

            html_content = driver.page_source

            with open("output.html", "w", encoding="utf-8") as file:
                file.write(html_content)

            scripts = driver.find_elements("tag name", "script")

            for script in scripts:

                if "application/ld+json" in script.get_attribute("type"):
                    try:
                        json_data = json.loads(script.get_attribute("innerHTML"))
                        
                        if "@type" in json_data and json_data["@type"] == "BuyAction":
                            price = float(json_data["object"]["offers"]["price"])

                            return price

                    except json.JSONDecodeError:
                        pass 
        
        finally:
            driver.quit()
        
        return 0
    
    def getPrice(self) -> float:
        return self.bosePrice