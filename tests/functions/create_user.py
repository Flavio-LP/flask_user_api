import requests

def create_user():

    return requests.post('http://127.0.0.1:5000/register',json = {
                "name" : "joana",
                "email" : "joana@joana.com",
                "password" : "1234"
        })