# 1. Import libraries for API requests, JSON formatting, epoch time conversion, and iso3166.

import sys
import json
import requests
from pprint import pprint

webex_base_url = "https://webexapis.com/v1"

accessToken = "Bearer OWVmYzhkYjktYjc4NC00MjFhLTlmZmUtMjVlOGZlNWYwZDVhYjY1ZGVmYzctYjUz_P0A1_bdd2aed2-da17-481d-bd6f-b43037ee90b7"

# 3. Provide the URL to the Webex room API.
endpoint_url = webex_base_url + "/rooms"

# payload = '''{
#     "title": "Project ISS Bot Announcements",
#     "teamId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
#     "classificationId": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
#     "isLocked": false,
#     "isPublic": true,
#     "description": "This room is used by the Project ISS Bot to post announcements.",
#     "isAnnouncementOnly": false
# }'''

payload = '''{
    "title": "Project ISS Bot Announcements",
    "isLocked": false,
    "isPublic": false,
    "description": "This room is used by the project ISS Bot to post announcements about ISS flyovers.",
    "isAnnouncementOnly": false
}'''


headers = {
    "Authorization": accessToken,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.request('POST', endpoint_url, headers=headers, data = payload)

print(response.text.encode('utf8'))

if not response.status_code == 200:
    raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(response.status_code, response.text))
    sys.exit()


print("Successfully called Webex API")
response_json =response.json()

pprint(response_json)