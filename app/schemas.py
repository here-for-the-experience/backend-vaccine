from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

class Vaccine(BaseModel) :
    name : str

class Vaccination(BaseModel) :
    token : str
    vaccine_id : Optional[int] = 1 
    vaccination_date : Optional[date] = date.today()
    certificate_url : Optional[str] = None

class TokenData(BaseModel) :
    id : int
    role_id : int

class Token(BaseModel) :
    token : str

class Approve(BaseModel) :
    token : str
    vaccination_id : int