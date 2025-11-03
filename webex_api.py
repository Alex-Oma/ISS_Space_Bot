def get_list_of_webex_rooms(webex_base_url, webex_access_token):
    '''
    This function retrieves the list of Webex rooms using the Webex Rooms API.
    It returns a list of rooms with their details.
    Parameters:
        webex_base_url (str): The base URL of the Webex API.
        webex_access_token (str): The access token for authenticating with the Webex API.
    Returns:
        list: A list of Webex rooms with their details.
    '''


    import requests

    # 3. Provide the URL to the Webex room API.
    endpoint_url = webex_base_url + "/rooms"
    r = requests.get(endpoint_url,
                     headers={
                         "Authorization": webex_access_token,
                         "Accept": "application/json"
                     }
    )

    #######################################################################################
    # DO NOT EDIT ANY BLOCKS WITH r.status_code
    if not r.status_code == 200:
        raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))
    #######################################################################################
    else:
        rooms = r.json()["items"]
        return rooms

def search_for_webex_room_to_monitor(rooms):
    '''
    This function searches for a Webex room to monitor based on user input.
    It prompts the user to enter a room name and searches for it in the provided list of rooms.
    If found, it returns the room ID and title; otherwise, it prompts the user to try again.
    Parameters:
        rooms (list): A list of Webex rooms with their details.
    Returns:
        tuple: A tuple containing the room ID and title of the found room.
    '''
    #######################################################################################
    # SEARCH FOR WEBEX ROOM TO MONITOR
    #  - Searches for user-supplied room name.
    #  - If found, print "found" message, else prints error.
    #  - Returns values for later use by bot.
    #######################################################################################
    while True:
        roomNameToSearch = input("Which room should be monitored for the /seconds messages? ")
        roomIdToGetMessages = None
        roomTitleToGetMessages = ""

        for room in rooms:
            if(room["title"].find(roomNameToSearch) != -1):
                print ("Found rooms with the word " + roomNameToSearch)
                print(room["title"])
                roomIdToGetMessages = room["id"]
                roomTitleToGetMessages = room["title"]
                print("Found room: " + roomTitleToGetMessages)
                break

        if(roomIdToGetMessages == None):
            print("Sorry, I didn't find any room with " + roomNameToSearch + " in it.")
            print("Please try again...")
        else:
            break

    return roomIdToGetMessages, roomTitleToGetMessages


def print_webex_rooms(rooms):
    '''
    This function prints the type and title of each Webex room in the provided list.
    Parameters:
        rooms (list): A list of Webex rooms with their details.
    Returns:
        None
    '''
    # 4. Create a loop to print the type and title of each room.
    print("\nList of available rooms:")
    for room in rooms:
        print(f"Room Type: {room['type']}, Title: {room['title']}")


def get_last_message_from_room(webex_base_url, webex_access_token, roomIdToGetMessages):
    '''
    This function retrieves the last message from a specified Webex room using the Webex Messages API.
    Parameters:
        webex_base_url (str): The base URL of the Webex API.
        webex_access_token (str): The access token for authenticating with the Webex API.
        roomIdToGetMessages (str): The ID of the Webex room from which to retrieve the last message.
    Returns:
        str: The text of the last message in the specified Webex room.
    '''
    import requests
    # 5. Provide the URL to the Webex messages API.
    endpoint_url = webex_base_url + "/messages"
    GetParameters = {
        "roomId": roomIdToGetMessages,
        "max": 1
    }
    r = requests.get(endpoint_url,
                         params=GetParameters,
                         headers={
                             "Authorization": webex_access_token,
                             "Accept": "application/json"
                        }
                    )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))

    json_data = r.json()
    if len(json_data["items"]) == 0:
        print("There are no messages found in the room.")
        return None

    messages = json_data["items"]
    message = messages[0]["text"]
    return message


def send_message_to_webex_room(webex_base_url, webex_access_token, roomId, messageText):
    '''
    This function sends a message to a specified Webex room using the Webex Messages API.
    Parameters:
        webex_base_url (str): The base URL of the Webex API.
        webex_access_token (str): The access token for authenticating with the Webex API.
        roomId (str): The ID of the Webex room to which the message will be sent.
        messageText (str): The text of the message to be sent to the Webex room.
    Returns:
        None
    '''
    import requests
    # Provide the URL to the Webex messages API.
    endpoint_url = webex_base_url + "/messages"
    payload = {
        "roomId": roomId,
        "text": messageText
    }
    r = requests.post(endpoint_url,
                      json=payload,
                      headers={
                          "Authorization": webex_access_token,
                          "Content-Type": "application/json",
                          "Accept": "application/json"
                      }
    )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))