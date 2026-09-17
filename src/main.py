import requests

def main():
    r = requests.get('https://store.steampowered.com/api/appdetails', params={'appids' : '1086940'}) #, 'cc' : 'pln', 'filters' : 'price_overview'})

    name = r.json()['1086940']['data']['name']
    price = r.json()['1086940']['data']['price_overview']['final_formatted']
    print(price)

if __name__=="__main__":
    main()

