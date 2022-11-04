from apps.models.location import Location
from apps.models.gym.gym import Gym
from pydantic import BaseModel



class GymSearch(BaseModel):
    name : str = None
    near_point : Location = None
    search_radius : int = 100

    def matches(self,gym:Gym):
        matched = True

        if self.name:
            matched = matched and self.name in gym.name

        if self.near_point:
            matched = matched and self.near_point.near_by(gym.location,self.search_radius)
        
        return matched

    def to_dict(self):
        return {
            "name":self.name,
            "near_point":self.near_point.to_dict(),
            "search_radius":self.search_radius
        }
    
    def from_dict(spec):
        return GymSearch(**spec)
