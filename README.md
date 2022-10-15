# fitness-app-api

`pipenv install` para instalar las dependencias en un ambiente virtual.
`pipenv shell` para arrancar una shell dentro del ambiente virtual.

_Dev:_ `uvicorn src.main:app --reload`
- Ejecuta la aplicacion y se recarga cuando detecta alguna modificación en el codigo.

_Prod:_ `uvicorn src.main:app`
- Ejecuta la aplicacion.


#### Endpoints Utiles:

- _/redoc_ - Muestra documentación para todos los endpoints definidos por la aplicación.
- _/docs_ - Provee una interfaz para testear cada uno de los endpoints definidos.
