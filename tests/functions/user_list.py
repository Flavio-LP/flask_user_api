import requests

def list_users():
    return requests.post('http://127.0.0.1:5000/users',json={
        "email" : "carlos@carlos.com"
    })

def list_users_error_exp():
    return requests.post('http://127.0.0.1:5000/users',json={
        "email" : "joao@joao.com"
    })

def list_users_error():
    return requests.post('http://127.0.0.1:5000/users',json={
        "email" 
    })