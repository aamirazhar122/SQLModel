from fastapi import FastAPI, HTTPException, Depends
from database import Location, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated

app : FastAPI = FastAPI(
     title = "Location Finder API", 
     version = "1.0.0",
     servers = [
         {
              
            "url" : "https://casual-globally-jaybird.ngrok-free.app/",
            "description" : "Production Server"

    },
    {
            "url" : "http://localhost:8000",
            "description" : "Development Server"

    }])

class Check_Location(BaseModel):
    name : str
    location : str
    
# dependancy injection

def get_db():
        db = SessionLocal()
        try : 
            yield db
        finally:
            db.close()    


@app.get("/location/{name}")
def get_person_loaction(name : str, db : Session = Depends(get_db)):
    location = db.query(Location).filter(Location.name == name).first()

    if location is None:
         raise HTTPException(status_code=404, detail = "Location not found")
    
    return{"name" : location.name , "location" : location.location}



