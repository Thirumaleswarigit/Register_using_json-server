import requests as r
import json

def get_user_details():
    username = input("Enter username: ")
    
    res = r.get("http://localhost:4000/posts", params={"username": username})
    users = res.json()
    
    if users:
        user = users[0]
        print(json.dumps(user, indent=4))
    else:
        print("Username not found. Please register properly.")
get_user_details()
