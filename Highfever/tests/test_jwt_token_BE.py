import requests
import jwt
import os
from config.config import coffee_maker_service
from config.config import wrong_coffee_maker_service
from config.config import client_email
from config.config import token_has_expired_text


class TestJwtTokenBE:

    def test_valid_token(self):
        """By using GET request api call
        we want to verify valid status code of "200 OK"
        in this way we show that the user is in the
        database with the token that is in the session

        1.Set valid url endpoint
        2.Create valid token and send get request
        3.Assert proper API condition(Status code = 200)
        4.Confirm if the user is in the db
        """
        # Create valid token
        encoded_valid_jwt = jwt.encode({"User": "Admin", "sub": "id=4", "auth": ["Admin"]}, os.environ.get('SECRET_KEY'))
        # Set token
        headers = {'Authorization': f'Bearer {encoded_valid_jwt}'}
        # Set valid url endpoint and send request
        response = requests.get(coffee_maker_service, headers=headers)
        json_response = response.json()
        print(json_response)
        # # Confirm if the user is in the db
        assert client_email == json_response['email']
        # # # Assert proper API condition(Status code = 200)
        assert response.status_code == 200

    def test_expired_token(self):
        """The user is on db, but he owns
        an expired token
        By using GET request api call
        we want to verify valid status code of "401 Unauthorized Error"

        1.Set valid url endpoint
        2.Create expired token and send get request
        3.Assert proper API condition(Status code = 401)
        4.Assert proper message("The token has expired")
        """
        # Create expired token
        jwt_exp = jwt.encode({"User": "Admin", "sub": "id=2", "auth": ["Admin"], "exp": 1663934539}, os.environ.get('SECRET_KEY'))
        # Set token
        headers = {'Authorization': f'Bearer {jwt_exp}'}
        print(headers)
        # # Set valid url endpoint and send request
        response = requests.get(coffee_maker_service, headers=headers)
        json_response = response.json()
        # Assert proper message("The token has expired")
        assert token_has_expired_text == json_response['message']
        # # Assert proper API condition(Status code = 401)
        assert response.status_code == 401

    def test_token_not_found(self):
        """The user is on the db,
        but no token has been generated yet
        By using GET request api call
        we want to verify valid status code of "401 Unauthorized Error"

        1.Set valid url endpoint
        2.Send request without any token forwarded
        3.Assert proper API condition(Status code = 401)
        4.Assert proper message("No bearer token found")
        """

        # we won't send any token at this point, just send request
        response = requests.get(coffee_maker_service)
        json_response = response.json()
        # Assert proper message("No bearer token found")
        assert 'No bearer token found' == json_response['message']
        # Assert proper API condition(Status code = 401)
        assert response.status_code == 401

    def test_invalid_token(self):
        """By using GET request api call
        we want to verify valid status code of "401 Unauthorized Error "
        in this way we show that the user is in the
        database but that the token is simply not valid

        1.Set valid url endpoint
        2.Send get request with invalid token
        3.Assert proper API condition(Status code = 401)
        4.Assert proper message("Invalid token.")
        """
        # Create valid token
        invalid_jwt = jwt.encode({"sub": "1234567890", "name": "John Doe"}, os.environ.get('SECRET_KEY'))
        # wrong token value manually entered
        headers = {'Authorization': f'Bearer {invalid_jwt}'}
        # Send get request with invalid token
        response = requests.get(coffee_maker_service, headers=headers)
        json_response = response.json()
        assert 'Invalid token.' == json_response['message']
        # Assert proper API condition(Status code = 401)
        assert response.status_code == 401

    def test_wrong_endpoint(self):
        """Checking are we getting code error 404 NOT FOUND: in case
        we send wrong URL address and valid token

        1.Set wrong endpoint address
        2.Create valid token and send get request
        3.Assert proper API condition(Status code = 400)
        4.Assert proper message("Bad request")
        """
        # Create valid token
        valid_jwt = jwt.encode({"User": "Admin", "sub": "id=2", "auth": ["Admin"]}, os.environ.get('SECRET_KEY'))
        # Set token
        headers = {'Authorization': f'Bearer {valid_jwt}'}
        # url is wrong as it's should be
        response = requests.get(wrong_coffee_maker_service, headers=headers)
        json_response = response.json()
        # Assert proper message("Bad request")
        assert 'Bad Request' == json_response['error']
        # Assert proper API condition(Status code = 400)
        assert response.status_code == 400

