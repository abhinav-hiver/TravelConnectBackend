from ast import Store
from black import re
from pytest_mock import session_mocker
from src.api.schema.request import TripPatchRequest, TripStatusRequest, UserPatchRequest, UserRequest
from src.models.trips import Trips
from src.models.users import Users
import logging
from sqlalchemy import func
from src.database.db import db_session

db_session = db_session()
logger = logging.getLogger("backend")


class DbRepositories:
    def __init__(self, user_id):
        self.user_id = user_id

    def update__user_details(self, request: UserPatchRequest):
        if request.name != None:
            Users.update(
                {"id": self.user_id},
                name=request.name, 
            )
        
        if request.contact_no != None:
            Users.update(
                {"id": self.user_id},
                contact_no=request.contact_no,
            )
        
        if request.email_id != None:
            Users.update(
                {"id": self.user_id},
                email_id=request.email_id,
            )
        
        if request.age != None:
            Users.update(
                {"id": self.user_id},
                age=request.age,
            )
        
        if request.interests != None:
            Users.update(
                {"id": self.user_id},
                interests=request.interests,
            )
        
        if request.profile_photo != None:
            Users.update(
                {"id": self.user_id},
                profile_photo=request.profile_photo,
            )
        
        if request.places_visited != None:
            Users.update(
                {"id": self.user_id},
                places_visited=request.places_visited,
            )
        
        if request.other_info != None:
            Users.update(
                {"id": self.user_id},
                other_info=request.other_info,
            )

        logger.info("Updated main user's details")

    def update__trip_details(self, request: TripPatchRequest):
        if request.destination != None:
            Trips.update(
                {"id": self.user_id},
                destination=request.destination,
            )
        
        if request.duration != None:
            Trips.update(
                {"id": self.user_id},
                duration=request.duration,
            )
        
        if request.events != None:
            Trips.update(
                {"id": self.user_id},
                events=request.events,
            )
        
        if request.status != None:
            Trips.update(
                {"id": self.user_id},
                status=request.status,
            )
        
        if request.additional_info != None:
            Trips.update(
                {"id": self.user_id},
                additional_info=request.additional_info,
            )
        
        if request.date_from != None:
            Trips.update(
                {"id": self.user_id},
                date_from=request.date_from,
            )
        
        if request.date_to != None:
            Trips.update(
                {"id": self.user_id},
                date_to=request.date_to,
            )

        logger.info("Updated Trip's details")

    def update__trip_status(self, request: TripStatusRequest):
        Trips.update(
            {"id": self.user_id},
            status=request.status, 
        )
        
        logger.info("Updated Trip's Status")