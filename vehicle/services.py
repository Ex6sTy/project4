import requests


def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get('https://api.currencyapi.com/v1/price?symbol=USD')
    print(response.text)
    usd_price = rub_price * 90
    return usd_price