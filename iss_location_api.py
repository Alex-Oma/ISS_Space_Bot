


def get_iss_location(iss_base_url):
    import requests

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

    return lat, lng, timestamp