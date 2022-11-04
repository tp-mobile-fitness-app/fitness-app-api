from apps.utils.rest_util import get_valid_rest_object,get_body
from apps.models.gym.gym_search import GymSearch
import apps.services.gym_service as gym_service
import apps.services.user_service as user_service
from fastapi import APIRouter
from fastapi import Request
from typing import List
from apps.models.gym.gym import GymClass,Gym
from apps.models.gym.reservation import Reservation


import apps.configs.configuration as conf
from apps.configs.vars import Vars

URI = "/gyms"
VERSION = "/v1"

blue_print = APIRouter(prefix=conf.get(Vars.API_BASE_PATH)+VERSION+URI)


@blue_print.get('', response_model=List[Gym])
def get_gyms():
    return get_valid_rest_object(gym_service.get_all_gyms())

@blue_print.post('/search', response_model=List[Gym])
def gym_search(search:GymSearch):
    return get_valid_rest_object(gym_service.get_gyms(search))

@blue_print.get('/{gym_id}/classes', response_model=List[GymClass])
def get_classes(gym_id):
    gym = gym_service.get_gym(gym_id)

    return get_valid_rest_object(gym.classes)

@blue_print.post('/{gym_id}/classes/{class_id}/reserve')
def reserve_class(gym_id,class_id,reservation:Reservation):

    user = user_service.get_user(reservation.user_id)

    gym_service.reserve(gym_id,class_id,user)

    return get_valid_rest_object({})