import json
import os

import apps.configs.configuration as conf
from apps.configs.vars import Vars
import apps.services.mock_service as mock_service
from fastapi import FastAPI
from apps.utils.blueprint_util import registrar_blue_prints

app = FastAPI()

registrar_blue_prints(app, 'apps/routes')

mock_service.load_data()

if __name__ == '__main__':

    possible_ports = [int(conf.get(Vars.API_PORT)), 80, 5000]

    for port in possible_ports:
        try:
            app.run(debug=conf.get(Vars.DEBUG_MODE),
                    host=conf.get(Vars.API_HOST), port=port)
            break
        except:
            continue
