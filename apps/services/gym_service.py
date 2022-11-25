from apps.models.exception import AppException
from apps.models.gym.gym_search import GymSearch
from apps.models.gym.gym import Gym, GymClass
from apps.models.user import User
import apps.services.user_service as user_service

ALL_GYMS=[]

def get_all_gyms():
    global ALL_GYMS
    return ALL_GYMS

def update_gym(gym:Gym):
    global ALL_GYMS
    ALL_GYMS = list(filter(lambda g:g.id!=gym.id,ALL_GYMS))
    ALL_GYMS.append(gym)

def get_gyms(search:GymSearch):
    gyms = get_all_gyms()

    return list(filter(lambda g: search.matches(g),gyms))

def get_gym(gym_id:str)->Gym:
    for g in get_all_gyms():
        if g.id==gym_id:
            return g
    return None

def get_image(gym_id:str)->str:
    return get_gym(gym_id).image

def get_gym_class(gym_id,class_id):
    return list(filter(lambda c:c.id==class_id,get_gym(gym_id).classes))[0]

def update_gym_class(gym_id,gym_class:GymClass):
    global ALL_GYMS
    gym = get_gym(gym_id)
    gym.classes = list(filter(lambda c:c.id!=gym_class.id,gym.classes))
    gym.classes.append(gym_class)

    update_gym(gym)

def reserve(gym_id,class_id,user:User):
    gym_class = get_gym_class(gym_id,class_id)

    if gym_class.has_spot():
        gym_class.reserve_place(user)
        user.schedule(gym_class)
        update_gym_class(gym_id,gym_class)
        user_service.update_user(user)
    else:
        raise AppException(409,"No hay lugar disponible en la clase")

def unbook(gym_id,class_id,user:User):
    gym_class = get_gym_class(gym_id,class_id)

    user.unschedule(gym_class)
    gym_class.unbook_place(user)

    update_gym_class(gym_id,gym_class)
    user_service.update_user(user)

