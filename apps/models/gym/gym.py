from datetime import datetime
from typing import List
from apps.models.location import Location
from pydantic import BaseModel


class GymClass(BaseModel):
    id : str = None
    start_date : datetime = None
    end_date : datetime = None
    professor : str
    type : str
    max_capacity : int = 1
    people : int = 0

    def has_spot(self)->bool:
        return self.people<self.max_capacity

    def reserve_place(self,user):
        self.people+=1

    def collides(self,other_class:"GymClass"):
        includes_other = self.start_date<=other_class.start_date and other_class.start_date<=self.end_date
        other_includes_me = other_class.start_date<=self.start_date and self.start_date<=other_class.end_date

        return includes_other or other_includes_me

    def to_dict(self):
        return {
            "id": self.id ,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "professor": self.professor ,
            "type": self.type ,
            "max_capacity": self.max_capacity,
            "people": self.people
        }
    
    def from_dict(spec):
        return GymClass(**spec)

class Gym(BaseModel):
    id : str = None
    name : str
    location : Location
    classes : List[GymClass] = []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location.to_dict()
        }
    
    def from_dict(spec):
        return Gym(**spec)
