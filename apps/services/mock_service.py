from apps.models.gym.gym import Gym, GymClass
from apps.models.schedule import Schedule
from apps.models.user import User
import apps.services.gym_service as gym_service
import apps.services.user_service as user_service
import random
import base64
from pydantic import BaseModel
from typing import List

FILES_PATH="files"



class GymClassMock(BaseModel):
    ids : str = None
    gym_id : str = None
    schedules: List[Schedule] = [] 
    professor : str
    type : str
    description: str = ""
    max_capacity : int = 1
    people : int = 0

    def to_gym_classes(self):
        classes = []
        for i,s in enumerate(self.schedules):
            id = self.ids.split(",")[i]
            classes.append(self.new_gym_class(id,s))
        return classes

    def new_gym_class(self,id:str,schedule:Schedule):
        self_dict = self.to_dict()
        self_dict["id"] = id
        self_dict["schedule"] = schedule.to_dict()

        return GymClass.from_dict(self_dict)

    def to_dict(self):
        return {
            "gym_id": self.gym_id ,
            "professor": self.professor ,
            "type": self.type ,
            "description":self.description,
            "max_capacity": self.max_capacity,
            "people": self.people
        }
    
    def from_dict(spec:dict):
        spec["schedules"] = [Schedule.from_dict(s) for s in spec["schedules"]]
        return GymClassMock(**spec)

def image_b64(image):
    with open(image, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string

def random_latitude():
    return -round(random.uniform(34.572937,34.621192), 6)

def random_longitude():
    return -round(random.uniform(58.368067,58.532347), 6)

def load_data():
    user1 = User.from_dict({
        "id":1,
        "name":"Jesus Ferrere",
        "phone":"115849374",
        "age":21,
        "mail":"yisus@gmail.com"
    })
    user2 = User.from_dict({
        "id":2,
        "name":"Seitan Vegano",
        "phone":"11584212",
        "age":24,
        "mail":"seitan@gmail.com"
    })
    user3 = User.from_dict({
        "id":3,
        "name":"Nicolas Slash",
        "phone":"115736374",
        "age":39,
        "mail":"guitarhero@gmail.com"
    })

    class1 = GymClassMock.from_dict({
        "ids":"1,2",
        "schedules":[
            {
                "start_hour":12,
                "end_hour":13.50,
                "week_day":5
            },
            {
                "start_hour":18.10,
                "end_hour":20,
                "week_day":2
            }
        ],
        "professor":"pirulo",
        "type":"yoga",
        "description":"YOGA INTEGRAL: Auna diferentes estilos de yoga. Los invito a escucharse, descubrir y ampliar espacios en su interior. Transitaremos Asanas, Pranayamas y relajacion.",
        "max_capacity":12
    })
    class2 = GymClassMock.from_dict({
        "ids":"3,4,5",
            "schedules":[
            {
                "start_hour":9,
                "end_hour":10.30,
                "week_day":1
            },
            {
                "start_hour":21,
                "end_hour":22,
                "week_day":3
            },
            {
                "start_hour":14,
                "end_hour":16,
                "week_day":5
            }
        ],
        "professor":"gonzalito",
        "description":"Ofrezco clases de Hapkido (arte marcial tradicional) enfocado a la defensa y al desarrollo personal de cada alumno.",
        "type":"clase privada",
        "max_capacity":1
    })
    class3 = GymClassMock.from_dict({
        "ids":"6",
        "schedules":[
            {
                "start_hour":10,
                "end_hour":11.10,
                "week_day":6
            },
        ],
        "professor":"profesor x",
        "description":"Entrenamiento grupal de zona media, algunos ejercicios de pilates y yoga, flexibilidad y movilidad articular.",
        "type":"x men first class",
        "max_capacity":3
    })
    class4 = GymClassMock.from_dict({
        "ids":"7",
        "schedules":[
            {
                "start_hour":10,
                "end_hour":11.10,
                "week_day":6
            },
        ],
        "professor":"romina martinez",
        "description":"Aprende Tae bo y convertite en una persona mas segura de vos mismo.",
        "type":"tae bo",
        "max_capacity":20
    })
    class5 = GymClassMock.from_dict({
        "ids":"8",
        "schedules":[
            {
                "start_hour":20,
                "end_hour":21,
                "week_day":2
            },
        ],
        "professor":"julian alvarez",
        "description":"Box Recreativo o MMA + Funcional. Aprende a ser un guerrero y cuidar tu estado fisico de forma inteligente y con resultados permanentes.",
        "type":"boxeo",
        "max_capacity":10
    })

    class6 = GymClassMock.from_dict({
        "ids":"9",
        "schedules":[
            {
                "start_hour":15,
                "end_hour":16.5,
                "week_day":5
            },
        ],
        "professor":"susana gimenez",
        "description":"Clases con actividades variadas para ejercitar el cuerpo en tiempos de Home Office.",
        "type":"gimnasia postural",
        "max_capacity":30
    })

    gym1 = Gym.from_dict({
        "id":1,
        "name":"el gym de lo pibe",
        "image":image_b64(f"{FILES_PATH}/gym1.jpg"),
        "location": {
            "latitude":random_latitude(),
            "longitude":random_longitude()
        },
        "description": "El gym de los pibe, para los pibe",
        "contact_info":"Tel: 01157453846 Mail: lopibe@gmail.com"
    })
    gym2 = Gym.from_dict({
        "id":2,
        "name":"golds gym",
        "image":image_b64(f"{FILES_PATH}/gym2.jpg"),
        "location": {
            "latitude":random_latitude(),
            "longitude":random_longitude()
        },
        "description": "Consegui tu fisico deseado, convertite en el 1% de la poblacion.",
        "contact_info":"Tel: 01157986138 Mail: golds@gmail.com"
    })
    gym3 = Gym.from_dict({
        "id":3,
        "name":"gym 24/7",
        "image":image_b64(f"{FILES_PATH}/gym3.jpg"),
        "location": {
            "latitude":random_latitude(),
            "longitude":random_longitude()
        },
        "description": "Cuando quieras, donde quieras. El gym que te acompaña a todos lados.",
        "contact_info":"Tel: 01158369264 Mail: seveneleven.gym@gmail.com"
    })
    
    gym4 = Gym.from_dict({
        "id":4,
        "name":"mario gym bros",
        "image":image_b64(f"{FILES_PATH}/gym4.jpg"),
        "location": {
            "latitude":90,
            "longitude":70
        },
        "description": "Salva a la princesa, convertite en donkey kong.",
        "contact_info":"Tel: 01152936485 Mail: bros.gym@gmail.com"
    })

    gym5 = Gym.from_dict({
        "id":5,
        "name":"gimnasio goku",
        "image":image_b64(f"{FILES_PATH}/gym5.jpg"),
        "location": {
            "latitude":random_latitude(),
            "longitude":random_longitude()
        },
        "description": "Junta todas tus fuerzas, solo para guerreros de clase alta.",
        "contact_info":"Tel: 01153574954 Mail: saiyan.gym@gmail.com"
    })

    for c in class1.to_gym_classes():
        gym1.add_class(c) 
    for c in class2.to_gym_classes():
        gym1.add_class(c) 
    for c in class3.to_gym_classes():
        gym2.add_class(c) 
    for c in class4.to_gym_classes():
        gym3.add_class(c) 
    for c in class5.to_gym_classes():
        gym4.add_class(c) 
    for c in class6.to_gym_classes():
        gym5.add_class(c) 

    gym_service.ALL_GYMS = [gym1,gym2,gym3,gym4,gym5]
    user_service.ALL_USERS = [user1,user2,user3]