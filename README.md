
[![Coverage Status](https://coveralls.io/repos/github/kelvinrandu/My-diary-api/badge.svg?branch=develop)](https://coveralls.io/github/kelvinrandu/My-diary-api?branch=develop)
[![Build Status](https://travis-ci.org/kelvinrandu/My-diary-api.svg?branch=Develop-API-v1)](https://travis-ci.org/kelvinrandu/My-diary-api)
# My-diary-api-v1
A restful app intended to communicate using api endpoints
## DESCRIPTION
My-diary-api is a restful api intended to communicate with a front end of your choice using various api endpoints.
The api endpoints are meant to do the following
- register a user
- login a user
- post entries 
- fetch entries 
- delete an  entry 
- modify an entry 

## REQUIREMENTS
Minimum requirements needed to run this application include;
- [pip](https://packaging.python.org/tutorials/installing-packages/)
- [python3](https://www.python.org/getit/)
- [postgres](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)

## RUNNING THE APPLICATION
- clone [this](https://github.com/kelvinrandu/My-diary-api.git) repository
- navigate to the project directory
- install virtual environment
```virtualenv -p python3 venv ```
- activate the virtual environment
```$ source venv/bin/activate```
- install dependencies needed for the project to run
``` $ pip install -r requirements.txt ```
- install flask
``` $ pip install flask```
- create database in postgres and configure with details in database.py
- run the application
``` $ flask run ```
## API ROUTES

| Methods        | Url          | Description |
| ------------- |:-------------:| -----:|
| POST   | https://mydiary-api-v1.herokuapp.com/api/v1/login           |  login                            | 
| POST   | https://mydiary-api-v1.herokuapp.com/api/v1/register           |  register                           | 
| GET     | https://mydiary-api-v1.herokuapp.com/api/v1/entries           |  Fetches all diary entries |           
| GET     | https://mydiary-api-v1.herokuapp.com/api/v1/entries/<int:id>  |  Fetches a single diary entry    |
| POST    | https://mydiary-api-v1.herokuapp.com/api/v1/entries           |  Creates a new diary entry       |
| PUT     | https://mydiary-api-v1.herokuapp.com/api/v1/entries/<int:id>  |   Modifies an entry              |
| DELETE  | https://mydiary-api-v1.herokuapp.com/api/v1/entries/<int:id>  |   Deletes an entry from my Diary |

## TESTING THE APP
Postman was the main application used in test the endpoints using the routes provided below
ans a snip of the response upon successful request 

- login
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/develop/images/api/login-api.png)

- register
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/develop/images/api/register-api.png)

- fetch all  diary entries
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/develop/images/api/getall.png)

- fetch a single diary entry
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/develop/images/api/geteach-api.png)

- post an entry into my diary
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/develop/images/api/postapi.png) 

- modify a single diary entry  
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/develop/images/api/edit.png)
- delete an entry from my diary
![alt text](https://github.com/kelvinrandu/My-diary-api/blob/develop/images/api/delete.png)


## RUN TEST
To run unitests type the code below in your terminal in your root folder
``` $ pytest ```
