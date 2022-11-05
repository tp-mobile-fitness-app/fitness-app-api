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
        "max_capacity":12
    })
    class2 = GymClass.from_dict({
        "id":2,
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
        "type":"clase privada",
        "max_capacity":1
    })
    class3 = GymClass.from_dict({
        "id":3,
        "schedules":[
            {
                "start_hour":10,
                "end_hour":11.10,
                "week_day":6
            },
        ],
        "professor":"profesor x",
        "type":"x men first class",
        "max_capacity":3
    })
    class4 = GymClass.from_dict({
        "id":4,
        "schedules":[
            {
                "start_hour":10,
                "end_hour":11.10,
                "week_day":6
            },
        ],
        "professor":"romina martinez",
        "type":"tae bo",
        "max_capacity":20
    })
    class5 = GymClass.from_dict({
        "id":5,
        "schedules":[
            {
                "start_hour":20,
                "end_hour":21,
                "week_day":2
            },
        ],
        "professor":"julian alvarez",
        "type":"boxeo",
        "max_capacity":10
    })

    class6 = GymClass.from_dict({
        "id":6,
        "schedules":[
            {
                "start_hour":15,
                "end_hour":16.5,
                "week_day":5
            },
        ],
        "professor":"susana gimenez",
        "type":"gimnasia postural",
        "max_capacity":30
    })

    gym1 = Gym.from_dict({
        "id":1,
        "name":"el gym de lo pibe",
        "location": {
            "latitude":70,
            "longitude":70
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
    gym3 = Gym.from_dict({
        "id":3,
        "name":"gym 24/7",
        "location": {
            "latitude":90,
            "longitude":72
        }
    })
    
    gym4 = Gym.from_dict({
        "id":4,
        "name":"mario gym bros",
        "location": {
            "latitude":90,
            "longitude":70
        }
    })

    gym5 = Gym.from_dict({
        "id":5,
        "name":"gimnasio goku",
        "location": {
            "latitude":80,
            "longitude":90
        }
    })

    gym1.classes.append(class1)
    gym1.classes.append(class2)
    gym2.classes.append(class3)
    gym3.classes.append(class4)
    gym4.classes.append(class5)
    gym5.classes.append(class6)

    gym_service.ALL_GYMS = [gym1,gym2,gym3,gym4,gym5]
    user_service.ALL_USERS = [user1,user2,user3]