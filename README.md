# 🚀 Space Bot API Investigation Sheet

**Total Marks: 30**  
**Part 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, and a **Geocoding API** (LocationIQ or Mapbox or other), plus the Python time module.

---

## ✅ Section 1: Webex Messaging API (7 marks)

| Criteria | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| API Base URL | `https://webexapis.com/v1/`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Authentication Method | `OAuth 2.0 Bearer Token`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Endpoint to list rooms | `https://webexapis.com/v1/rooms`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Endpoint to get messages | `https://webexapis.com/v1/messages`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Endpoint to send message | `https://webexapis.com/v1/messages`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Required headers | `Authorization: Bearer <access_token>`, `Accept: application/json`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Sample full GET or POST request | [{'created': '2025-10-12T14:03:18.514Z', 'creatorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hZWMxOWZhOC1hNWQyLTQxZTgtODU2OS05ZTE4MGIzZWU2ODM', 'description': 'This room is used by the project ISS Bot to post ' 'announcements about ISS flyovers.', 'id': 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMzQ1ZTg1MjAtYTc3NC0xMWYwLTg3ZDctYjlmNTIyYjU3YmQ2', 'isLocked': False,   'isPublic': False,   'isReadOnly': False,   'lastActivity': '2025-10-12T14:03:18.514Z',   'ownerId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9iZGQyYWVkMi1kYTE3LTQ4MWQtYmQ2Zi1iNDMwMzdlZTkwYjc',   'title': 'Project ISS Bot Announcements',   'type': 'group'},  {'created': '2025-10-12T14:02:45.214Z',   'creatorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hZWMxOWZhOC1hNWQyLTQxZTgtODU2OS05ZTE4MGIzZWU2ODM',   'description': 'This room is used by the project ISS Bot to post '                  'announcements about ISS flyovers.',   'id': 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMjA4NTU3ZTAtYTc3NC0xMWYwLThkYmQtM2JhZjMzYjQ2Nzc2',   'isLocked': False,   'isPublic': False,   'isReadOnly': False,  'lastActivity': '2025-10-12T14:02:45.214Z',   'ownerId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9iZGQyYWVkMi1kYTE3LTQ4MWQtYmQ2Zi1iNDMwMzdlZTkwYjc',   'title': 'Project ISS Bot Announcements',   'type': 'group'}] |

---

## 🛰️ Section 2: ISS Current Location API (3 marks)

| Criteria | Details                                   |
|---------|-------------------------------------------|
| API Base URL | `http://api.open-notify.org/`             |
| Endpoint for current ISS location | `http://api.open-notify.org/iss-now.json` |
| Sample response format (example JSON) | {"message": "success", "iss_position": {"longitude": "-36.9020", "latitude": "51.4174"}, "timestamp": 1759761471} |  
```

```

---

## 🗺️ Section 3: Geocoding API (LocationIQ or Mapbox or other) (6 marks)

| Criteria                                 | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Provider used (circle one)               | **LocationIQ**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| API Doc                                  | https://docs.locationiq.com/reference/reverse-api                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| API Base URL                             | `https://eu1.locationiq.com/v1/`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Endpoint for reverse geocoding           | `https://eu1.locationiq.com/v1/reverse`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Authentication method                    | `API Key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Required query parameters                | `key, lat, lon, format`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Sample request with latitude/longitude   | https://eu1.locationiq.com/v1/reverse?key=pk.6b11667ec7f2f2dd378b1cec9b4d152e&lat=51.50344025&lon=-0.12770820958562096&format=json                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Sample JSON response (formatted example) | {"place_id":"274058577","licence":"https:\/\/locationiq.com\/attribution","osm_type":"relation","osm_id":"1879842","lat":"51.503487750000005","lon":"-0.12769645443243238","display_name":"10 Downing Street, 10, Downing Street, Westminster, Millbank, London, Greater London, England, SW1A 2AA, United Kingdom","address":{"government":"10 Downing Street","house_number":"10","road":"Downing Street","quarter":"Westminster","suburb":"Millbank","city":"London","state_district":"Greater London","state":"England","postcode":"SW1A 2AA","country":"United Kingdom","country_code":"gb"},"boundingbox":["51.5033074","51.5036913","-0.1277991","-0.1273088"]} |  
```

```

---

## ⏰ Section 4: Epoch to Human Time Conversion (Python time module) (2 marks)

| Criteria | Details                            |
|---------|------------------------------------|
| Library used | `time`                             |
| Function used to convert epoch | `time.ctime(timestamp)`            |
| Sample code to convert timestamp | timeString = time.ctime(timestamp) |
| Output (human-readable time) | `2025-12-06 13:37:51` |

---

## 🧩 Section 5: Web Architecture & MVC Design Pattern (12 marks)

