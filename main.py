from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, select, Field, create_engine, Session
from typing import Optional, List, Annotated

class HeroBase(SQLModel):
    name : str
    age : int | None
 
class Hero(HeroBase, table = True):
    id : int | None = Field(default=None, primary_key=True)
    
class CreateHero(HeroBase):
     age : int | None
     
class ResponseHero(HeroBase):
        id : int
class HeroUpdate(SQLModel):
     name : str | None = None
     age  : int | None = None     

db_url = "postgresql://aamirlucky60:AhJX4ZpVc8mS@ep-weathered-base-a51yuvs0.us-east-2.aws.neon.tech/practise?sslmode=require"
engine = create_engine(db_url, echo=True)

def creatr_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.on_event("startup")
def on_startup():
     creatr_tables()

#dependency injection

def get_db():
    with Session(engine) as session :
        yield session

#get method
@app.get("/hero", response_model=List[Hero])
def get_data(session: Annotated[Session, Depends(get_db)]):        
    heros = session.exec(select(Hero)).all()
    return heros

#post method
@app.post("/heros", response_model=ResponseHero)
def post_data(hero:CreateHero, db: Annotated[Session, Depends(get_db)]):
        hero_to_insert = Hero.model_validate(hero)
        db.add(hero_to_insert)
        db.commit()
        db.refresh(hero_to_insert)
        return hero_to_insert

# get method with id
@app.get("/hero/{hero_id}", response_model=ResponseHero)
def get_data_by_id(hero_id: int, session : Annotated[Session, Depends(get_db)]):
    get_data = session.get(Hero, hero_id)
    if not hero_id:
         raise HTTPException(status_code=404, detail="hero not found")
    return get_data

#update method
@app.patch("/hero/{hero_id}", response_model=ResponseHero)
def update_data(hero_id : int, hero_data : HeroUpdate,session : Annotated[Session, Depends(get_db)]):
     hero = session.get(Hero, hero_id)
     if not hero :
          raise HTTPException(status_code=404, detail="hero not found")
     hero_dict_data = hero_data.model_dump(exclude_unset=True)
     for key, value in hero_dict_data.items():
          setattr(hero, key, value) 
     session.add(hero)
     session.commit()
     session.refresh(hero)
     return hero

#delete method
@app.delete("/hero/{hero_id}")
def delete_data(hero_id : int, session:Annotated[Session, Depends(get_db)]):
     hero = session.get(Hero, hero_id)
     if not hero:
          raise HTTPException(status_code=404, detail="hero not found")
     session.delete(hero)
     session.commit()
     return {"message": "Hero deleted successfully"}

