import requests
import json
import pandas as pd
headers = {
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://www.bmstores.co.uk',
    'Referer': 'https://www.bmstores.co.uk/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
params = {
    "x-algolia-agent": "Algolia for JavaScript (3.35.0); Browser; instantsearch.js (3.6.0); JS Helper (2.28.0)",
    "x-algolia-api-key": "MzE0ODhjNTlhZjMxY2U4ZGM1ZDU4OWU3Mzc1MzM2NzhmZWU2ZjdhNjZhOWRlNTAyMDcxZGQzZGUyODZkZmRkN2ZpbHRlcnM9JTI4c3RhdHVzJTNBYXBwcm92ZWQlMjkrQU5EK3B1Ymxpc2hkYXRlKyUzQysxNzE3ODQ5Njk0K0FORCslMjhleHBpcnlkYXRlKyUzRSsxNzE3ODQ5Njk0K09SK2V4cGlyeWRhdGUrJTNEKy0xJTI5",
    "x-algolia-application-id": "MV7E2A3YQL",
}


data = '{"requests":[{"indexName":"prod_bmstores_stores","params":"query=&hitsPerPage=1000&page=0&attributesToRetrieve=*&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&getRankingInfo=true&aroundLatLng=51.50886%2C-0.59296&aroundRadius=5000000&clickAnalytics=false&facets=%5B%22ranges%22%5D&tagFilters="}]}'

response = requests.post(
    'https://mv7e2a3yql-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.0)%3B%20Browser%3B%20instantsearch.js%20(3.6.0)%3B%20JS%20Helper%20(2.28.0)&x-algolia-application-id=MV7E2A3YQL&x-algolia-api-key=MzE0ODhjNTlhZjMxY2U4ZGM1ZDU4OWU3Mzc1MzM2NzhmZWU2ZjdhNjZhOWRlNTAyMDcxZGQzZGUyODZkZmRkN2ZpbHRlcnM9JTI4c3RhdHVzJTNBYXBwcm92ZWQlMjkrQU5EK3B1Ymxpc2hkYXRlKyUzQysxNzE3ODQ5Njk0K0FORCslMjhleHBpcnlkYXRlKyUzRSsxNzE3ODQ5Njk0K09SK2V4cGlyeWRhdGUrJTNEKy0xJTI5',
    headers=headers,
    params=params,
    data=data,
)
results = response.json()["results"][0]["hits"]

df = pd.DataFrame(results)
df.to_csv('bmloc.csv')