Web Architecture is the conceptual structure and organization of a web application, defining how different components interact and communicate with each other.
In a basic way, it is the blueprint for how a web application is built and how it functions.
It's mai components are:

- Client: The frontend or user interface, typically a web browser or mobile app, that users interact with.
- Server: A powerful machine or system that processes client requests, performs business logic, and returns
- Database: A storage system that holds data for the application, such as user information, content, and settings.
- 
MVS stands for Model-View-Controller.
It is a software design pattern commonly used for developing user interfaces that divides an application into three interconnected components.
This separation helps manage complex applications by promoting organized code, reusability, and maintainability.


### 🌐 Web Architecture – Client-Server Model

- **Client**: The frontend or user interface, typically a web browser or mobile app, sends requests to the server.
- **Server**: A powerful machine or system that processes client requests, performs business logic, and returns responses.
- (Explain the communication between them & include a block diagram )
- 
The Client-Server Model is a distributed application structure that partitions tasks or workloads between service providers, called servers, and service requesters, called clients.
- Clients initiate communication sessions with servers, which await incoming requests.
- Servers are typically powerful machines or systems that manage resources and provide services to multiple clients.
- Clients are usually devices like computers, smartphones, or tablets that users interact with to access services
- provided by servers.
- 


### 🔁 RESTful API Usage
 
A RESTful API (Representational State Transfer) is a set of rules and conventions for building and interacting with web services.
It allows different software applications to communicate with each other over the internet using standard HTTP methods.
- RESTful APIs are designed to be stateless, meaning each request from a client to a server must contain all the information needed to understand and process the request.
- They use standard HTTP methods such as GET, POST, PUT, DELETE, etc., to perform operations on resources.
- Resources are typically represented in formats like JSON or XML.
- RESTful APIs are widely used for web services because they are simple, scalable, and easy to understand.
- They enable developers to create applications that can interact with other applications and services seamlessly.


### 🧠 MVC Pattern in Space Bot

| Component   | Description                                                                                                                                                                                                                                                                                      |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Model**  | It has all the "business" logic such as calling APIs, processing their responses, converting epoch time to human readable time.                                                                                                                                                                  |
| **View**   | It displays text messages to the user and also displays results of calling APIs, showig list of rooms available, last message from the selected room, any error messages and also takes inputs from the user such as access token for webex API, name of the webex room to monitor for commands. |
| **Controller** | This handles the input from the user such as access token being entered, webex room selected for monitoring and makes changes and updates to the model by setting corresponding variables in my bot.                                                                                             |


#### Example:
- Model: An example of Model here could be a class that handles the logic for fetching the current location of the ISS from the ISS Current Location API, processing the response, and converting the epoch time to a human-readable format.
- 
- View: An example of View here could be a function that displays the current location of the ISS and the human-readable time to the user in a formatted message.
- 
- Controller: An example of Controller here could be a function that takes user input (e.g., a command to fetch the ISS location), calls the appropriate Model function to get the data, and then calls the View function to display the result to the user.

---

### 📝 Notes

- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved them using tools like Postman, Curl, or Python scripts.

---

### ✅ Total: /30


Webex API has been successfully called to create new room for ISS flyovers announcements.
b'{"id":"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMzQ1ZTg1MjAtYTc3NC0xMWYwLTg3ZDctYjlmNTIyYjU3YmQ2","title":"Project ISS Bot Announcements","type":"group","isLocked":false,"lastActivity":"2025-10-12T14:03:18.514Z","creatorId":"Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hZWMxOWZhOC1hNWQyLTQxZTgtODU2OS05ZTE4MGIzZWU2ODM","created":"2025-10-12T14:03:18.514Z","ownerId":"Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9iZGQyYWVkMi1kYTE3LTQ4MWQtYmQ2Zi1iNDMwMzdlZTkwYjc","description":"This room is used by the project ISS Bot to post announcements about ISS flyovers.","isPublic":false}'
Successfully called Webex API
{'created': '2025-10-12T14:03:18.514Z',
 'creatorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hZWMxOWZhOC1hNWQyLTQxZTgtODU2OS05ZTE4MGIzZWU2ODM',
 'description': 'This room is used by the project ISS Bot to post '
                'announcements about ISS flyovers.',
 'id': 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMzQ1ZTg1MjAtYTc3NC0xMWYwLTg3ZDctYjlmNTIyYjU3YmQ2',
 'isLocked': False,
 'isPublic': False,
 'lastActivity': '2025-10-12T14:03:18.514Z',
 'ownerId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9iZGQyYWVkMi1kYTE3LTQ4MWQtYmQ2Zi1iNDMwMzdlZTkwYjc',
 'title': 'Project ISS Bot Announcements',
 'type': 'group'}


