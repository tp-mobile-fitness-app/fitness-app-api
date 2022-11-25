from datetime import datetime
from typing import List
from apps.models.location import Location
from apps.models.schedule import Schedule
from pydantic import BaseModel


class GymClass(BaseModel):
    id : str = None
    gym_id : str = None
    schedules: List[Schedule] = [] 
    professor : str
    type : str
    description: str = ""
    max_capacity : int = 1
    people : int = 0

    def has_spot(self)->bool:
        return self.people<self.max_capacity

    def reserve_place(self,user):
        self.people+=1
        
    def unbook_place(self,user):
        self.people-=1

    def collides(self,other_class:"GymClass"):
        collide = True
        for s in self.schedules:
            collide = collide and any(s.collides(s2) for s2 in other_class.schedules)
        return collide

    def to_dict(self):
        return {
            "id": self.id ,
            "gym_id": self.gym_id ,
            "professor": self.professor ,
            "type": self.type ,
            "description":self.description,
            "max_capacity": self.max_capacity,
            "schedules": [s.to_dict() for s in self.schedules],
            "people": self.people
        }
    
    def from_dict(spec:dict):
        spec["schedules"] = [Schedule.from_dict(s) for s in spec.get("schedules",[])]
        return GymClass(**spec)

class Gym(BaseModel):
    id : str = None
    name : str
    location : Location
    image : str = None
    classes : List[GymClass] = []

    def add_class(self,some_class:GymClass):
        some_class.gym_id = self.id
        self.classes.append(some_class)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location.to_dict()
        }
    
    def from_dict(spec:dict):
        spec["classes"] = [GymClass.from_dict(c) for c in spec.get("classes",[])]
        return Gym(**spec)
