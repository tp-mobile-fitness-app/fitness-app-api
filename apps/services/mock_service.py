import datetime
from apps.models.gym.gym import Gym, GymClass
from apps.models.user import User
import apps.services.gym_service as gym_service
import apps.services.user_service as user_service

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

    class1 = GymClass.from_dict({
        "id":1,
        "start_date":datetime.datetime(2022,10,6,17,30),
        "end_date":datetime.datetime(2022,10,6,19,0),
        "professor":"pirulo",
        "type":"yoga",
        "max_capacity":12
    })
    class2 = GymClass.from_dict({
        "id":2,
        "start_date":datetime.datetime(2022,10,21,11,0),
        "end_date":datetime.datetime(2022,10,21,12,0),
        "professor":"gonzalito",
        "type":"clase privada",
        "max_capacity":1
    })
    class3 = GymClass.from_dict({
        "id":3,
        "start_date":datetime.datetime(2022,10,16,14,0),
        "end_date":datetime.datetime(2022,10,16,17,0),
        "professor":"profesor x",
        "type":"x men first class",
        "max_capacity":3
    })

    gym1 = Gym.from_dict({
        "id":1,
        "name":"el gym de lo pibe",
        "location": {
            "latitude":19,
            "longitude":28
        }
    })
    gym2 = Gym.from_dict({
        "id":2,
        "name":"golds gym",
        "location": {
            "latitude":81,
            "longitude":72
        }
    })

    gym1.classes.append(class1)
    gym1.classes.append(class2)
    gym2.classes.append(class3)

    gym_service.ALL_GYMS = [gym1,gym2]
    user_service.ALL_USERS = [user1,user2,user3]