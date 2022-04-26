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
    collection = []
    for object in table:
        collection.append(object["mid"])
        print(f'{object["effectiveDate"]} - {object["mid"]}')
    ave = ((sum(collection)) / int(number))
    print(f'The average of the {number} days is {round(ave, 4)} PLN')


average_daily_exchange_rate()