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
from webex_api import get_list_of_webex_rooms, search_for_webex_room_to_monitor, print_webex_rooms, get_last_message_from_room, send_message_to_webex_room
from iss_location_api import get_iss_location
from geolocation_api import get_location_from_coordinates

webex_base_url = "https://webexapis.com/v1"
iss_base_url = "http://api.open-notify.org"
geocode_base_url = "https://eu1.locationiq.com/v1"

# 1. Import libraries for API requests, JSON formatting, epoch time conversion, and iso3166.

import sys
import json
import requests
import time
from pprint import pprint


accessToken = input("Please enter your Webex access token: ")
accessToken = "Bearer " + accessToken
geoCodeToken = input("Please enter your Geolocation access token: ")

# Let's fetch the list of Webex rooms using the function from webex_api.py
rooms = get_list_of_webex_rooms(webex_base_url, accessToken)

# Let's print the list of Webex rooms using the function from webex_api.py
print_webex_rooms(rooms)

# Handle the case when no rooms are found and in this case exit the program as there is no room to monitor
if len(rooms) == 0:
    print("No rooms found for this user. Please create a room in Webex. Exiting the program.")
    sys.exit()

#######################################################################################
# SEARCH FOR WEBEX ROOM TO MONITOR
#  - Searches for user-supplied room name.
#  - If found, print "found" message, else prints error.
#  - Stores values for later use by bot.
# DO NOT EDIT CODE IN THIS BLOCK
#######################################################################################

roomIdToGetMessages, roomTitleToGetMessages = search_for_webex_room_to_monitor(rooms)


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

    # Let's get the last message from the Webex room using the function from webex_api.py
    message = get_last_message_from_room(webex_base_url, accessToken, roomIdToGetMessages)
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

        # Let's get the ISS location using the function from iss_location_api.py
        lat, lng, timestamp = get_iss_location(iss_base_url)

# 8. Convert the timestamp epoch value to a human readable date and time.
# Calling the epoch_to_readable function to convert the timestamp to a human readable date and time.
        timeString = epoch_to_readable(timestamp)

#Let's get the geographical location using the function from geolocation_api.py
        responseMessage = get_location_from_coordinates(geocode_base_url, geoCodeToken, lat, lng, timeString)

# print the response message
        print("Sending to Webex: " + responseMessage)
        # Let's send the message to the Webex room using the function from webex_api.py
        send_message_to_webex_room(webex_base_url, accessToken, roomIdToGetMessages, responseMessage)
