###############################################################
#This is just a starter code for the assignment 1, 
# you need to follow the assignment brief to complete all the tasks required by the assessment brief
#
#  This program:
# - Asks the user to enter an access token or use the hard coded access token.
# - Lists the user's Webex rooms.
# - Asks the user which Webex room to monitor for "/seconds" of requests.
# - Monitors the selected Webex Team room every second for "/seconds" messages.
# - Discovers GPS coordinates of the ISS flyover using ISS API.
# - Display the geographical location using geolocation API based on the GPS coordinates.
# - Formats and sends the results back to the Webex Team room.
#
# The student will:
# 1. Import libraries for API requests, JSON formatting, epoch time conversion, and iso3166.
# 2. Complete the if statement to ask the user for the Webex access token.
# 3. Provide the URL to the Webex room API.
# 4. Create a loop to print the type and title of each room.
# 5. Provide the URL to the Webex messages API.
# 6. Provide the URL to the ISS Current Location API.
# 7. Record the ISS GPS coordinates and timestamp.
# 8. Convert the timestamp epoch value to a human readable date and time.
# 9. Provide your Geoloaction API consumer key.
# 10. Provide the URL to the Geoloaction address API.
# 11. Store the location received from the Geoloaction API in a variable.
# 12. Complete the code to format the response message.
# 13. Complete the code to post the message to the Webex room.
###############################################################
from time_utils import epoch_to_readable



webex_base_url = "https://webexapis.com/v1"
iss_base_url = "http://api.open-notify.org"
geocode_base_url = "https://eu1.locationiq.com/v1"

# 1. Import libraries for API requests, JSON formatting, epoch time conversion, and iso3166.

import sys
import json
import requests
import time
from pprint import pprint
from iso3166 import countries

# 2. Complete the if statement to ask the user for the Webex access token.
choice = input("Do you wish to use the hard-coded Webex token? (y/n) ")

if choice.lower() == "n":
    accessToken = input("Please enter your Webex access token: ")
else:
    accessToken = "Bearer NA"

# 3. Provide the URL to the Webex room API.
endpoint_url = webex_base_url + "/rooms"
r = requests.get(   endpoint_url,
                    headers = {
                        "Authorization": accessToken,
                        "Accept": "application/json"
                    }
                )

#######################################################################################
# DO NOT EDIT ANY BLOCKS WITH r.status_code
if not r.status_code == 200:
    raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))
#######################################################################################

# 4. Create a loop to print the type and title of each room.
print("\nList of available rooms:")
rooms = r.json()["items"]

for room in rooms:
    print(f"Room Type: {room['type']}, Title: {room['title']}")

#######################################################################################
# SEARCH FOR WEBEX ROOM TO MONITOR
#  - Searches for user-supplied room name.
#  - If found, print "found" message, else prints error.
#  - Stores values for later use by bot.
# DO NOT EDIT CODE IN THIS BLOCK
#######################################################################################

while True:
    roomNameToSearch = input("Which room should be monitored for the /seconds messages? ")
    roomIdToGetMessages = None

    for room in rooms:
        if (room["title"].find(roomNameToSearch) != -1):
            print("Found rooms with the word " + roomNameToSearch)
            print(room["title"])
            roomIdToGetMessages = room["id"]
            roomTitleToGetMessages = room["title"]
            print("Found room: " + roomTitleToGetMessages)
            break

    if (roomIdToGetMessages == None):
        print("Sorry, I didn't find any room with " + roomNameToSearch + " in it.")
        print("Please try again...")
    else:
        break

######################################################################################
# WEBEX BOT CODE
#  Starts Webex bot to listen for and respond to /seconds messages.
######################################################################################

while True:
    time.sleep(1)
    GetParameters = {
        "roomId": roomIdToGetMessages,
        "max": 1
    }
# 5. Provide the URL to the Webex messages API.
    endpoint_url = webex_base_url + "/messages"
    r = requests.get(endpoint_url,
                         params=GetParameters,
                         headers={
                             "Authorization": accessToken,
                             "Accept": "application/json"
                        }
                    )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))

    json_data = r.json()
    if len(json_data["items"]) == 0:
        print("There are no messages found in the room.")


    messages = json_data["items"]
    message = messages[0]["text"]
    print("Received message: " + message)

    if message.find("/") == 0:
        if (message[1:].isdigit()):
            seconds = int(message[1:])
        else:
            raise Exception("The message is not in the correct format. It should be /<number of seconds>")

        # for the sake of testing, the max number of seconds is set to 5.
        if seconds > 5:
            seconds = 5

        time.sleep(seconds)

