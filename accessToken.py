import oauthlib
import requests
import oauthlib.oauth2 as oa2
from urllib.parse import urlencode
import webbrowser
import json
from rauth import OAuth2Service

#  Values that you need to provide
base_url = 'https://api.kroger.com/v1/connect/oauth2'
authorization_url = base_url + '/authorize'
token_url = base_url + '/token'
client_id = "mealpricer-940ddd5f344ad0a2bde8913ee5b51b9d3823471200546567028"
client_secret = "pqGNCYnGQ8lIrfAA69KJSTE9FhGhsNjFzzFFQuoG"
api_base_url = 'https://api.kroger.com'
redirect_url = 'https://api.kroger.com/v1/'
w = requests.get(f'{authorization_url}?response_type=code&client_id={client_id}&redirect_url={redirect_url}')
PARAMS = {'grant_type': 'client-credentials',
          'client_id': client_id,
          'client_secret': client_secret,
          'redirect_uri': redirect_url}
r = requests.post(token_url,data=PARAMS)
print(w.text)

