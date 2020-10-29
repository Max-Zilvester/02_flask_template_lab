from app import app
from app.models.event import *
from flask import render_template, request
from app.models.event_list import *


@app.route("/")
def index():
    return render_template("index.html", title="Home", events=events)


@app.route("/add-event", method=["POST"])
def add_event():
    events_date = request.form["date"]
    events_name = request.form["name"]
    events_number_of_guests = request.form["number_of_guests"]
    events_room_location = request.form["room_location"]
    events_description = request.form["description"]
    new_event = Event(
        events_date,
        events_name,
        events_number_of_guests,
        events_room_location,
        events_description,
    )
    add_new_event(new_event)
    return render_template("index.html", title="Home", events=events)