# 6. Provide the URL to the ISS Current Location API.
        r = requests.get(iss_base_url + "/iss-now.json")

        json_data = r.json()
        if json_data["message"] != "success":
            raise Exception("The ISS API did not return a success message.")

# 7. Record the ISS GPS coordinates and timestamp.
# {"iss_position": {"latitude": "40.6138", "longitude": "-67.0834"}, "message": "success", "timestamp": 1760291326}
        lat = json_data["iss_position"]["latitude"]
        lng = json_data["iss_position"]["longitude"]
        timestamp = json_data["timestamp"]

# 8. Convert the timestamp epoch value to a human readable date and time.
# Calling the epoch_to_readable function to convert the timestamp to a human readable date and time.
        timeString = epoch_to_readable(timestamp)

# 9. Provide your Geoloaction API consumer key.
# https://eu1.locationiq.com/v1/reverse?key=pk.6b11667ec7f2f2dd378b1cec9b4d152e&lat=51.50344025&lon=-0.12770820958562096&format=json
        mapsAPIGetParameters = {
            "key": "NA",
            "lat": lat,
            "lon": lng,
            "format": "json",
        }

# 10. Provide the URL to the Reverse GeoCode API.
# Get location information using the API reverse geocode service using the HTTP GET method
# {"place_id":"274058577","licence":"https:\/\/locationiq.com\/attribution","osm_type":"relation","osm_id":"1879842","lat":"51.503487750000005","lon":"-0.12769645443243238","display_name":"10 Downing Street, 10, Downing Street, Westminster, Millbank, London, Greater London, England, SW1A 2AA, United Kingdom","address":{"government":"10 Downing Street","house_number":"10","road":"Downing Street","quarter":"Westminster","suburb":"Millbank","city":"London","state_district":"Greater London","state":"England","postcode":"SW1A 2AA","country":"United Kingdom","country_code":"gb"},"boundingbox":["51.5033074","51.5036913","-0.1277991","-0.1273088"]}
        endpoint_url = geocode_base_url + "/reverse"
        r = requests.get(endpoint_url, params=mapsAPIGetParameters)

# Verify if the returned JSON data from the API service are OK
        json_data = r.json()

        if not r.status_code == 200 and not r.status_code == 404:
            raise Exception("Incorrect reply from Geocode API. Status code: {}. Text: {}".format(r.status_code, r.text))

        # Handle the case when unable to geocode
        # {"error":"Unable to geocode"}
        if "error" in json_data and json_data["error"] == "Unable to geocode":
            CountryResult = "XZ"
        else:
# 11. Store the location received from the API in a required variables
            CountryResult = json_data["address"]["country_code"].upper()
            StreetResult = json_data["address"]["road"] if "road" in json_data["address"] else "Unknown street"
            CityResult = json_data["address"]["city"] if "city" in json_data["address"] else "Unknown city"
            StateResult = json_data["address"]["state"] if "state" in json_data["address"] else "Unknown state"

        # Find the country name using ISO3611 country code
        if not CountryResult == "XZ":
            CountryResult = countries.get(CountryResult).name

# 12. Complete the code to format the response message.
#     Example responseMessage result: In Austin, Texas the ISS will fly over on Thu Jun 18 18:42:36 2020 for 242 seconds.
# responseMessage = "On {}, the ISS was flying over the following location: \n{} \n{}, {} \n{}\n({}\", {}\")".format(timeString, StreetResult, CityResult, StateResult, CountryResult, lat, lng)

        if CountryResult == "XZ":
            responseMessage = "On {}, the ISS was flying over a body of water at latitude {}° and longitude {}°.".format(
                timeString, lat, lng)
        else:
            responseMessage = "On {}, the ISS was flying over the following location: \n{} \n{}, {} \n{}\n({}\", {}\")".format(
                timeString, StreetResult, CityResult, StateResult, CountryResult, lat, lng)

# print the response message
        print("Sending to Webex: " + responseMessage)

# 13. Complete the code to post the message to the Webex room.
# the Webex HTTP headers, including the Authoriztion and Content-Type
        HTTPHeaders = {
            "Authorization": accessToken,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        PostData = {
           "roomId": roomIdToGetMessages,
            "text": responseMessage
        }

        # Post the call to the Webex message API.
        endpoint_url = webex_base_url + "/messages"
        r = requests.post(endpoint_url, data=json.dumps(PostData), headers = HTTPHeaders
        )

        if not r.status_code == 200:
            raise Exception("Error sending message to room {}. Status code: {}. Text: {}".format(roomTitleToGetMessages, r.status_code, r.text))
