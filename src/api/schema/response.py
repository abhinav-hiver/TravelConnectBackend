from datetime import datetime
from os import access
from typing import List, Literal, Union

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    return_message: str = Field(..., title="Message from the server")


class UserDataResponse(BaseModel):
    name: str = Field(..., title="Name of the user")
    contact_no: str = Field(..., title="Contact Info of the user")
    email_id: str = Field(None, title="Email ID of the user")
    age: int = Field(None, title="Age of the user")
    interests: str = Field(None, title="Interests of the user")
    profile_photo: str = Field(None, title="Profile Pic of the user")
    places_visited: str = Field(None, title="Places Visited by the user")
    other_info: str = Field(None, title="Other Relevant Information")

class TripDataResponse(BaseModel):
    hosted_by: int = Field(..., title="User ID of user who hosted")
    destination: str = Field(..., title="Destination")
    duration: int = Field(None, title="Duration")
    events: str = Field(None, title="Events")
    status: str = Field(None, title="Status")
    additional_info: str = Field(None, title="Additional Info")
    date_from: datetime = Field(None, title="Date From")
    date_to: datetime = Field(None, title="Date To")
