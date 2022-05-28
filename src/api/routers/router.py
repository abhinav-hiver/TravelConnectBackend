import logging
import os
from typing import List

from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from src.api.schema.request import TripPatchRequest, TripRequest, TripStatusRequest, UserPatchRequest, UserRequest

from src.api.schema.response import TripDataResponse, UserDataResponse
from src.modules.api_manager import add_new_trip, add_new_user, get_all_trips, get_trip_by_id, get_trip_by_user_id, get_trip_status_by_id, get_user_by_id, update_trip_by_id, update_user_by_user_id


os.path.join(os.getcwd(), "src")

router = APIRouter()


#######################################
#       Backend APIS              #
#######################################
log = logging.getLogger("backend")

@router.post("/user/add")
def add_user(request: UserRequest):
    log.info(f"Add User API request : {jsonable_encoder(request)}")
    add_new_user(request)
    return {"200" : "OK"}

@router.get("/user/fetch/{user_id}", response_model=UserDataResponse)
def fetch_user(user_id: int):
    log.info(f"Fetch User API request")
    return get_user_by_id(user_id)

@router.patch("/user/update/{user_id}")
def update_user(user_id: int, request: UserPatchRequest):
    log.info(f"Update User API request : {jsonable_encoder(request)}")
    update_user_by_user_id(user_id, request)
    return {"200" : "OK"}

@router.get("/user/fetch_trip/{user_id}", response_model=List[TripDataResponse])
def fetch_user(user_id: int):
    log.info(f"Fetch Trip by User ID API request")
    return get_trip_by_user_id(user_id)


# ## Trip APIs
@router.post("/trip/add")
def add_trip(request: TripRequest):
    log.info(f"Add Trip API request : {jsonable_encoder(request)}")
    add_new_trip(request)
    return {"200" : "OK"}

@router.get("/trip/fetch_all", response_model=List[TripDataResponse])
def fetch_trip():
    log.info(f"Fetch All Trips API request")
    return get_all_trips()

@router.get("/trip/fetch/{trip_id}", response_model=TripDataResponse)
def fetch_trip(trip_id: int):
    log.info(f"Fetch Trip API request")
    return get_trip_by_id(trip_id)

@router.patch("/trip/update_details/{trip_id}")
def update_trip(trip_id: int, request: TripPatchRequest):
    log.info(f"Update Trip API request : {jsonable_encoder(request)}")
    update_trip_by_id(trip_id, request)
    return {"200" : "OK"}

@router.patch("/trip/update_status/{trip_id}")
def update_trip_status(trip_id: int, request: TripStatusRequest):
    log.info(f"Update Trip Status by ID API request: {jsonable_encoder(request)}")
    get_trip_status_by_id(trip_id, request)
    return {"200" : "OK"}
