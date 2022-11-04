from pydantic import BaseModel
import math

class Location(BaseModel):
    latitude : float
    longitude: float

    def near_by(self,location:"Location",max_distance:int=100):
        distance = math.dist([self.latitude,self.longitude], [location.latitude,location.longitude])
        return distance<=max_distance

    def to_dict(self):
        return {
            "latitude":self.latitude,
            "longitude":self.longitude
        }
    
    def from_dict(spec):
        return Location(**spec)