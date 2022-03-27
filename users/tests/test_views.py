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

def test_right_user_login_get(client,f_user):
    url = reverse('users-api:login')
    data = {'username': 'hima','password': 'himahima'}
    response = client.get(url)
    assert response.status_code == 200

def test_wrong_user_login(client,f_user):
    url = reverse('users-api:login')
    data = {'username': 'hima2','password': 'himahima'}
    response = client.post(url,data=data)
    assert response.status_code == 200
    
def test_users(client,f_user):
    url = reverse('users-api:users')
    client.force_login(f_user)
    response = client.get(url)
    assert response.status_code == 200
    # list of users
    assert response.data[0]['username'] == 'hima'

def test_user_update(client,f_user):
    url = reverse('users-api:user-update',args=[f_user.id])
    client.force_login(f_user)
    response = client.get(url)
    assert response.data['username'] == 'hima'
    assert response.status_code == 200

def test_user_update(client,f_user):
    url = reverse('users-api:user-update',args=[f_user.id])
    data = {'email': 's@s.com'}
    client.force_login(f_user)
    response = client.patch(url,data=data)
    pprint(vars(response))
    assert response.status_code == 200