from fastapi import APIRouter

import apps.configs.configuration as var
from apps.utils.logger_util import get_logger
from apps.models.exception import AppException

blue_print = APIRouter(prefix='')

logger = get_logger()


@blue_print.get('/vars')
def variables():
    return var.variables_cargadas()


@blue_print.get('/errors')
def error():
    raise AppException('PRUEBA', 'No Wanda Nara!')


@blue_print.get('/alive')
def vivo():
    logger.info("VIVO")
    return {"estado": "vivo"}