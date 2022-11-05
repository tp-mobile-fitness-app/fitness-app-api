from fastapi import APIRouter
from apps.utils.rest_util import get_valid_rest_object
import apps.services.user_service as user_service

import apps.configs.configuration as conf
from apps.configs.vars import Vars
from apps.models.gym.gym import GymClass
from apps.models.user import User
from typing import List
from apps.services.mock_service import load_data

URI = "/mocks"
VERSION = "/v1"


blue_print = APIRouter(prefix=conf.get(Vars.API_BASE_PATH)+VERSION+URI,tags=["mocks"])


@blue_print.get('/init')
def init():
    load_data()
    return get_valid_rest_object({})