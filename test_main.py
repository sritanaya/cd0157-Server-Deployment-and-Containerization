'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'myjwtsecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Njg5OTg4MzcsIm5iZiI6MTY2Nzc4OTIzNywiZW1haWwiOiJhYmNAeHl6LmNvbSJ9.Y2T-ru7IVp4PGTH7FU1YC2zbLHGdhCnCW0t58RHWBmY'
EMAIL = 'abc@xyz.com'
PASSWORD = 'WindowsPwd'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
