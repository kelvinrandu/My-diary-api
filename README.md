# My-diary-api
A restful app intended to communicate using api endpoints
[![Build Status](https://travis-ci.org/kelvinrandu/My-diary-api.svg?branch=develop)](https://travis-ci.org/kelvinrandu/My-diary-api)
## DESCRIPTION
My-diary-api is a restful api intended to communicate with a front end of your choice using various api endpoints.
The api endpoints are meant to do the following
- POST (post entries to my dictionary)
- GET   ( fetch entries from my dictionary)
- DELETE (delete an  entry from my dictionary)
- PUT    (modify an entry from my dictionary)

## REQUIREMENTS
Minimum requirements needed to run this application include;
- [pip](https://github.com/kelvinrandu/My-diary-api/tree/master)
- [python3](http://www.python-pip-install.com/)

## RUNNING THE APPLICATION
- clone [this](https://github.com/kelvinrandu/My-diary-api/tree/master) repository
- navigate to the project directory
- activate the virtual environment
``` $ source .env ```
- install dependencies needed for the project to run
``` $ pip install -r requirements.txt ```
- run the application
``` $ python app.py ```
## TESTING THE APP
Postman was the main application used in test the endpoints using the routes provided below
ans a snip of the response if request is successful
- fetch all  diary entries  (GET) https://my-diary-api-endpoints.herokuapp.com/api/v1/entries
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/get%20all.png)
- fetch a single diary entry (GET) https://my-diary-api-endpoints.herokuapp.com/api/v1/entries/<int:id>
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/post%20%20%20get%20each.png)
- post an entry into my diary(POST) https://my-diary-api-endpoints.herokuapp.com/api/v1/entries
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/post%20entry.png)
- modify a single diary entry (PUT) https://my-diary-api-endpoints.herokuapp.com/api/v1/entries/<int:id>
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/modify.png)
- delete an entry from my diary (DELETE)https://my-diary-api-endpoints.herokuapp.com/api/v1/entries/<int:id>
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/delete.png)


## RUN TEST
To run unitests type the code below in your terminal in your root folder
``` $ python app-test.py ```