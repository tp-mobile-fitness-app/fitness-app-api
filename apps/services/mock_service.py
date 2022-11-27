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
        "professor":"Pirulo",
        "type":"Yoga",
        "description":"INTEGRAL YOGA: Combines different styles of yoga. I invite you to listen, discover and expand spaces within. We will transit Asanas, Pranayamas and relaxation.",
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
        "professor":"Gonzalito",
        "description":"I offer Hapkido classes (traditional martial art) focused on the defense and personal development of each student.",
        "type":"Private Class",
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
        "professor":"Professor X",
        "description":"Middle zone group training, some Pilates and yoga exercises, flexibility and joint mobility.",
        "type":"X Men First Class",
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
        "professor":"Romina Martinez",
        "description":"Learn Tae bo and become a more confident person of yourself.",
        "type":"Tae Bo",
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
        "professor":"Julian Alvarez",
        "description":"Recreational Box or MMA + Functional. Learn to be a warrior and take care of your physical condition intelligently and with permanent results.",
        "type":"Boxing",
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
        "professor":"Susana Gimenez",
        "description":"Classes with varied activities to exercise the body in Home Office times.",
        "type":"Posture Gymnastics",
        "max_capacity":30
    })

    gym1 = Gym.from_dict({
        "id":1,
        "name":"The kid's Gym",
        "image":image_b64(f"{FILES_PATH}/gym1.jpg"),
        "location": {
            "latitude":random_latitude(),
            "longitude":random_longitude()
        },
        "description": "The kids' gym, for the kids",
        "contact_info":"Tel: 01157453846 Mail: kidsgym@gmail.com"
    })
    gym2 = Gym.from_dict({
        "id":2,
        "name":"Golds gym",
        "image":image_b64(f"{FILES_PATH}/gym2.jpg"),
        "location": {
            "latitude":random_latitude(),
            "longitude":random_longitude()
        },
        "description": "The gym for the elite of the elite.",
        "contact_info":"Tel: 01157986138 Mail: golds@gmail.com"
    })
    gym3 = Gym.from_dict({
        "id":3,
        "name":"Gym 24/7",
        "image":image_b64(f"{FILES_PATH}/gym3.jpg"),
        "location": {
            "latitude":random_latitude(),
            "longitude":random_longitude()
        },
        "description": "Get your desired physique, become 1% of the population.",
        "contact_info":"Tel: 01158369264 Mail: seveneleven.gym@gmail.com"
    })
    
    gym4 = Gym.from_dict({
        "id":4,
        "name":"Mario Gym Bros",
        "image":image_b64(f"{FILES_PATH}/gym4.jpg"),
        "location": {
            "latitude":90,
            "longitude":70
        },
        "description": "Save the princess, become Donkey Kong.",
        "contact_info":"Tel: 01152936485 Mail: bros.gym@gmail.com"
    })

    gym5 = Gym.from_dict({
        "id":5,
        "name":"Goku gym",
        "image":image_b64(f"{FILES_PATH}/gym5.jpg"),
        "location": {
            "latitude":random_latitude(),
            "longitude":random_longitude()
        },
        "description": "Gather all your forces, only for high-class warriors.",
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