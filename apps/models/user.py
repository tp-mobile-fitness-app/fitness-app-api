from typing import List
from apps.models.exception import AppException
from apps.models.gym.gym import GymClass
from pydantic import BaseModel

class User(BaseModel):
    id : str = None
    name: str
    phone : str
    age : int = None
    mail : str = None
    classes : List[GymClass] = []

    def schedule(self,gym_class:GymClass):
        for c in self.classes:
            if c.collides(gym_class):
                raise AppException(409,"Clase ocurre en un horario ya reservado")
                
        self.classes.append(gym_class)

    def to_dict(self):
        return {
            "id" :self.id,
            "name": self.name,
            "phone" :self.phone,
            "age" :self.age,
            "mail" :self.mail
        }

    def from_dict(spec):
        return User(**spec)