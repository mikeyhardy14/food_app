import requests
from oauthlib.oauth2 import WebApplicationClient

#  Values that you need to provide
base_url = 'https://api.kroger.com/v1'
authorization_url = base_url + '/connect/oauth2/authorize'
token_url = base_url + '/connect/oauth2/token'


client_id = "mealpricer-940ddd5f344ad0a2bde8913ee5b51b9d3823471200546567028"
client_secret = "pqGNCYnGQ8lIrfAA69KJSTE9FhGhsNjFzzFFQuoG"
client = WebApplicationClient(client_id)

def exchange_code(code):
    data = {
        'client_id' : client_id,
        'client_secret' : client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': base_url
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r =requests.post(token_url,data=data,headers=headers)
    r.raise_for_status()
    return r.json()

























# url = client.prepare_request_uri(
#     authorization_url,
#     client_secret,
#     redirect_url= 'https://api.kroger.com/v1/',
#     scope= 'product.compact',
# )
#
# data = client.prepare_request_body(
#     redirect_uri= 'https://api.kroger.com/v1/',
#     client_secret= client_secret,
#     client_id = client_id
# )
# response = requests.post(token_url, data=data)
# print(response)