from pydantic import BaseModel


class Reservation(BaseModel):
    user_id : str = None

    def to_dict(self):
        return {
            "user_id":self.user_id
        }
    
    def from_dict(spec):
        return Reservation(**spec)
