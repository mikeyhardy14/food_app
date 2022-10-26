import oauthlib
import requests
from oauthlib.oauth2 import WebApplicationClient
import json

#  Values that you need to provide
base_url = 'https://api.kroger.com/v1/connect/oauth2'
authorization_url = base_url + '/authorize'
token_url = base_url + '/token'
client_id = "mealpricer-940ddd5f344ad0a2bde8913ee5b51b9d3823471200546567028"
client_secret = "pqGNCYnGQ8lIrfAA69KJSTE9FhGhsNjFzzFFQuoG"
client = WebApplicationClient(client_id)
api_base_url = 'https://api.kroger.com'
redirect_url = 'https://api.kroger.com/v1/'



# authToken = requests.get()
data = client.prepare_request_uri(
    authorization_url,
    client_secret=client_secret,
    redirect_uri=redirect_url,
    scope=['product.compact']
)
print(data)
response = requests.post(token_url, data=data)
print(client.token)