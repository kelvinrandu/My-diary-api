[![Coverage Status](https://coveralls.io/repos/github/kelvinrandu/My-diary-api/badge.svg?branch=develop)](https://coveralls.io/github/kelvinrandu/My-diary-api?branch=develop)
[![Build Status](https://travis-ci.org/kelvinrandu/My-diary-api.svg?branch=develop)](https://travis-ci.org/kelvinrandu/My-diary-api)
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
- [pip](https://packaging.python.org/tutorials/installing-packages/)
- [python3](https://www.python.org/getit/)

## RUNNING THE APPLICATION
- clone [this](https://github.com/kelvinrandu/My-diary-api/tree/master) repository
- navigate to the project directory
- activate the virtual environment
``` $ source .env ```
- install dependencies needed for the project to run
``` $ pip install -r requirements.txt ```
- install flask
``` $ pip install flask```
- run the application
``` $ python app.py ```
## API ROUTES

| Methods        | Url          | Description |
| ------------- |:-------------:| -----:|
| GET     | https://my-diary-api-endpoints.herokuapp.com/api/v1/entries           |  Fetches all diary entries |           
| GET     | https://my-diary-api-endpoints.herokuapp.com/api/v1/entries/<int:id>  |  Fetches a single diary entry    |
| POST    | https://my-diary-api-endpoints.herokuapp.com/api/v1/entries           |  Creates a new diary entry       |
| PUT     | https://my-diary-api-endpoints.herokuapp.com/api/v1/entries/<int:id>  |   Modifies an entry              |
| DELETE  | https://my-diary-api-endpoints.herokuapp.com/api/v1/entries/<int:id>  |   Deletes an entry from my Diary |

## TESTING THE APP
Postman was the main application used in test the endpoints using the routes provided below
ans a snip of the response if request is successful
- fetch all  diary entries
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/get%20all.png)
- fetch a single diary entry
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/post%20%20%20get%20each.png)
- post an entry into my diary 
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/post%20entry.png)
- modify a single diary entry  
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/modify.png)
- delete an entry from my diary
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/ch-add-readme-159255344/images/delete.png)


## RUN TEST
To run unitests type the code below in your terminal in your root folder
``` $ python app-test.py ```