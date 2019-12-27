#!/usr/bin/env python3

import requests
import json


bitfinex_url = 'https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD'


def get_current_price():
    response = None
    try:
        response = requests.get(bitfinex_url, timeout=2)
    except requests.exceptions.Timeout:
        print('[ERROR] Exchange API not responding.')
        raise
    return json.loads(response.text)[0][1]


if __name__ == '__main__':
    with open("price.csv", "w+") as file:
        file.write(str(get_current_price()))
        print('[INFO] price.csv file created.')
