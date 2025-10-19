

def get_location_from_coordinates(geolocation_base_url, api_key, latitude, longitude, timeString):
    import requests
    from iso3166 import countries

    # 9. Provide your Geoloaction API consumer key.
    # https://eu1.locationiq.com/v1/reverse?key=pk.6b11667ec7f2f2dd378b1cec9b4d152e&lat=51.50344025&lon=-0.12770820958562096&format=json
    mapsAPIGetParameters = {
        "key": api_key,
        "lat": latitude,
        "lon": longitude,
        "format": "json",
    }

    # 10. Provide the URL to the Reverse GeoCode API.
    # Get location information using the API reverse geocode service using the HTTP GET method
    # {"place_id":"274058577","licence":"https:\/\/locationiq.com\/attribution","osm_type":"relation","osm_id":"1879842","lat":"51.503487750000005","lon":"-0.12769645443243238","display_name":"10 Downing Street, 10, Downing Street, Westminster, Millbank, London, Greater London, England, SW1A 2AA, United Kingdom","address":{"government":"10 Downing Street","house_number":"10","road":"Downing Street","quarter":"Westminster","suburb":"Millbank","city":"London","state_district":"Greater London","state":"England","postcode":"SW1A 2AA","country":"United Kingdom","country_code":"gb"},"boundingbox":["51.5033074","51.5036913","-0.1277991","-0.1273088"]}
    endpoint_url = geolocation_base_url + "/reverse"
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
            timeString, latitude, longitude)
    else:
        responseMessage = "On {}, the ISS was flying over the following location: \n{} \n{}, {} \n{}\n({}\", {}\")".format(
            timeString, StreetResult, CityResult, StateResult, CountryResult, latitude, longitude)

    return responseMessage
