import json
from pprint import pprint
import pytest
from django.urls import reverse
from .factories import UserFactory




def test_right_user_register(client,f_user):
    url = reverse('users-api:register')
    data = {'username': 'fifth','email': 't@t.com','password': 'password1','role': 'buyer','deposit': '0'}
    response = client.post(url,data=data)
    assert response.status_code == 201

def test_wrong_user_register(client,f_user):
    url = reverse('users-api:register')
    # wrong password field
    data = {'username': 'hello','email': 't@t.com','password1': 'password1','role': 'buyer','deposit': '0'}
    response = client.post(url,data=data)
    assert response.status_code == 400

