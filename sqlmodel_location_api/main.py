from fastapi import FastAPI, HTTPException, Depends, status
from model import SQLModel, Session, Location, engine, select
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI( title = "location finder api",
               version = "1.0.0",
               servers = [
                   {
                        "url" : "https://active-snipe-uniquely.ngrok-free.app/",
                        "description" : "Production Server"
               },
               
                {
                        "url" : "http://127.0.0.1:8000",
                        "description" : "Development server"

               }
               
               ])
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

    
#get request for name by name

@app.get("/persons")
def get_all_data() :
    with Session(engine) as session:
        loc_data_all = session.exec(select(Location)).all()
        
        return loc_data_all
      
#post request

@app.post("/person/")
def create_data (location : Location):
    with Session(engine) as session:
        session.add(location)
        session.commit()
        session.refresh(location)
        return location    

# dependency injection:
def get_location_or_404(name: str)->Location:
    with Session(engine) as session:
        get_data = session.exec(select(Location).where(Location.name == name)).first()
        if not get_data :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="location not found")
        return get_data

#Get request(all)
    
@app.get("/location/{name}")
def get_data(name : str, location: Annotated[Location, Depends(get_location_or_404)]):
        """
    Retrieve the location of a person by their name.

    Args:
        name (str): The name of the person.

    Returns:
        Location: The location of the person.
        """
        
        return location
