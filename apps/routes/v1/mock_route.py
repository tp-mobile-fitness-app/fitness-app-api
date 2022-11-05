from fastapi import APIRouter
from apps.utils.rest_util import get_valid_rest_object

import apps.configs.configuration as conf
from apps.configs.vars import Vars
from apps.services.mock_service import load_data

URI = "/mocks"
VERSION = "/v1"


blue_print = APIRouter(prefix=conf.get(Vars.API_BASE_PATH)+VERSION+URI,tags=["mocks"])


@blue_print.get('/init')
def init():
    load_data()
    return get_valid_rest_object({})