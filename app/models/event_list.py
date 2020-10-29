from app.models.event import *

event_1 = Event("29/10/2020", "Birthday", 10, "first floor", "Neal's birthday party")
event_2 = Event("01/03/2019", "Hiking", 5, "mountain side", "exploring the mountains")
events = [event_1, event_2]


def add_new_event(event):
    events.append(event)
