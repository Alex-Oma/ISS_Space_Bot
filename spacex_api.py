def get_all_launches(spacex_base_url):
    '''
    This function retrieves all SpaceX launches using the SpaceX Launches API.
    It returns a list of launches with their details.
    '''

    import requests

    endpoint_url = spacex_base_url + "/launches"
    r = requests.get(endpoint_url)

    json_data = r.json()
    if r.status_code != 200:
        raise Exception("Incorrect reply from SpaceX API. Status code: {}. Text: {}".format(r.status_code, r.text))

    return json_data

def get_details_about_a_launch(spacex_base_url, launch_id):
    '''
    This function retrieves details about a specific SpaceX launch using the SpaceX Launches API.
    It returns the details of the specified launch.
    '''

    import requests

    endpoint_url = spacex_base_url + f"/launches/{launch_id}"
    r = requests.get(endpoint_url)

    json_data = r.json()
    if r.status_code != 200:
        raise Exception("Incorrect reply from SpaceX API. Status code: {}. Text: {}".format(r.status_code, r.text))

    return json_data

def get_next_launch(spacex_base_url):
    '''
    This function retrieves details about the next scheduled SpaceX launch using the SpaceX Launches API.
    It returns the details of the next launch.
    '''

    import requests

    endpoint_url = spacex_base_url + "/launches/next"
    r = requests.get(endpoint_url)

    json_data = r.json()
    if r.status_code != 200:
        raise Exception("Incorrect reply from SpaceX API. Status code: {}. Text: {}".format(r.status_code, r.text))

    return json_data

def get_rocket_details(spacex_base_url, rocket_id):
    '''
    This function retrieves details about a specific SpaceX rocket using the SpaceX Rockets API.
    It returns the details of the specified rocket.
    '''

    import requests

    endpoint_url = spacex_base_url + f"/rockets/{rocket_id}"
    r = requests.get(endpoint_url)

    json_data = r.json()
    if r.status_code != 200:
        raise Exception("Incorrect reply from SpaceX API. Status code: {}. Text: {}".format(r.status_code, r.text))

    return json_data

def get_launch_pad_details(spacex_base_url, launchpad_id):
    '''
    This function retrieves details about a specific SpaceX launch pad using the SpaceX Launch Pads API.
    It returns the details of the specified launch pad.
    '''

    import requests

    endpoint_url = spacex_base_url + f"/launchpads/{launchpad_id}"
    r = requests.get(endpoint_url)

    json_data = r.json()
    if r.status_code != 200:
        raise Exception("Incorrect reply from SpaceX API. Status code: {}. Text: {}".format(r.status_code, r.text))

    return json_data

def get_next_launch_details_message(spacex_base_url):
    '''
    This function retrieves details about the next scheduled SpaceX launch and formats a message with the details.
    It returns a formatted string with the next launch details.
    '''

    from datetime import datetime

    result = get_next_launch(spacex_base_url)
    mission_name = result["name"]
    rocket_id = result['rocket']
    launchpad_id = result['launchpad']
    date_utc_str = result['date_utc']

    rocket_details = get_rocket_details(spacex_base_url, rocket_id)
    rocket_type = rocket_details['name']

    launchpad_details = get_launch_pad_details(spacex_base_url, launchpad_id)
    launchpad_location = launchpad_details['locality']
    launchpad_region = launchpad_details['region']
    launchpad_latitude = launchpad_details['latitude']
    launchpad_longitude = launchpad_details['longitude']

    next_launch_details_message = (
        f"The next SpaceX launch is the '{mission_name}' mission using a '{rocket_type}' rocket "
        f"from '{launchpad_location}' ('{launchpad_region}' region, longitude {launchpad_longitude}, "
        f"latitude {launchpad_latitude}) on {date_utc_str} (UTC)."
    )

    return next_launch_details_message