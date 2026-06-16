def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    return "Login Failed"

print(login("admin", "1234"))
