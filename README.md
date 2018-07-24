# My-diary-api
A restful app intended to communicate using api endpoints
## DESCRIPTION
My-diary-api is a restful api intended to communicate with a front end of your choice using various api endpoints.
The api endpoints are meant to do the following
- POST (post entries to my dictionary)
- GET   ( fetch entries from my dictionary)
- DELETE (delete an  entry from my dictionary)
- PUT    (modify an entry from my dictionary)

## REQUIREMENTS
Minimum requirements needed to run this application include;
- pip
- virtual env
- python3

## RUNNING THE APPLICATION
- clone the repository
- activate the virtual environment
- install dependencies
- run the application
## TESTING THE APP
Postman was the main application used in test the endpoints using the routes provided below
- fetch all  diary entries  (GET) https://my-diary-api-endpoints.herokuapp.com/api/v1/entries
- fetch a single diary entry (GET) https://my-diary-api-endpoints.herokuapp.com/api/v1/entries/<int:id>
- post an entry into my diary(POST) https://my-diary-api-endpoints.herokuapp.com/api/v1/entries
- modify a single diary entry (PUT) https://my-diary-api-endpoints.herokuapp.com/api/v1/entries/<int:id>
- delete an entry from my diary (DELETE)https://my-diary-api-endpoints.herokuapp.com/api/v1/entries/<int:id>


## RUN TEST
- python app-test.py