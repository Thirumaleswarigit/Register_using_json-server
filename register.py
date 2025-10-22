import requests as r

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm_password = input("Enter confirm password: ")
    email = input("Enter email: ")

    if password != confirm_password:
        print("Passwords do not match!")
        return

    users = r.get("http://localhost:4000/posts").json()
    for user in users:
        if user["username"] == username:
            print("Username already exists!")
            register_user()
            

    data = {
        "username": username,
        "password": password,
        "conformpassword": confirm_password,
        "email": email
    }

    res = r.post("http://localhost:4000/posts", json=data)
    print("User registered successfully!")
    print(res.text)


register_user()
