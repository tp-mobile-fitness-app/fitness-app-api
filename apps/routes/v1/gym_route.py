from http import HTTPStatus

from apps.utils.rest_util import get_valid_rest_object,get_body
from apps.models.gym.gym_search import GymSearch
import apps.services.gym_service as gym_service
import apps.services.user_service as user_service
from fastapi import APIRouter
from fastapi import Request, FastAPI



import apps.configs.configuration as conf
from apps.configs.vars import Vars

URI = "/gyms"
VERSION = "/v1"

blue_print = APIRouter(prefix=conf.get(Vars.API_BASE_PATH)+VERSION+URI)


@blue_print.get('')
def get_gyms():
    return get_valid_rest_object(gym_service.get_all_gyms())

@blue_print.post('/search')
def gym_search(search:GymSearch):
    return get_valid_rest_object(gym_service.get_gyms(search))

@blue_print.get('/{gym_id}/classes')
def get_classes(gym_id):
    gym = gym_service.get_gym(gym_id)

    return get_valid_rest_object(gym.classes)

@blue_print.post('/{gym_id}/classes/{class_id}/reserve')
def reserve_class(gym_id,class_id,request:Request):
    body = get_body(request)

    user_id = body["user_id"]
    user = user_service.get_user(user_id)

    gym_service.reserve(gym_id,class_id,user)

    return get_valid_rest_object({})