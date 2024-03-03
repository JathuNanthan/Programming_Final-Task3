# authentication.py

def sign_in(username, password):
    # Dictionary to store username-password pairs for each employee
    credentials = {
        "E001": "password1",
        "E002": "password2",
        "E003": "password3",
    }

    # Check if input credentials match stored credentials
    if username in credentials and password == credentials[username]:
        return True
    else:
        return False
