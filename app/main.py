from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from . import models, database, schemas
from .database import get_db
from datetime import date
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

import os
from dotenv import load_dotenv
load_dotenv()

USER_SERVER_URL = f"https://{os.getenv('AUTH_PREFIX')}auth.redevops.store/"

app = FastAPI()

origins = [
    "http://dev.redevops.store",
    "http://redevops.store",
    "http://dev.api.redevops.store",
    "http://api.redevops.store",
    "http://dev.auth.redevops.store",
    "http://auth.redevops.store",
    "http://dev.admin.redevops.store",
    "http://admin.redevops.store",

    "https://dev.redevops.store",
    "https://redevops.store",
    "https://dev.api.redevops.store",
    "https://api.redevops.store",
    "https://dev.auth.redevops.store",
    "https://auth.redevops.store",
    "https://dev.admin.redevops.store",
    "https://admin.redevops.store",
    
    "http://localhost",
    "http://localhost:8001",
    "http://localhost:5173",

    "http://127.0.0.1",
    "http://127.0.0.1:8001",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- UTILS ---
SECRET_TOKEN = "0123456789"
ALGORITHM = "HS256"
EXPIRATION_TIME = 24 * 60 * 7
def verify_access_token(token : str, credentials_exception) :
    try :
        payload = jwt.decode(token, SECRET_TOKEN, algorithms=[ALGORITHM])
        id = payload.get("id")
        if not id :
            raise credentials_exception
        token_data = schemas.TokenData(id = payload.get("id"), role_id = payload.get("role_id"))
    except JWTError :
        raise credentials_exception
    return token_data

# -----
# POST API THAT TAKES token as header; date in body, parses the token, retrive user_id and create a vaccination record
# -----
@app.post("/create", tags=["Vaccination"], status_code=201)
def create_vaccination(Token : schemas.Token, db : Session = Depends(get_db)) :
    
    user_id = verify_access_token(Token.token, HTTPException(status_code=401, detail="Invalid Token")).id

    new_vaccination = models.Vaccination(user_id=user_id, vaccine_id=1, vaccination_date=date.today(), certificate_url="https://www.wits.ac.za/media/wits-university/mandatory-vaccinations/images/Vaccination%20policy%20400x4002.jpg")

    db.add(new_vaccination)
    try :
        db.commit()
    except :
        raise HTTPException( status_code = 400, detail = { "message" : "Some error occured"})
    db.refresh(new_vaccination)
    return {
        "success": True
    }

@app.post("/myvaccine", tags=["Vaccine"], status_code=201) 
def my_vaccine(Token : schemas.Token, db : Session = Depends(get_db)) :
    user_id = verify_access_token(Token.token, HTTPException(status_code=401, detail="Invalid Token")).id
    # return the Vaccination of the user
    vaccination = db.query(models.Vaccination).filter(models.Vaccination.user_id == user_id).first()

    return {
        vaccination
    }


@app.post("/allvaccines", tags=["Vaccine"]) 
def allvaccine(Token : schemas.Token, db : Session = Depends(get_db)) :
    user_id = verify_access_token(Token.token, HTTPException(status_code=401, detail="Invalid Token")).id
    role_id = verify_access_token(Token.token, HTTPException(status_code=401, detail="Invalid Token")).role_id

    if role_id == 2:
        # return the Vaccination of the user
        vaccination = db.query(models.Vaccination).all()
        # retur all the vaccination in json
        return vaccination
    else:
        raise HTTPException( status_code = 401, detail = { "message" : "You are not authorized to access this resource"})
    

@app.post("/approve", tags=["Vaccine"]) 
def approveVaccine(Approve : schemas.Approve, db : Session = Depends(get_db)) :
    user_id = verify_access_token(Approve.token, HTTPException(status_code=401, detail="Invalid Token")).id
    role_id = verify_access_token(Approve.token, HTTPException(status_code=401, detail="Invalid Token")).role_id

    if role_id == 2:
        # approve the vaccination of Approve.vaaccination_id
        vaccination = db.query(models.Vaccination).filter(models.Vaccination.id == Approve.vaccination_id).first()
        vaccination.verified = True
        db.commit()
        db.refresh(vaccination)
        return {
            "success": True
        }
    else:
        raise HTTPException( status_code = 401, detail = { "message" : "You are not authorized to access this resource"})
    





# @app.get("/vaccine/{user_id}", tags=["vaccine"], status_code=200)
# def get_vaccine(user_id : int, db : Session = Depends(get_db)) :
#     vaccine = db.query(models.Vaccine).filter(models.Vaccine.id == user_id).first()
#     return vaccine


