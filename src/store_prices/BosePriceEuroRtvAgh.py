from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BosePriceEuroRtvAgh:

    def __init__(self, url) -> None:
        self.__url = url
        self.bosePrice = self.__getBosePriceFromEuroRtvAgh()

    def __getBosePriceFromEuroRtvAgh(self) -> float: 
        gecko_service = Service(r"C:\Users\marcj\Documents\gecko\geckodriver.exe")

        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Firefox(service=gecko_service, options=options)

        try:
            driver.get(self.__url)
            
            price_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-template__large--total"))
            )
            price_decimal = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-template__large--decimal"))
            )

            price = float((price_element.text).replace(" ", "")+"."+price_decimal.text)

            return price
        
        finally:
            driver.quit()
        
        return 0
    
    def getPrice(self) -> float:
        return self.bosePrice