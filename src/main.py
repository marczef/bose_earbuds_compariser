import sys
from pathlib import Path

from store_prices.BosePriceEuroRtvAgh import BosePriceEuroRtvAgh
from store_prices.BosePriceMediaMarkt import BosePriceMediaMarkt
from store_prices.BosePriceMediaExpert import BosePriceMediaExpert

# URL of the product page
urlEuroRtvAgh = "https://www.euro.com.pl/sluchawki/bose-quietcomfort-ultra-earbuds-dokanalowe-bluetooth-5-3-diamond-60th.bhtml"
urlMediaMarkt = "https://mediamarkt.pl/pl/product/_sluchawki-douszne-bose-quietcomfort-ultra-earbuds-bialy-1477223.html?srsltid=AfmBOoqGG1ZP5GvEF5NZL0lPZwa3Yhf9O7ZNa8-XNhsQC57MpbpEgxPD"
urlMediaExpert = "https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-dokanalowe-bose-quietcomfort-ultra-bialy"

def main():
    sys.path.append(str(Path(__file__).resolve().parent / "src"))

    boseEuroRtvAgd = BosePriceEuroRtvAgh(urlEuroRtvAgh)
    boseMediaMarkt = BosePriceMediaMarkt(urlMediaMarkt)
    boseMediaExpert = BosePriceMediaExpert(urlMediaExpert)

    print(f"słuchawki bose w euro agh {boseEuroRtvAgd.getPrice()}")
    print(f"słuchawki bose w media markt {boseMediaMarkt.getPrice()}")
    print(f"słuchawki bose w media expert {boseMediaExpert.getPrice()}")

if __name__=="__main__":
    main()

