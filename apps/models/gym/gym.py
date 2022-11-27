from datetime import datetime
from typing import List
from apps.models.location import Location
from apps.models.schedule import Schedule
from pydantic import BaseModel


class GymClass(BaseModel):
    id : str = None
    gym_id : str = None
    schedule: Schedule = None 
    professor : str
    type : str
    description: str = ""
    max_capacity : int = 1
    people : int = 0

    def has_spot(self)->bool:
        return self.people<self.max_capacity

    def reserve_place(self,user):
        self.people = self.max_capacity if self.people==self.max_capacity else self.people+1
        
    def unbook_place(self,user):
        self.people = 0 if self.people==0 else self.people-1

    def collides(self,other_class:"GymClass"):
        return self.schedule.collides(other_class.schedule)

    def to_dict(self):
        return {
            "id": self.id ,
            "gym_id": self.gym_id ,
            "professor": self.professor ,
            "type": self.type ,
            "description":self.description,
            "max_capacity": self.max_capacity,
            "schedule": self.schedule.to_dict(),
            "people": self.people
        }
    
    def from_dict(spec:dict):
        spec["schedule"] = Schedule.from_dict(spec["schedule"])
        return GymClass(**spec)

class Gym(BaseModel):
    id : str = None
    name : str
    location : Location
    image : str = None
    classes : List[GymClass] = []
    description : str = ""
    contact_info : str = ""

    def add_class(self,some_class:GymClass):
        some_class.gym_id = self.id
        self.classes.append(some_class)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location.to_dict(),
            "description": self.description,
            "contact_info": self.contact_info
        }
    
    def from_dict(spec:dict):
        spec["classes"] = [GymClass.from_dict(c) for c in spec.get("classes",[])]
        return Gym(**spec)
