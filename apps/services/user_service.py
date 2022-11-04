from apps.models.exception import AppException
from apps.models.user import User

ALL_USERS=[]

def get_all_users():
    global ALL_USERS
    return ALL_USERS

def update_user(user:User):
    global ALL_USERS
    ALL_USERS = list(filter(lambda u:u.id!=user.id,ALL_USERS))
    ALL_USERS.append(user)

def get_user(user_id:str)->User:
    for u in get_all_users():
        if u.id==user_id:
            return u
    return None

