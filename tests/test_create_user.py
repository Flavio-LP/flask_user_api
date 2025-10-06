from functions.create_user import create_user

def test_create_user():
    req = create_user()
    assert req.status_code == 201

def test_user_exists():
    req = create_user()
    assert req.status_code == 409