import requests
import json
import Pyiiko
from datetime import datetime
import xmltodict

from Pyiiko import IikoServer

now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def stores():
    i = IikoServer(ip='http://194.9.27.239:8129', login='mihail', password='903d1bb6717418f02c05d4901e761dc8a981baeb')
    i.token()
    stores_list = (xmltodict.parse(i.stores())['corporateItemDtoes']['corporateItemDto'])
    i.quit_token()
    return stores_list


def products():
    i = IikoServer(ip='http://194.9.27.239:8129', login='mihail', password='903d1bb6717418f02c05d4901e761dc8a981baeb')
    products_list = (xmltodict.parse(i.products()))
    product_list = []
    for product in products_list['productDtoes']['productDto']:
        try:
            if product['productType'] != "DISH" and product['productType'] != 'MODIFIER':
                product_list.append(product)
        except:
            None
    i.quit_token()
    return product_list


def products_balance(product_id):
    i = IikoServer(ip='http://194.9.27.239:8129', login='mihail', password='903d1bb6717418f02c05d4901e761dc8a981baeb')

    url = 'http://194.9.27.239:8129/resto/api/v2/reports/balance/stores?key=' + i.token() + '&timestamp=' + datetime.now().strftime(
        '%Y-%m-%dT%H:%M:%S') + '&product=' + product_id
    response = requests.get(url)
    i.quit_token()
    storess = stores()
    store_list = []
    for product in json.loads(response.text):
        for store in storess:
            if product['store'] == store['id']:
                store_list.append({"storeName": store['name'],
                                   "amount": product['amount'],
                                   'sum': product['sum']})
    try:
        sorted_data = sorted(store_list, key=lambda x: x['amount'], reverse=True)
        print(sorted_data)
        return sorted_data
    except:
        return store_list




def store_balance():
    None

