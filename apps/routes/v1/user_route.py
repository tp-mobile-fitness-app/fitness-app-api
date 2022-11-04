from http import HTTPStatus

from fastapi import APIRouter
from apps.utils.rest_util import get_valid_rest_object
import apps.services.user_service as user_service

import apps.configs.configuration as conf
from apps.configs.vars import Vars

URI = "/users"
VERSION = "/v1"


blue_print = APIRouter(prefix=conf.get(Vars.API_BASE_PATH)+VERSION+URI)


@blue_print.get('/<user_id>/classes')
def get_user_classes(user_id):
    user = user_service.get_user(user_id)
    return get_valid_rest_object(user.classes)