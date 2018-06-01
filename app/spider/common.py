import requests
from fake_useragent import UserAgent
ua = UserAgent()

def getJsonValues(url):
    
    host = url.split(".com")[0]+".com"
    headers = {
        "Referer": host,
        "User-Agent": ua.random
    }
    response = requests.get(url, headers=headers)
    return response.json()