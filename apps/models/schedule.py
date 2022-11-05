from pydantic import BaseModel

class Schedule(BaseModel):
    start_hour : float
    end_hour : float
    week_day: int

    def collides(self,other_sched:"Schedule"):
        if self.week_day != other_sched.week_day:
            return False

        includes_other = self.start_hour<=other_sched.start_hour and other_sched.start_hour<=self.end_hour
        other_includes_me = other_sched.start_hour<=self.start_hour and self.start_hour<=other_sched.end_hour

        return includes_other or other_includes_me

    def to_dict(self):
        return {
            "start_hour" : self.start_hour,
            "end_hour" : self.end_hour,
            "week_day": self.week_day
        }

    def from_dict(sched_spec:dict):
        return Schedule(**sched_spec)