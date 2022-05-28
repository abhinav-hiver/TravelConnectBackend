import profile
from src.api.schema.request import TripPatchRequest, TripRequest, TripStatusRequest, UserPatchRequest, UserRequest
from src.api.schema.response import TripDataResponse, UserDataResponse
from src.database.db import db_session
import logging
from src.database.db_repository import DbRepositories
from src.models.trips import Trips
from src.models.users import Users

logger = logging.getLogger("backend")
db_session = db_session()


def add_new_user(request: UserRequest):
        user = Users(
            name=request.name, 
            contact_no=request.contact_no,
            email_id=request.email_id,
            age=request.age,
            interests=request.interests,
            profile_photo=request.profile_photo,
            places_visited=request.places_visited,
            other_info=request.other_info
        )
        db_session.add(user)
        db_session.flush()

def get_user_by_id(user_id: str):
    user = Users.get({"id": user_id}).first()
    return UserDataResponse(
        name=user.name, 
        contact_no=user.contact_no,
        email_id=user.email_id,
        age=user.age,
        interests=user.interests,
        profile_photo=user.profile_photo,
        places_visited=user.places_visited,
        other_info=user.other_info
    )

def update_user_by_user_id(user_id: str, request: UserPatchRequest):
    db_repositories = DbRepositories(user_id)
    db_repositories.update__user_details(request)

def add_new_trip(request: TripRequest):
        trip = Trips(
            hosted_by=request.hosted_by, 
            destination=request.destination,
            duration=request.duration,
            events=request.events,
            status=request.status,
            additional_info=request.additional_info,
            date_from=request.date_from,
            date_to=request.date_to
        )
        db_session.add(trip)
        db_session.flush()

def get_all_trips():
    trips = Trips.fetch_all()
    res = []
    for trip in trips:
        res.append(
            TripDataResponse(
                hosted_by=trip.hosted_by, 
                destination=trip.destination,
                duration=trip.duration,
                events=trip.events,
                status=trip.status,
                additional_info=trip.additional_info,
                date_from=trip.date_from,
                date_to=trip.date_to
            )
        )
    return res

def get_trip_by_id(trip_id: str):
    trip = Trips.get({"id": trip_id}).first()
    return TripDataResponse(
        hosted_by=trip.hosted_by, 
        destination=trip.destination,
        duration=trip.duration,
        events=trip.events,
        status=trip.status,
        additional_info=trip.additional_info,
        date_from=trip.date_from,
        date_to=trip.date_to
    )

def update_trip_by_id(trip_id: str, request: TripPatchRequest):
    db_repositories = DbRepositories(trip_id)
    db_repositories.update__trip_details(request)

def get_trip_status_by_id(trip_id: str, request: TripStatusRequest):
    db_repositories = DbRepositories(trip_id)
    db_repositories.update__trip_status(request)

def get_trip_by_user_id(user_id: str):
    trips = Trips.get({"hosted_by": user_id}).all()
    res = []
    for trip in trips:
        res.append(
            TripDataResponse(
                hosted_by=trip.hosted_by, 
                destination=trip.destination,
                duration=trip.duration,
                events=trip.events,
                status=trip.status,
                additional_info=trip.additional_info,
                date_from=trip.date_from,
                date_to=trip.date_to
            )
        )
    return res