import requests

def create_user():

    return requests.post('http://127.0.0.1:5000/register',json = {
                "name" : "pablo",
                "email" : "pablo@.pablocom",
                "password" : "1234"
        })

def create_user_erros():

    return requests.post('http://127.0.0.1:5000/register',json = {
                "name" : "pablo",
                "password" : "1234"
        })