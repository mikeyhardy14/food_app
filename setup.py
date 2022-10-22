import config
import requests
from urllib.request import urlopen
import json
# url = 'https://api.kroger.com/v1/products?filter.term=fat%20free%20milk'
# response = urlopen(url)
# data_json = json.loads(response.read())
# print(data_json)
# locations?filter.zipCode.near=84410&filter.radiusInMiles=10&filter.limit=10

url = "https://api.kroger.com/v1/"
response = requests.get(url)
print(response.text)