# 🚀 Space Bot API Investigation Sheet

**Total Marks: 30**  
**Part 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, and a **Geocoding API** (LocationIQ or Mapbox or other), plus the Python time module.

---

## ✅ Section 1: Webex Messaging API (7 marks)

| Criteria | Details                                                                                                                                                                                                     |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| API Base URL | `https://webexapis.com/v1/`                                                                                                                                                                                 |
| Authentication Method | `OAuth 2.0 Bearer Token`                                                                                                                                                                                    |
| Endpoint to list rooms | `https://webexapis.com/v1/rooms`                                                                                                                                                                            |
| Endpoint to get messages | `https://webexapis.com/v1/messages`                                                                                                                                                                         |
| Endpoint to send message | `https://webexapis.com/v1/messages`                                                                                                                                                                         |
| Required headers | `Authorization: Bearer <access_token>`, `Content-Type: application/json`                                                                                                                                    |
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
|

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
|

---

## ⏰ Section 4: Epoch to Human Time Conversion (Python time module) (2 marks)

| Criteria | Details                           |
|---------|-----------------------------------|
| Library used | `time`                            |
| Function used to convert epoch | `time.strftime()` |
| Sample code to convert timestamp |
import time
epoch_time = 1759761471
human_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))
print(human_time)

|
| Output (human-readable time) | `2025-12-06 13:37:51` |

---

## 🧩 Section 5: Web Architecture & MVC Design Pattern (12 marks)

The Model-View-Controller (MVC) design pattern is a widely used architectural approach in 
software development, particularly for building web applications. It divides an application into 
three interconnected components: Model, View, and Controller, ensuring a clear separation of concerns. 
This modular structure enhances maintainability, scalability, and collaboration among developers.

### 🌐 Web Architecture – Client-Server Model

- **Client**: 
- **Server**: 
- (Explain the communication between them & include a block diagram )
The Client-Server Model is a fundamental concept in web architecture, enabling communication between clients (users or devices) and servers. 
This model is essential for the operation of web applications, as it allows for the efficient handling of data and services. Here's a brief 
overview of how the Client-Server Model works in web architecture:

Client: The frontend or user interface, typically a web browser or mobile app, sends requests to the server.

Server: A powerful machine or system that processes client requests, performs business logic, and returns responses.

Request-Response Cycle: The process involves the client sending a request, the server processing it, and the client receiving a response.

Layered Architecture: The model operates primarily in the application and network layers, with the client initiating communication and the server handling the request and response

### 🔁 RESTful API Usage
 
A RESTful API (Representational State Transfer) is a widely used architectural style for designing networked applications. It allows communication between a client and a server using 
standard HTTP methods. Here's a concise guide to understanding and using RESTful APIs: 

Resources: Everything in a RESTful API is treated as a resource, identified by a unique URL (e.g., /users, /products/123).

HTTP Methods:

Each request from the client to the server must contain all the information needed to process it. The server does not store client state.

JSON/XML: Data is typically exchanged in lightweight formats like JSON or XML.



### 🧠 MVC Pattern in Space Bot

| Component   | Description |
|------------|-------------|
| **Model**  |  |
| **View**   |  |
| **Controller** |  |


#### Example:
- Model: 
- View: 
- Controller: 

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


Example of response received after calling ISS API:
{"iss_position": {"latitude": "40.6138", "longitude": "-67.0834"}, "message": "success", "timestamp": 1760291326}