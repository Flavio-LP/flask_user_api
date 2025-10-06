import requests


def user_login():
        return requests.post('http://127.0.0.1:5000/login',json = {
            "email" : "carlos@carlos.com",
            "password" : "1234"
        })

def user_login_invalid():
        return requests.post('http://127.0.0.1:5000/login',json = {
            "email" : "joao@joao.com",
            "password" : "12341"
        })

def user_login_error():
        return requests.post('http://127.0.0.1:5000/login',json = {
            "email" : "joao@joao.com"
        })

def user_login_notfound():
        return requests.post('http://127.0.0.1:5000/login',json = {
            "email" : "fabio@fabio.com",
            "password" : "12341"
        })