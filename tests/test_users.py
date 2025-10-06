from functions.create_user import create_user, create_user_erros
from functions.user_login import user_login, user_login_invalid, user_login_error, user_login_notfound
from functions.user_list import list_users

def test_create_user():
    req = create_user()
    assert req.status_code == 201

def test_user_exists():
    req = create_user()
    assert req.status_code == 409

def test_user_error():
    req = create_user_erros()
    assert req.status_code == 400
def test_user_login():
    req = user_login()
    assert req.status_code == 200    

def test_user_login_invalid():
    req = user_login_invalid()
    assert req.status_code == 401    

def test_user_login_error():
    req = user_login_error()
    assert req.status_code == 400    

def test_user_login_notfound():
    req = user_login_notfound()
    assert req.status_code == 404  

def test_list_users():
    req = list_users()
    assert req.status_code == 200

def test_list_users_error_exp():
    req = list_users()
    assert req.status_code == 498

def test_list_users_error():
    req = list_users()
    assert req.status_code == 404    