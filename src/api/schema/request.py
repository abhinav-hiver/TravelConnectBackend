from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    name: str = Field(..., title="Name of the user")
    contact_no: str = Field(..., title="Contact Info of the user")
    email_id: str = Field(..., title="Email ID of the user")
    age: int = Field(..., title="Age of the user")
    interests: str = Field(None, title="Interests of the user")
    profile_photo: str = Field(None, title="Profile Pic of the user")
    places_visited: str = Field(None, title="Places Visited by the user")
    other_info: str = Field(None, title="Other Relevant Information")

class UserPatchRequest(BaseModel):
    name: Optional[str] 
    contact_no: Optional[str]
    email_id: Optional[str] 
    age: Optional[int] 
    interests: Optional[str] 
    profile_photo: Optional[str]
    places_visited: Optional[str]
    other_info: Optional[str]

class TripRequest(BaseModel):
    hosted_by: int = Field(..., title="User ID of user who hosted")
    destination: str = Field(..., title="Destination")
    duration: int = Field(None, title="Duration")
    events: str = Field(None, title="Events")
    status: str = Field("open", title="Status")
    additional_info: str = Field(None, title="Additional Info")
    date_from: str = Field(None, title="Date From")
    date_to: str = Field(None, title="Date To")

class TripPatchRequest(BaseModel):
    destination: Optional[str]
    duration: Optional[int]
    events: Optional[str]
    status: Optional[str]
    additional_info: Optional[str]
    date_from: Optional[str]
    date_to: Optional[str]

class TripStatusRequest(BaseModel):
    status: str = Field(None, title="Status")

