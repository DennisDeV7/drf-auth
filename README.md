# LAB - Class 33

## Project: Authentication and Production Server

## Author: Dennis DeVries

### Setup

To runserver on linux: sudo docker compose up --build

To run tests:

    - Get into docker container: `sudo docker compose run web bash`
    - `python  manage.py test`

I tested web responses with thunderclient first using a POST

- `http://localhost:8000/api/token/`
- the JSON content should look as follows: {"username":"username_here","password":"your_password_here"}

I then tested the GET response with:

- `http://localhost:8000/api/v1/dogs/`
- input the access token that was output by the previous test
