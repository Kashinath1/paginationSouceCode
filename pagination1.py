import requests

baseurl = 'https://www.annapurnapost.com/'
endpoint = 'character'

def main_request(baseurl, endpoint):
    r =  requests.get(baseurl + endpoint)
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    for item in response['results']:
        print(item['name'], len(item['[episode']))
    return 
    
    


data = main_request(baseurl, endpoint)
print(get_pages(data))
parse_json(data)

