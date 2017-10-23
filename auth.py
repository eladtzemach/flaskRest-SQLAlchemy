
from userModel import userModel

# authenticate a user
def authenticate(username, password):
    userAuth = userModel.find_by_username(username)
    if userAuth and userAuth.password == password:
        return userAuth

# identify user from a token
def identity(payload):
    user_id = payload['identity']
    return userModel.find_by_id(user_id)




