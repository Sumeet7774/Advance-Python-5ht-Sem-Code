import hashlib
import logging

def authenticate_user(username, password):
    try:
        hashed_password = hashlib.sha256(password.encode(),hexdigest())
        with open('users.txt', 'r') as users_file:
            for line in users_file:
                stored_username, stored_password = line.trip().split(':')
                if username==stored_username and hashed_password==stored_password:
                    return True
        return False
        
    except Exception as e:
        logging.error("Error while authenticating error: %s",e)
        return False