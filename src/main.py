import sys
from pathlib import Path

from store_prices.BosePriceEuroRtvAgh import BosePriceEuroRtvAgh
from store_prices.BosePriceMediaMarkt import BosePriceMediaMarkt

# URL of the product page
urlEuroRtvAgh = "https://www.euro.com.pl/sluchawki/bose-quietcomfort-ultra-earbuds-dokanalowe-bluetooth-5-3-diamond-60th.bhtml"
urlMediaExpert = 'https://www.mediaexpert.pl/'
urlMediaMarkt = 'https://mediamarkt.pl/pl/product/_sluchawki-douszne-bose-quietcomfort-ultra-earbuds-bialy-1477223.html?srsltid=AfmBOoqGG1ZP5GvEF5NZL0lPZwa3Yhf9O7ZNa8-XNhsQC57MpbpEgxPD'

def main():
    sys.path.append(str(Path(__file__).resolve().parent / "src"))

    # x = BosePriceEuroRtvAgh(urlEuroRtvAgh)
    y = BosePriceMediaMarkt(urlMediaMarkt)

if __name__=="__main__":
    main()

