import requests

api_key = 'wjraHCNRXJHe9xV5tjFLiA'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': 'https://linkedin.com/in/johnrmarty/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)
print(response.json())