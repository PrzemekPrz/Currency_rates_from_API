import requests
import json

def average_daily_exchange_rate():
    currency = input("Enter of the currency short name: ")
    number = input("Enter number of days back: ")
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/last/{number}/?format=json'
    response = requests.get(url)
    data = json.loads(response.text)
    table = data['rates']
    name = data['currency']
    result = (f'{name} - {currency}')
    print(result.upper())
    for object in table:
        print(f'{object["effectiveDate"]} - {round(object["mid"], 2)} PLN')
average_daily_exchange_rate()