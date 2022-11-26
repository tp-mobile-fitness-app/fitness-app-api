from pydantic import BaseModel
import datetime
from dateutil.relativedelta import relativedelta
import math

class Schedule(BaseModel):
    start_hour : float
    end_hour : float
    week_day: int
    start_date: datetime.datetime = None
    end_date: datetime.datetime = None

    def collides(self,other_sched:"Schedule"):
        if self.week_day != other_sched.week_day:
            return False

        includes_other = self.start_hour<=other_sched.start_hour and other_sched.start_hour<=self.end_hour
        other_includes_me = other_sched.start_hour<=self.start_hour and self.start_hour<=other_sched.end_hour

        return includes_other or other_includes_me

    def next_date_from_now(self,date_hour):
        today = datetime.datetime.today()
        if today.weekday()<=self.week_day:
            next_date=today+datetime.timedelta(days = self.week_day-today.weekday())

        else:
            next_date=today+datetime.timedelta(days = 7+self.week_day-today.weekday())

        minutes, hour = math.modf(date_hour)
        minutes = round(minutes*60)

        return datetime.datetime(next_date.year,next_date.month,next_date.day,round(hour),round(minutes))


    def to_dict(self):
        return {
            "start_hour" : self.start_hour,
            "end_hour" : self.end_hour,
            "start_date":self.next_date_from_now(self.start_hour),
            "end_date":self.next_date_from_now(self.end_hour),
            "week_day": self.week_day
        }

    def from_dict(sched_spec:dict):
        return Schedule(**sched_spec)