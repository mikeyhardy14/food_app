from rauth import OAuth2Service
import json
import requests


def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]



class ExampleOAuth2Client:
    def __init__(self, client_id, client_secret):
        self.access_token = None

        self.service = OAuth2Service(
            name="foo",
            client_id=client_id,
            client_secret=client_secret,
            access_token_url="http://api.example.com/oauth/access_token",
            authorize_url="http://api.example.com/oauth/access_token",
            base_url="http://api.example.com/",
        )

        self.get_access_token()

    def get_access_token(self):
        data = {'code': 'bar',  # specific to my app
                'grant_type': 'client_credentials', # generally required!
               }

        session = self.service.get_auth_session(data=data, decoder=json.loads)

        self.access_token = session.access_token


base_url = 'https://api.kroger.com/v1/connect/oauth2'
authorization_url = base_url + '/authorize'
token_url = base_url + '/token'
client_id = "mealpricer-940ddd5f344ad0a2bde8913ee5b51b9d3823471200546567028"
client_secret = "pqGNCYnGQ8lIrfAA69KJSTE9FhGhsNjFzzFFQuoG"
api_base_url = 'https://api.kroger.com'
redirect_url = 'https://api.kroger.com/v1/'
print(get_access_token('https://api.kroger.com/v1/connect/oauth2/token', client_id, client_secret))