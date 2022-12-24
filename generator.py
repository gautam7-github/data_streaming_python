from datetime import datetime as dt

import pandas as pd
import requests
from mimesis import Address, Datetime, Finance, Internet, Person
from mimesis.enums import Gender

person = Person('en')


person = Person()
addess = Address()
datetime = Datetime()
finance = Finance()
internet = Internet()


def generatePersonData():
    def create_rows_mimesis(num=1):
        output = [
            {
                "name": person.full_name(),
                "age": person.age(),
                "gender": person.gender(),
                "date_of_joining": datetime.formatted_date(),
                "email": person.email(),
                "occupation": person.occupation(),
                "employer": finance.company(),
                "city": addess.city(),
                "state": addess.state(),
                "country": addess.country(),
                "nationality": person.nationality(),
                "ipv6": internet.ip_v6(),
                "ipv4": internet.ip_v4(),
                "mac_address": internet.mac_address()
            } for _ in range(num)
        ]
        return output

    return pd.DataFrame(create_rows_mimesis(100))


def generateStockData():
    def create_rows_mimesis(num=1):
        output = [
            {
                "company": finance.stock_name(),
                "ticker": finance.stock_ticker(),
                "price": finance.price()
            } for _ in range(num)
        ]
        return output

    return pd.DataFrame(create_rows_mimesis(10))


def generateNSEData():
    URL = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    resp = requests.get(URL, headers=headers)
    print(resp.status_code)
    if resp.status_code == 200:
        jsonData = resp.json()
        stocks = jsonData['data'][1:]
        df = pd.DataFrame.from_records(stocks)
        df['timestamp'] = dt.now()
    else:
        print("Error")
        return pd.DataFrame()
