import requests
from bs4 import BeautifulSoup
import urllib.request

class BosePriceMediaMarkt:

    def __init__(self, url) -> None:
        self.__url = url
        self.bosePrice = self.__getBosePriceFromMediaMarkt()

    def __getBosePriceFromMediaMarkt(self) -> float: 

        # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
        # response = requests.get(self.__url, headers=headers, timeout=10)

        # # print(r)

        # # Parsing the HTML
        # soup = BeautifulSoup(response.content, 'html.parser')
        # # print(soup.prettify())

        # with open("output.html", "w", encoding="utf-8") as file:
        #     file.write(soup.prettify())
        try:
            # Open the URL and read its content
            response = urllib.request.urlopen(self.__url)
            
            # data = response.read()
            
            # html_content = data.decode('utf-8')
            
            # print(html_content)
            # with open("output.html", "w", encoding="utf-8") as file:
            #     soup = BeautifulSoup(html_content, 'html.parser')
            #     print(soup.prettify())
            #     file.write(soup.prettify())

        except Exception as e:
            print("Error fetching URL:", e)

